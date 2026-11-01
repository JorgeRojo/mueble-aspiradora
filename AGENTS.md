# Guía Técnica Maestra: Mueble Aspiradora Cota Cero (Diseño Final $540 \times 478 \times 620\text{ mm}$)

Este documento recoge las especificaciones definitivas, el despiece de carpintería, la cinemática del mecanismo de apertura de $80^\circ$ y los archivos en producción del mueble cubre-base para la estación **Dreame (L10s / X40)** a cota cero.

---

## 1. Dimensiones y Arquitectura del Diseño Final

* **Dimensiones exteriores totales**: **$540\text{ mm}$ (Ancho) $\times 478\text{ mm}$ (Fondo desde pared) $\times 620\text{ mm}$ (Alto total: $600\text{ mm}$ laterales $+ 20\text{ mm}$ tapa superior doble)**.
* **Hueco interior libre**: **$510\text{ mm}$ (Ancho) $\times 463\text{ mm}$ (Fondo útil tras frente de $15\text{ mm}$) $\times 600\text{ mm}$ (Alto bajo tapa)**.
* **Cota Cero Total**: Estructura autoportante sin suelo de madera inferior; la base Dreame ($423 \times 568\text{ mm}$) apoya directamente sobre el suelo de la estancia.

---

## 2. Despiece de Madera (7 Piezas — 2 Tableros de $15\text{ mm}$ + 1 Tablero de $10\text{ mm}$)

Todos los tableros de partida miden **$1200 \times 600\text{ mm}$**:

