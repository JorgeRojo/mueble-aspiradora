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

## 3. Cinemática del Portón Abatible ($80^\circ$), Distancias de Agujeros de Montaje y Automatización

### 3.1. Unión entre Piezas de Madera (`[P01]`–`[P07]`, tornillos $\varnothing 4 \times 40\text{ mm}$ y $\varnothing 4 \times 30\text{ mm}$)
* **En Costados `[P01]` y `[P02]` ($478 \times 600 \times 15\text{ mm}$) — 5 taladros pasantes $\varnothing 4\text{ mm}$ avellanados por costado**:
  * **Unión frontal con `[P03]` Cubierta Superior Fija** (línea vertical a **$7,5\text{ mm}$ del canto frontal**, $Y = -470,5\text{ mm}$, **paso de $130,0\text{ mm}$**):
    * `M_F1`: $Z = 180,0\text{ mm}$ | `M_F2`: $Z = 310,0\text{ mm}$ | `M_F3`: $Z = 440,0\text{ mm}$ | `M_F4`: $Z = 570,0\text{ mm}$ (coinciden con 4 taladros guía $\varnothing 3\text{ mm}$ en los cantos laterales de `[P03]` a $33, 163, 293\text{ y } 423\text{ mm}$ desde la base de `[P03]`).
  * **Unión trasera con `[P05]` Nervio Trasero Superior** (a **$7,5\text{ mm}$ del canto trasero** = $470,5\text{ mm}$ del frente):
    * `M_N1`: $Z = 582,5\text{ mm}$ desde el suelo (a $17,5\text{ mm}$ del borde superior de $600\text{ mm}$, centro del nervio `[P05]` de $35\text{ mm}$).
* **En Lámina Superior Base `[P06]` ($540 \times 478 \times 10\text{ mm}$, $Z \in [600, 610]\text{ mm}$) — 10 taladros $\varnothing 4\text{ mm}$ avellanados (ocultos bajo `[P07]`)**:
  * **Laterales hacia `[P01]` y `[P02]`** (a **$7,5\text{ mm}$ de los bordes izquierdo y derecho**, $X = 7,5\text{ mm}$ y $X = 532,5\text{ mm}$): **3 taladros por lado** a $Y_{frente} = 60,0\text{ mm}$, $239,0\text{ mm}$ y $418,0\text{ mm}$ (**separación entre agujeros = $179,0\text{ mm}$**).
  * **Frente hacia `[P03]`** (a **$7,5\text{ mm}$ del borde frontal**) y **Trasera hacia `[P05]`** (a **$7,5\text{ mm}$ del borde trasero** = $470,5\text{ mm}$ del frente): **2 taladros delanteros + 2 traseros** en $X = 170,0\text{ mm}$ y $X = 370,0\text{ mm}$ (**separación entre agujeros = $200,0\text{ mm}$**, equivalentes a $155,0\text{ mm}$ y $355,0\text{ mm}$ desde el extremo izquierdo de `[P03]` y `[P05]`).

### 3.2. Bisagras Garosa $135 \times 40 \times 35\text{ mm}$ ($80^\circ$ SIN muelles helicoidales, SKU `B0BX5QCP6J`) — Tornillos $\varnothing 4 \times 12\text{ mm}$
* **Cinemática de los remaches articulados internos de fábrica**:
  * Pivotes en costado: $O_1 = (-451,0,\; 124,0\text{ mm})$ (a $27\text{ mm}$ del frente) y $O_2 = (-431,0,\; 80,0\text{ mm})$ (a $47\text{ mm}$ del frente).
  * Eslabones: $L_1 = 58,21\text{ mm}$, $L_2 = 48,88\text{ mm}$, separación en puerta $d_P = 44,00\text{ mm}$ ($P_1$ a $82\text{ mm}$ y $P_2$ a $38\text{ mm}$ de la base del portón).
* **Taladros de montaje de `Placa_Costado` ($100 \times 36\text{ mm}$) en cara interior de `[P01]` y `[P02]` (base en $Z_0 = 2,0\text{ mm}$, paso Euro $32,0\text{ mm}$)**:
  * `H_C1` (Sup., $\varnothing 6,0\text{ mm}$): a **$41,0\text{ mm}$ del frente** y **$Z = 98,0\text{ mm}$** del suelo ($v = 96,0\text{ mm}$).
  * `H_C2` (Med-Alto, $\varnothing 4,5\text{ mm}$): a **$38,0\text{ mm}$ del frente** y **$Z = 66,0\text{ mm}$** del suelo (**separación vertical = $32,0\text{ mm}$**).
  * `H_C3` (Med-Bajo, $\varnothing 6,0\text{ mm}$): a **$35,0\text{ mm}$ del frente** y **$Z = 34,0\text{ mm}$** del suelo (**separación vertical = $32,0\text{ mm}$**).
  * `H_C4` (Inf., $\varnothing 4,5\text{ mm}$): a **$25,0\text{ mm}$ del frente** y **$Z = 6,5\text{ mm}$** del suelo (a $27,5\text{ mm}$ bajo `H_C3`).
* **Taladros de montaje de `Escuadra_Puerta` ($62,5 \times 14\text{ mm}$) en cara interior del Portón `[P04]` ($506 \times 143\text{ mm}$, paso Euro $16,0\text{ mm}$)**:
  * `T_P1` (Ranura superior): a **$8,0\text{ mm}$ del borde lateral** ($X_{local} = 8,0 / 498,0\text{ mm}$) y **$Z_{local} = 112,0\text{ mm}$** de la base del portón ($31,0\text{ mm}$ del borde superior).
  * `T_P2` (Taladro circular central, $\varnothing 4,5\text{ mm}$): a **$5,0\text{ mm}$ del borde lateral** ($X_{local} = 5,0 / 501,0\text{ mm}$) y **$Z_{local} = 96,0\text{ mm}$** de la base (**separación = $16,0\text{ mm}$**).
  * `T_P3` (Ranura inferior): a **$8,0\text{ mm}$ del borde lateral** ($X_{local} = 8,0 / 498,0\text{ mm}$) y **$Z_{local} = 80,0\text{ mm}$** de la base (**separación = $16,0\text{ mm}$ respecto a `T_P2` y $32,0\text{ mm}$ respecto a `T_P1`**).

