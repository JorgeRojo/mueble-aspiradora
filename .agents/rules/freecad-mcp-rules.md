# FreeCAD MCP (`freecad-mcp`) — Non-Obvious Rules & Best Practices

These rules address internal behaviors of the `freecad-mcp` XML-RPC bridge (`rpc_server.py`, `gui_dispatch.py`, `view_manager.py`) and FreeCAD 1.1 (OCCT / Coin3D / TechDraw) on macOS that are not evident from the MCP tool schemas alone.

---

## 1. Modal Dialog Deadlocks & Crash Recovery (`activeModalWidget` Guard)

* **Internal Mechanism**: `gui_dispatch.py` checks `QtWidgets.QApplication.activeModalWidget() is not None` on every tick and refuses to run any queued MCP task while a modal dialog is open.
* **The Crash-Recovery Trap**: If FreeCAD crashes or is killed (`kill -9`), its next startup opens a modal *"Document Recovery"* dialog before processing RPC requests, wedging every MCP tool call until timeout (`a modal dialog is open in FreeCAD`).
* **Mandatory Rule**:
  * Before launching or restarting FreeCAD from the CLI, **always** remove stale recovery files first:
    `rm -rf ~/Library/Caches/FreeCAD/v1-1/Cache/FreeCAD_Doc_* ~/Library/Caches/FreeCAD/Cache/FreeCAD_Doc_*`
  * Never open blocking `QtWidgets.QMessageBox` or modal file dialogs inside `execute_code`.

---

## 2. 3D View vs. TechDraw MDI Tab Traps (`get_view` & `saveImage`)

* **Internal Mechanism**:
  * Calling `page.ViewObject.show()` brings a `TechDraw::DrawPage` MDI tab to the front.
  * When a TechDraw tab is in front, `FreeCADGui.activeView()` returns `TechDrawGui::MDIViewPage` instead of `Gui::View3DInventor`.
  * Consequently, calling `get_view` or `Gui.activeDocument().activeView().saveImage(...)` while a TechDraw tab is active fails (`The tab in front is not a 3D view` or `AttributeError: 'TechDrawGui.MDIViewPage' object has no attribute 'saveImage'`).
  * Furthermore, `FreeCADGui` has **no** `Gui.MDIView` class attribute (`AttributeError`).
* **Mandatory Rule**:
  * Inside `execute_code`, always retrieve the 3D view explicitly via `mdiViewsOfType`:
    ```python
    gdoc = Gui.getDocument(doc.Name)
    views3d = gdoc.mdiViewsOfType("Gui::View3DInventor")
    if views3d:
        v = views3d[0]
    ```
  * Always pass `"Framebuffer"` as the 5th argument to `saveImage` (with a 4-arg fallback) to avoid black offscreen GL renders on macOS:
    ```python
    try:
        v.saveImage(out_path, 1600, 1200, "Current", "Framebuffer")
    except TypeError:
        v.saveImage(out_path, 1600, 1200, "Current")
    ```

---

## 3. Preventing OpenGL Near-Plane Clipping ("Cortes" en Vistas 3D)

* **Cause of Clipped 3D Renders**:
  * When rotating the camera manually with `v.setCameraOrientation(...)` followed by `v.fitAll()`, Coin3D sets a tight near/far clipping range around the bounding sphere. Corners of boxes closest to the camera frequently cross the near clipping plane, appearing sliced open ("cortados").
  * Calling `v.getCameraNode()` directly raises `RuntimeError: No SWIG wrapped library loaded`.
* **Mandatory Rule**:
  * After calling `v.fitAll()` on a custom or isometric orientation, always call `v.zoomOut()` once (or increase orthographic camera height via `v.getCamera()` / `v.setCamera(...)`) before `Gui.updateGui()` and `v.saveImage(...)`. This pushes the camera back slightly and expands the near clipping plane so no geometry is ever clipped.

---

## 4. Persistent `_EXEC_NAMESPACE` & Avoiding Duplicate Objects (`Name001`)

* **Internal Mechanism**:
  * `rpc_server.py` executes all `execute_code` calls inside a single persistent dict `_EXEC_NAMESPACE`.
  * Calling `doc.addObject("Part::Feature", "MyPart")` when `"MyPart"` already exists does **not** overwrite it; FreeCAD silently creates `"MyPart001"`, leaving TechDraw views pointing to the stale `"MyPart"`.
