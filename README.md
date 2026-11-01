# Mueble Automatizado a Cota Cero para Robot Aspirador Dreame (Diseño Final: $540 \times 478 \times 620\text{ mm}$)

Módulo cubre-base a medida diseñado para ocultar la estación de autovaciado y robot aspirador **Dreame (L10s / X40)** a **Cota Cero**, con **portón inferior abatible frontal de $80^\circ$** mediante **bisagras articuladas Garosa $135 \times 40 \times 35\text{ mm}$ (sin muelles)** accionado por **2 actuadores lineales Dawnso Mini 150N ($215/325\text{ mm}$, carrera $110\text{ mm}$)** y control nativo por **Zigbee (Home Assistant)**.

| Vista 3D Cerrado ($540 \times 478 \times 620\text{ mm}$) | Vista 3D Portón Abierto a $80^\circ$ | Cinemática Lateral Exacta ($80^\circ$) |
| :---: | :---: | :---: |
| ![Mueble Cerrado](planos/Vista_3D_Mueble_Final_Cerrado.png) | ![Portón Abierto 80°](planos/Vista_3D_Porton_Abierto_80deg.png) | ![Cinemática Abierto Acotado](planos/Vista_3D_Perfil_Mecanismo_Abierto_Acotado.png) |

---

## 1. Modelos 3D CAD en FreeCAD y Planos Técnicos ISO A4

### 1.1. Modelos 3D Maestros (`.FCStd` y `.step`)
* [`Mueble_Aspiradora_Cota_Cero.FCStd`](Mueble_Aspiradora_Cota_Cero.FCStd): Modelo CAD 3D maestro en estado cerrado ($\theta = 0^\circ$) con las 6 hojas técnicas ISO A4 integradas en TechDraw.
* [`Modulo_01_Porton_Abierto_80deg.FCStd`](Modulo_01_Porton_Abierto_80deg.FCStd): Modelo CAD 3D con el portón abierto a $\theta = 80^\circ$ y los actuadores extendidos a $325,0\text{ mm}$ ($\beta_o = +8,8^\circ$).
* [`Mecanismo_Metalico_Bisagras_y_Actuadores.FCStd`](Mecanismo_Metalico_Bisagras_y_Actuadores.FCStd) y [`planos/Mecanismo_Metalico_Bisagras_y_Actuadores.step`](planos/Mecanismo_Metalico_Bisagras_y_Actuadores.step): Modelo 3D aislado exclusivamente con los herrajes metálicos (bisagras Garosa sin muelles + escuadras) y los 2 actuadores lineales.

### 1.2. Dossiers de Planos ISO A4 Listos para Impresión
* **Dossier de Corte y Mecanizado de Madera (2 Hojas A4)**: [`planos/Planos_Corte_Madera_Diseño_Final_A4.pdf`](planos/Planos_Corte_Madera_Diseño_Final_A4.pdf)
* **Dossier Maestro Completo del Proyecto (6 Hojas A4)**: [`planos/Planos_Mueble_Aspiradora_Completo_A4.pdf`](planos/Planos_Mueble_Aspiradora_Completo_A4.pdf)

| Hoja | Vista Previa / Archivos | Contenido |
| :--- | :--- | :--- |
| **Corte 1/2** | [`Plano_Corte_01_Mapas_Tableros_A4.pdf`](planos/Plano_Corte_01_Mapas_Tableros_A4.pdf) · [`.png`](planos/Plano_Corte_01_Mapas_Tableros_A4.png) | Mapas de corte a escala sobre **2 tableros de $1200 \times 600 \times 15\text{ mm}$** y **1 tablero de $1200 \times 600 \times 10\text{ mm}$** + secuencia de 8 cortes rectos. |
| **Corte 2/2** | [`Plano_Corte_02_Despiece_Acotado_Piezas_A4.pdf`](planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.pdf) · [`.png`](planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.png) | Despiece acotado individual de las **7 piezas (`[P01]`–`[P07]`)**, arco LiDAR ($244 \times 22\text{ mm}, R=178\text{ mm}$) y **plantilla milimétrica de taladros**. |
| **Plano 01** | [`Plano_01_Alzado_y_Planta_A4.pdf`](planos/Plano_01_Alzado_y_Planta_A4.pdf) · [`.svg`](planos/Plano_01_Alzado_y_Planta_A4.svg) | Alzado frontal y planta superior acotados. |
| **Plano 02** | [`Plano_02_Perfil_e_Isometrica_A4.pdf`](planos/Plano_02_Perfil_e_Isometrica_A4.pdf) · [`.svg`](planos/Plano_02_Perfil_e_Isometrica_A4.svg) | Sección lateral y vista isométrica general. |
| **Plano 03** | [`Plano_03_Despiece_Carpinteria_A4.pdf`](planos/Plano_03_Despiece_Carpinteria_A4.pdf) · [`.svg`](planos/Plano_03_Despiece_Carpinteria_A4.svg) | Vistas de carpintería y lista de materiales (BOM). |
| **Plano 04** | [`Plano_04_Puerta_Vertical_y_Actuadores_A4.pdf`](planos/Plano_04_Puerta_Vertical_y_Actuadores_A4.pdf) · [`.svg`](planos/Plano_04_Puerta_Vertical_y_Actuadores_A4.svg) | Cinemática de las bisagras Garosa $80^\circ$ sin muelles y actuadores Dawnso Mini 150N. |

| Hoja 1 de Corte: Mapas de Tableros | Hoja 2 de Corte: Despiece Acotado y Taladros |
| :---: | :---: |
| ![Hoja 1 Mapas de Corte](planos/Plano_Corte_01_Mapas_Tableros_A4.png) | ![Hoja 2 Despiece Acotado](planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.png) |