### 3.3. Actuadores Lineales Dawnso Mini 150N 12V DC ($215/325\text{ mm}$, carrera $110\text{ mm}$) y Soportes `[H03]`
* **Cotas oficiales del fabricante del actuador ($L_{min} = S + 57,5\text{ mm}$)**:
  * Distancia entre centros de los **2 orificios de pasador $\varnothing 4,2\text{ mm}$ (`2-Ø4.2`)**: **$215,0\text{ mm}$** cerrado ($\beta_c = -4,6^\circ$) $\to$ **$325,0\text{ mm}$** abierto a $80^\circ$ ($\beta_o = +8,8^\circ$).
  * Lengüeta trasera: ancho **$9,9\text{ mm}$** $\times$ espesor **$7,9\text{ mm}$**; cabeza delantera del vástago: **$\varnothing 9,0\text{ mm}$** $\times$ espesor plano **$6,1\text{ mm}$**.
  * Carcasa reductora: **$37,5 \times 19,9 \times 15,0\text{ mm}$** (ancho con aletas $= 39,9\text{ mm}$; 4 taladros en aletas `4-Ø5.0` separados **$11,0 \times 29,9\text{ mm}$** — libres para permitir el giro del actuador).
* **Soporte Trasero Fijo `A` en Costados `[P01]` y `[P02]` (tornillos $\varnothing 4 \times 12\text{ mm}$)**:
  * **Eje del pasador M4 (`A`, $\varnothing 4,2\text{ mm}$)**: a **$252,3\text{ mm}$ del canto frontal** ($225,7\text{ mm}$ del canto trasero, $Y = -225,7\text{ mm}$) y **$Z_A = 41,3\text{ mm}$** del suelo (a $22,0\text{ mm}$ de la cara interior del costado).
  * **2 taladros en madera (`A_S1` y `A_S2`)**: a **$252,3\text{ mm}$ del frente**, en **$Z = 54,3\text{ mm}$** y **$Z = 28,3\text{ mm}$** (**separación entre agujeros = $26,0\text{ mm}$**, $\pm 13,0\text{ mm}$ respecto al eje $A$).
* **Soporte Delantero Móvil `B` en cara interior del Portón `[P04]` (tornillos $\varnothing 4 \times 12\text{ mm}$)**:
  * **Eje del pasador M4 (`B`, $\varnothing 4,2\text{ mm}$)**: a **$20,0\text{ mm}$ del borde lateral** ($X_{local} = 20,0 / 486,0\text{ mm}$), en **$Z_{local} = 22,0\text{ mm}$** de la base del portón ($Z_{global} = 24,0\text{ mm}$, proyectado $23,0\text{ mm}$ hacia el interior: $B(0^\circ) = (-440,0,\; 24,0\text{ mm}) \to B(80^\circ) = (-546,9,\; 90,8\text{ mm})$).
  * **2 taladros en madera (`B_S1` y `B_S2`)**: a **$20,0\text{ mm}$ del borde lateral**, en **$Z_{local} = 32,0\text{ mm}$** y **$Z_{local} = 12,0\text{ mm}$** de la base del portón (**separación entre agujeros = $20,0\text{ mm}$**, $\pm 10,0\text{ mm}$ respecto al eje $B$).
* **Control Zigbee**: Relé MHCOZY de 2 canales con contactos secos en modo **Interlock** e inversión de polaridad (puente en H) alimentado a 12V DC.

---

## 4. Archivos Maestros en Producción

* [`Mueble_Aspiradora_Cota_Cero.FCStd`](file:///Users/jorge/projects/mueble-aspiradora/Mueble_Aspiradora_Cota_Cero.FCStd): Modelo CAD 3D cerrado + 6 hojas TechDraw ISO A4.
* [`Modulo_01_Porton_Abierto_80deg.FCStd`](file:///Users/jorge/projects/mueble-aspiradora/Modulo_01_Porton_Abierto_80deg.FCStd): Modelo CAD 3D con portón abierto a $80^\circ$.
* [`Mecanismo_Metalico_Bisagras_y_Actuadores.FCStd`](file:///Users/jorge/projects/mueble-aspiradora/Mecanismo_Metalico_Bisagras_y_Actuadores.FCStd) y [`planos/Mecanismo_Metalico_Bisagras_y_Actuadores.step`](file:///Users/jorge/projects/mueble-aspiradora/planos/Mecanismo_Metalico_Bisagras_y_Actuadores.step): Modelo CAD 3D de herrajes y actuadores.
* [`planos/Planos_Corte_Madera_Diseño_Final_A4.pdf`](file:///Users/jorge/projects/mueble-aspiradora/planos/Planos_Corte_Madera_Diseño_Final_A4.pdf): Dossier de 2 hojas A4 de corte y despiece de madera.
* [`planos/Planos_Mueble_Aspiradora_Completo_A4.pdf`](file:///Users/jorge/projects/mueble-aspiradora/planos/Planos_Mueble_Aspiradora_Completo_A4.pdf): Dossier maestro completo de 6 hojas A4.
* [`.agents/rules/freecad-mcp-rules.md`](file:///Users/jorge/projects/mueble-aspiradora/.agents/rules/freecad-mcp-rules.md): Reglas técnicas de uso de `freecad-mcp`.