* **Mandatory Rule**:
  * Always use an idempotent helper when creating or updating objects in `execute_code`:
    ```python
    obj = doc.getObject(name)
    if obj is None:
        obj = doc.addObject("Part::Feature", name)
    obj.Shape = new_shape
    ```
  * When deleting objects, check `if doc.getObject(name): doc.removeObject(name)`.
  * Never assume the requested document name equals `doc.Name`: FreeCAD sanitizes hyphens/spaces to underscores. Always read `doc.Name`.

---

## 5. TechDraw HLR Performance, `EditableTexts`, and Dimensions

* **Avoid Heavy Helices/Splines in TechDraw**:
  * TechDraw's Hidden Line Removal (HLR) runs synchronously on the GUI thread during `doc.recompute()`. Adding complex swept helices (`Part.makeHelix` + `makePipeShell`, such as multi-turn coil springs) multiplies HLR projection time by $50\text{–}100\times$ and can exceed the 90s `EXECUTE_CODE_TIMEOUT`, permanently marking GUI dispatch as `"stuck"`. Use simplified cylinders/chamfers for small hardware in drawings.
* **`DrawSVGTemplate.EditableTexts` Mutation**:
  * `page.Template.EditableTexts["Title"] = "..."` silently fails because `EditableTexts` returns a copy of the C++ property map. Always copy, modify, and reassign:
    ```python
    texts = dict(page.Template.EditableTexts)
    texts["Title"] = "Nuevo Titulo"
    page.Template.EditableTexts = texts
    ```
* **`DrawViewDimension` Formatting**:
  * Vertex indices (`Vertex0`, `Vertex1`) in a `DrawViewPart` change whenever 3D geometry is modified. If setting an explicit text label in `dim.FormatSpec`, always set `dim.Arbitrary = True` so TechDraw renders the exact `FormatSpec` string rather than substituting a mismatched vertex distance.
* **Exporting TechDraw Pages**:
  * `TechDrawGui.exportPageAsPdf(page, pdf_path)` requires `page.ViewObject.show()` and `Gui.updateGui()` to have been called at least once so the QGraphicsScene for that page is populated.
  * Never use `execute_code_headless` for `TechDrawGui` or `FreeCADGui` operations (`freecadcmd` has no GUI/OpenGL context).
* **`DrawViewAnnotation.X` Center-Anchor Convention**:
  * In TechDraw, `annotation.X` specifies the **horizontal center** of the text block (while `annotation.Y` is the top/vertical anchor), NOT the left edge. On a 297 mm wide A4 landscape page, placing a wide text block on the right half requires `annotation.X` around `195..210 mm` (not `130 mm`), otherwise its left half will overlap views placed on the left side of the sheet.

---

## 6. Safe Multi-Document Handling & 2D-to-3D Link Rotation

* **Rotating Link Bars in the $(Y, Z)$ Plane (`Part.makeBox` along $+Y$)**:
  * A box created with `Part.makeBox(thickness_x, length, width_z)` already extends along the $+Y$ axis ($\theta = 0^\circ$ in the $(Y, Z)$ plane).
  * To align it with a vector $(\Delta Y, \Delta Z)$ at angle $\alpha = \text{atan2}(\Delta Z, \Delta Y)$, rotate around $+X = (1, 0, 0)$ by **`angle_deg`** directly (never `angle_deg - 90.0`), because rotating $(0, L, 0)$ around $+X$ by $\alpha$ yields $(0, L\cos\alpha, L\sin\alpha) = (0, \Delta Y, \Delta Z)$.
* **Safe Multi-Document Handling**:
  * Never call `App.closeDocument()` on the sole active GUI document while its MDI views are open.
  * When exporting a subset of objects to a secondary `.FCStd` file, create the secondary document, copy `.Shape.copy()`, save it, restore `App.setActiveDocument(main_doc.Name)` and `Gui.setActiveDocument(main_doc.Name)`, and only then close the secondary document (or use `Part.export(objs, path)` for STEP/STL).
