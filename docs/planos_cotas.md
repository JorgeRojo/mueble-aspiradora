# Planos Técnicos y Esquemas de Cotas: Mueble Aspiradora 480 mm

Este documento recoge el esquema dimensional y los planos de referencia gráfica del mueble recibidor a **Cota Cero** ($480 \times 790 \times 560\text{ mm}$).

---

## 1. Vistas y Renders Disponibles

* **Fotografía Realista Principal (Acabado en Recibidor)**: [`../foto_realista_mueble_recibidor.jpg`](../foto_realista_mueble_recibidor.jpg)
  * Muestra el mueble monolítico terminado lacado en blanco satinado apoyado a cota cero sobre parqué en espiga, con el robot Dreame saliendo por el vano inferior y decoración superior.
* **Variante con Puerta Suspendida**: [`../foto_realista_mueble_recibidor_alt.jpg`](../foto_realista_mueble_recibidor_alt.jpg)
* **Render Fotorrealista con Cotas Milimétricas**: [`../render_mueble_realista_cotas.jpg`](../render_mueble_realista_cotas.jpg)
  * Puerta abierta a $80^\circ$, compuerta levantada, base Dreame interior y cotas en líneas negras.
* **Plano Wireframe CAD / Blueprint**: [`../render_mueble_wireframe.jpg`](../render_mueble_wireframe.jpg)
* **Visor 3D Interactivo WebGL (Three.js)**: [`../render_3d_photorealistic.html`](../render_3d_photorealistic.html)

---

## 2. Esquema de Cotas en Alzado Frontal (Puerta Cerrada)

```
        480 mm (Ancho Exterior)
<---------------------------------------->
+----------------------------------------+  ^
|     ENCIMERA SUPERIOR (Compuesto 25 mm)|  |
+----------------------------------------+  |
|   RANURA SUPERIOR DE ACCESORIOS (40 mm)|  |
+----------------------------------------+  |
|                                        |  |
|                                        |  |
|                                        |  |
|          PUERTA PRINCIPAL              |  | 790 mm (Alto Total Exterior)
|       (Lacado blanco satinado)         |  |
|                                        |  |
|                                        |  |
|   +--------------------------------+   |  |
|   | COMPUERTA GUILLOTINA CERRADA   |   |  |
|   |     410 mm x 140 mm            |   |  |
|---|--------------------------------|---|  |  ^ 117 mm (Alto vano)
|45 | Vano paso robot: 390 mm ancho  |45 |  v  v
+===+================================+===+  ===== Suelo / Cota Cero
```

---

## 3. Esquema de Cotas en Alzado Frontal (Puerta Abierta - Interior)

```
        480 mm (Ancho Exterior)
        430 mm (Hueco Interior Libre)
<---------------------------------------->
+---+--------------------------------+---+  ^
|   |    ENCIMERA SUPERIOR (25 mm)   |   |  |
|   +--------------------------------+   |  |
|   |  Ranura superior útil (40 mm)  |   |  |
|   +--------------------------------+   |  |
| 25|    Balda interior (25 mm)      | 25|  |
| mm+--------------------------------+ mm|  | 790 mm (Alto Total Exterior)
|   |                                |   |  |
| c | Espacio libre depósitos: 132 mm| c |  |
| o | (Extracción cómoda de agua)    | o |  |
| s + - - - - - - - - - - - - - - - -+ s |  |  ^
| t |                                | t |  |  |
| a |      BASE DREAME               | a |  |  | 568 mm (Alto Base)
| d |      (Ancho: 423 mm)           | d |  |  |
| o |      [Holgura: 3.5 mm/lado]    | o |  |  |
|   |                                |   |  |  |
|   |          ROBOT Ø350 mm         |   |  |  |
+===+================================+===+  v  v Suelo / Cota Cero
```

---

## 4. Esquema de Cotas en la Cara Interior de la Puerta (Abierta)

```
                       480 mm
<---------------------------------------------------->
+----------------------------------------------------+  ^
|                                                    |  |
|                   [Bisagra 165°]                   |  |
|                   (Cazoleta Ø35)                   |  |
|                       |                            |  |
|                   +---+---+                        |  |
|                   | MOTOR |                        |  |
|                   | MINI  |                        |  |
|                   | 150N  |                        |  |
|                   +---+---+                        |  |
|                   | ACT.  |                        |  |
|                   | TUB.  |                        |  |
|                   +---+---+                        |  |
|                       |                            |  | 790 mm
|                 [Vástago 150 mm]                   |  |
|                   Carrera útil                     |  |
|                       |                            |  |
|     +==+        +-----------+        +==+          |  |
|     |  |        | SOPORTE   |        |  |          |  |
|     |  |  +-----+-----------+-----+  |  |          |  |
|     |R |  |                       |  |R |          |  |
|     |I |  | COMPUERTA GUILLOTINA  |  |I | 140 mm   |  |
|     |E |  | ELEVADA               |  |E | alto     |  |
|     |L |  | 410 mm ancho          |  |L | panel    |  |
|     |  |  +-----------------------+  |  |          |  |
|     |U |                             |U |          |  |
|     |20|      VANO PASO ROBOT        |20|          |  |
|     |mm|      100% DESPEJADO         |mm|          |  |
| 45mm|  |      390 mm x 117 mm        |  | 45mm     |  | ^ 117 mm
+=====+==+=============================+==+=====+====+  v Suelo (Cota Cero)
```

---

## 5. Tabla Resumen de Tolerancias y Holguras Críticas

| Componente | Dimensión Pieza | Dimensión Hueco | Holgura Resultante | Evaluación |
| :--- | :--- | :--- | :--- | :--- |
| **Base Dreame (Ancho)** | 423 mm | 430 mm interior | **7.0 mm total (3.5 mm/lado)** | Ajuste preciso, sin vibración. |
| **Depósitos de agua (Alto)** | 568 mm base | 700 mm a balda | **132 mm libres** | Extracción cómoda de depósitos hacia arriba. |
| **Paso del Robot (Ancho)** | 350 mm diámetro | 390 mm vano | **40 mm total (20 mm/lado)** | Margen seguro de atraque. |
| **Paso del Robot (Alto)** | 97 mm con LiDAR | 117 mm vano | **20 mm superior** | Evita cualquier roce de torreta láser. |
| **Elevación Compuerta** | 117 mm vano | 125 mm alzada | **8 mm sobre vano** | Hueco 100% despejado a ras de suelo. |
| **Fondo para rampa y actuador**| 493 mm base + 35 mm actuador | 560 mm exterior | **32 mm libres** | Todo entra sin colisión al cerrar la puerta. |