1. **`[P01]` Costado Izquierdo ($478 \times 600 \times 15\text{ mm}$ — Tablero #1 de $15\text{ mm}$)**:
   * Rectángulo puro sin cajeados. Aprovecha directamente los $600\text{ mm}$ de ancho del tablero mediante **1 único corte transversal** a $478\text{ mm}$.
2. **`[P02]` Costado Derecho ($478 \times 600 \times 15\text{ mm}$ — Tablero #1 de $15\text{ mm}$)**:
   * Rectángulo puro sin cajeados. Aprovecha directamente los $600\text{ mm}$ de ancho del tablero mediante **1 único corte transversal** a $478\text{ mm}$.
3. **`[P03]` Cubierta Frontal Superior Fija ($510 \times 453 \times 15\text{ mm}$ — Tablero #2 de $15\text{ mm}$)**:
   * Rectángulo puro embutido entre ambos costados ($X \in [15, 525]\text{ mm}, Y \in [-478, -463]\text{ mm}, Z \in [147, 600]\text{ mm}$).
4. **`[P04]` Portón Inferior Abatible $80^\circ$ ($506 \times 143 \times 15\text{ mm}$ — Tablero #2 de $15\text{ mm}$)**:
   * Situado en $Z \in [2, 145]\text{ mm}$ con $2\text{ mm}$ de holgura perimetral e incluye un arco central inferior de **$244\text{ mm}$ de cuerda $\times 22\text{ mm}$ de flecha ($R = 178\text{ mm}$)** para el paso de la torreta LiDAR.
5. **`[P05]` Nervio Trasero Superior ($510 \times 35 \times 15\text{ mm}$ — Tablero #2 de $15\text{ mm}$)**:
   * Listón transversal trasero superior ($X \in [15, 525]\text{ mm}, Y \in [-15, 0]\text{ mm}, Z \in [565, 600]\text{ mm}$), pegado bajo la cara inferior de la tapa superior `[P06]`.
6. **`[P06]` Lámina Superior Base ($540 \times 478 \times 10\text{ mm}$ — Tablero #1 de $10\text{ mm}$)**:
   * Cubre el $100\%$ de la planta superior del mueble ($Z \in [600, 610]\text{ mm}$), apoyando sobre `[P01]`, `[P02]`, `[P03]` y `[P05]`.
7. **`[P07]` Lámina Superior Tapa ($540 \times 478 \times 10\text{ mm}$ — Tablero #1 de $10\text{ mm}$)**:
   * Encolada sobre `[P06]` formando una encimera rígida de $20\text{ mm}$ de espesor ($Z \in [610, 620]\text{ mm}$).

---

## 3. Cinemática del Portón Abatible ($80^\circ$) y Automatización

* **Bisagras Garosa $135 \times 40 \times 35\text{ mm}$ ($80^\circ$) SIN muelles helicoidales**:
  * Pivotes fijos en cara interior de costados: $O_1 = (-451,0,\; 124,0\text{ mm})$ (a $27\text{ mm}$ del frente) y $O_2 = (-431,0,\; 80,0\text{ mm})$ (a $47\text{ mm}$ del frente).
  * Eslabones: $L_1 = 58,21\text{ mm}$, $L_2 = 48,88\text{ mm}$, separación en puerta $d_P = 44,00\text{ mm}$ ($P_1$ a $82\text{ mm}$ y $P_2$ a $38\text{ mm}$ de la base del portón).
* **Actuadores Lineales Dawnso Mini 150N 12V DC ($215\text{ mm}$ cerrado / $325\text{ mm}$ abierto, carrera $110\text{ mm}$)**:
  * Pivote fijo trasero en costado: $A = (-225,7,\; 41,3\text{ mm})$ (a $252,3\text{ mm}$ del canto frontal).
  * Pivote móvil delantero en portón: $B(0^\circ) = (-440,0,\; 24,0\text{ mm}) \to B(80^\circ) = (-546,9,\; 90,8\text{ mm})$.
  * Recorrido exacto: $L_c = 215,0\text{ mm}$ ($\beta_c = -4,6^\circ$) $\to L_o = 325,0\text{ mm}$ ($\beta_o = +8,8^\circ$).
* **Control Zigbee**: Relé MHCOZY de 2 canales con contactos secos en modo **Interlock** e inversión de polaridad (puente en H) alimentado a 12V DC.

---

## 4. Archivos Maestros en Producción

* [`Mueble_Aspiradora_Cota_Cero.FCStd`](file:///Users/jorge/projects/mueble-aspiradora/Mueble_Aspiradora_Cota_Cero.FCStd): Modelo CAD 3D cerrado + 6 hojas TechDraw ISO A4.
* [`Modulo_01_Porton_Abierto_80deg.FCStd`](file:///Users/jorge/projects/mueble-aspiradora/Modulo_01_Porton_Abierto_80deg.FCStd): Modelo CAD 3D con portón abierto a $80^\circ$.
* [`Mecanismo_Metalico_Bisagras_y_Actuadores.FCStd`](file:///Users/jorge/projects/mueble-aspiradora/Mecanismo_Metalico_Bisagras_y_Actuadores.FCStd) y [`planos/Mecanismo_Metalico_Bisagras_y_Actuadores.step`](file:///Users/jorge/projects/mueble-aspiradora/planos/Mecanismo_Metalico_Bisagras_y_Actuadores.step): Modelo CAD 3D de herrajes y actuadores.
* [`planos/Planos_Corte_Madera_Diseño_Final_A4.pdf`](file:///Users/jorge/projects/mueble-aspiradora/planos/Planos_Corte_Madera_Diseño_Final_A4.pdf): Dossier de 2 hojas A4 de corte y despiece de madera.
* [`planos/Planos_Mueble_Aspiradora_Completo_A4.pdf`](file:///Users/jorge/projects/mueble-aspiradora/planos/Planos_Mueble_Aspiradora_Completo_A4.pdf): Dossier maestro completo de 6 hojas A4.
* [`.agents/rules/freecad-mcp-rules.md`](file:///Users/jorge/projects/mueble-aspiradora/.agents/rules/freecad-mcp-rules.md): Reglas técnicas de uso de `freecad-mcp`.