---

## 2. Dimensiones Generales y Despiece de Madera (7 Piezas)

* **Dimensiones Exteriores Totales**: **$540\text{ mm}$ (Ancho) $\times 478\text{ mm}$ (Fondo exacto desde pared) $\times 620\text{ mm}$ (Alto: $600\text{ mm}$ costados $+ 20\text{ mm}$ tapa superior doble)**.
* **Hueco Interior Libre**: **$510\text{ mm}$ (Ancho) $\times 463\text{ mm}$ (Fondo útil tras frente de $15\text{ mm}$) $\times 600\text{ mm}$ (Alto bajo tapa)**.

| Cód. | Pieza | Dimensiones ($\text{mm}$) | Tablero ($1200 \times 600$) | Corte y Mecanizado |
| :--- | :--- | :---: | :--- | :--- |
| **`[P01]`** | Costado Izquierdo | **$478 \times 600 \times 15$** | Tablero #1 ($15\text{ mm}$) | **1 corte transversal recto** a $478\text{ mm}$ ($600\text{ mm}$ directo del ancho del tablero, sin cajeados) |
| **`[P02]`** | Costado Derecho | **$478 \times 600 \times 15$** | Tablero #1 ($15\text{ mm}$) | **1 corte transversal recto** a $478\text{ mm}$ ($600\text{ mm}$ directo del ancho del tablero, sin cajeados) |
| **`[P03]`** | Cubierta Frontal Fija | **$510 \times 453 \times 15$** | Tablero #2 ($15\text{ mm}$) | Corte recto puro ($Z \in [147, 600]\text{ mm}$, embutida entre costados) |
| **`[P04]`** | Portón Abatible $80^\circ$ | **$506 \times 143 \times 15$** | Tablero #2 ($15\text{ mm}$) | $Z \in [2, 145]\text{ mm}$ ($2\text{ mm}$/lado holgura) + arco central LiDAR ($244 \times 22\text{ mm}, R=178\text{ mm}$) |
| **`[P05]`** | Nervio Trasero Superior | **$510 \times 35 \times 15$** | Tablero #2 ($15\text{ mm}$) | Corte recto puro ($Z \in [565, 600]\text{ mm}, Y \in [-15, 0]\text{ mm}$, pegado bajo la tapa superior) |
| **`[P06]`** | Lámina Superior Base | **$540 \times 478 \times 10$** | Tablero #1 ($10\text{ mm}$) | Corte recto puro; cubre el $100\%$ de la superficie superior ($Z \in [600, 610]\text{ mm}$) |
| **`[P07]`** | Lámina Superior Tapa | **$540 \times 478 \times 10$** | Tablero #1 ($10\text{ mm}$) | Corte recto puro; encolada sobre `[P06]` formando tapa rígida de $20\text{ mm}$ ($Z \in [610, 620]\text{ mm}$) |

---

## 3. Cinemática Exacta y Coordenadas de Taladrado de Herrajes

### 3.1. En Cara Interior de Costados `[P01]` y `[P02]` (medidas desde el Canto Frontal $Y=-478\text{ mm}$ y Suelo $Z=0$)
* **Bisagra Garosa $135 \times 40 \times 35\text{ mm}$ ($80^\circ$, sin muelle helicoidal)**:
  * **Eje superior fijo ($O_1$)**: a **$27,0\text{ mm}$ del canto frontal** ($Y = -451,0\text{ mm}$) y **$Z = 124,0\text{ mm}$** del suelo.
  * **Eje inferior fijo ($O_2$)**: a **$47,0\text{ mm}$ del canto frontal** ($Y = -431,0\text{ mm}$) y **$Z = 80,0\text{ mm}$** del suelo.
* **Soporte Trasero Actuador Dawnso Mini 150N (Pivote Fijo $A$)**:
  * **Centro del pasador ($A$)**: a **$252,3\text{ mm}$ del canto frontal** ($225,7\text{ mm}$ del canto trasero) y **$Z = 41,3\text{ mm}$** del suelo.

### 3.2. En Cara Interior del Portón `[P04]` (medidas desde el Borde Inferior del Portón $Z_p = 0$)
* **Pletina Móvil de Bisagra Garosa** (a $13,0\text{ mm}$ de cada borde lateral):
  * **Articulación superior ($P_1$)**: a **$82,0\text{ mm}$ de la base del portón** ($Z = 84,0\text{ mm}$ absolutos).
  * **Articulación inferior ($P_2$)**: a **$38,0\text{ mm}$ de la base del portón** ($Z = 40,0\text{ mm}$ absolutos).
* **Escuadra Delantera del Actuador (Pivote Móvil $B$)**:
  * A $18,0\text{ mm}$ de cada borde lateral; eje $B$ a **$22,0\text{ mm}$ de la base del portón** ($Z = 24,0\text{ mm}$ absolutos, sobresaliendo $23,0\text{ mm}$ hacia el interior del mueble).

### 3.3. Recorrido y Ángulos Verificados
* **Cerrado ($\theta = 0^\circ$)**: $B(0^\circ) = (-440,0,\; 24,0\text{ mm}) \implies \|B - A\| = \mathbf{215,0\text{ mm}}$ ($\beta_c = -4,6^\circ$).
* **Abierto ($\theta = 80^\circ$)**: $B(80^\circ) = (-546,9,\; 90,8\text{ mm}) \implies \|B - A\| = \mathbf{325,0\text{ mm}}$ ($\beta_o = +8,8^\circ$, carrera útil completa $= 110,0\text{ mm}$, altura libre de paso $= 109,5\text{ mm}$).
