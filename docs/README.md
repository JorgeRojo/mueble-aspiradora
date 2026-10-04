# Documentación Técnica: Proyecto Mueble Consola Dreame a Cota Cero

Bienvenido al repositorio de documentación técnica para la fabricación, despiece y montaje del mueble recibidor a medida para la estación robot aspirador **Dreame L10s / X40**.

---

## Índice de Documentos

1. ### [Especificaciones Técnicas y Constructivas (`especificaciones_tecnicas.md`)](especificaciones_tecnicas.md)
   * **Dimensiones exteriores**: $480\text{ mm}$ (ancho) $\times 790\text{ mm}$ (alto) $\times 560\text{ mm}$ (fondo).
   * **Arquitectura interior y Cota Cero**: Concepto autoportante sin suelo, zócalo ni trasera.
   * **Técnica constructiva de nervios**: Paneles de contrachapado de 10 mm con regrueso perimetral de 15 mm ($10 + 15 = 25\text{ mm}$). Peso total ultraligero ($\approx 8,5\text{ kg}$).
   * **Mecanismo de compuerta guillotina**: Compuerta de $410 \times 140\text{ mm}$, micro actuador lineal 12V 150N (carrera 150 mm) y rieles en "U" de $20\text{ mm}$.
   * **Despiece completo de láminas**: Corte sobre tableros de $60 \times 120\text{ cm}$.
   * **Lista de materiales comerciales (BOM)**: Herrajes, bisagras de $165^\circ$, actuador y electrónica de control Zigbee.
   * **Esquema de cableado y automatización**: Puente en H con módulo Zigbee 2 canales MHCOZY e integración con Home Assistant.

2. ### [Planos Técnicos y Esquemas de Cotas (`planos_cotas.md`)](planos_cotas.md)
   * Esquema dimensional en alzado frontal con puerta cerrada.
   * Esquema dimensional interior con puerta abierta y base Dreame.
   * Esquema de distribución de herrajes en la cara interior de la puerta.
   * Tabla de tolerancias y holguras críticas de funcionamiento.

---

## Archivos Gráficos y Renders Asociados

* **Fotografía Realista Principal (Recibidor)**: [`../foto_realista_mueble_recibidor.jpg`](../foto_realista_mueble_recibidor.jpg)
* **Fotografía Realista Variante (Puerta Suspendida)**: [`../foto_realista_mueble_recibidor_alt.jpg`](../foto_realista_mueble_recibidor_alt.jpg)
* **Render Fotorrealista 3D con Cotas Milimétricas**: [`../render_mueble_realista_cotas.jpg`](../render_mueble_realista_cotas.jpg)
* **Visor 3D Interactivo WebGL (Three.js)**: [`../render_3d_photorealistic.html`](../render_3d_photorealistic.html)
* **Plano Wireframe CAD / Blueprint**: [`../render_mueble_wireframe.jpg`](../render_mueble_wireframe.jpg)
