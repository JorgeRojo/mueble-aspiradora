# Especificaciones Técnicas y Constructivas: Mueble Aspiradora Cota Cero ($540 \times 478 \times 620\text{ mm}$)

Documento técnico definitivo del módulo cubre-base para estación **Dreame L10s / X40** a **Cota Cero**, fabricado con **7 piezas de madera** (2 tableros de $1200 \times 600 \times 15\text{ mm}$ y 1 tablero de $1200 \times 600 \times 10\text{ mm}$), **bisagras articuladas Garosa $135 \times 40 \times 35\text{ mm}$ ($80^\circ$) sin muelles** y **2 actuadores lineales Dawnso Mini 150N ($215/325\text{ mm}$, carrera $110\text{ mm}$)**.

---

## 1. Cuadro General de Dimensiones

| Parámetro | Cota Exacta | Detalle Constructivo |
| :--- | :---: | :--- |
| **Ancho exterior total** | **$540\text{ mm}$** | $15\text{ mm}$ (`[P01]`) $+ 510\text{ mm}$ (vano interior) $+ 15\text{ mm}$ (`[P02]`). |
| **Fondo exterior total** | **$478\text{ mm}$** | Medida exacta desde la pared hasta el frente exterior enrasado ($Y \in [-478, 0]\text{ mm}$). |
| **Altura exterior total** | **$620\text{ mm}$** | $600\text{ mm}$ (costados `[P01]`/`[P02]` directos del ancho del tablero) $+ 20\text{ mm}$ (tapa doble `[P06]`+`[P07]`). |
| **Hueco libre interior** | **$510 \times 463 \times 600\text{ mm}$** | Base Dreame ($423\text{ mm}$ ancho $\times 568\text{ mm}$ alto) alojada con $43,5\text{ mm}$ libres por lado y $32\text{ mm}$ libres arriba. |
| **Cubierta frontal fija `[P03]`** | **$510 \times 453 \times 15\text{ mm}$** | Embutida entre costados desde $Z = 147\text{ mm}$ hasta $Z = 600\text{ mm}$ ($Y \in [-478, -463]\text{ mm}$). |
| **Portón inferior abatible `[P04]`** | **$506 \times 143 \times 15\text{ mm}$** | $Z \in [2, 145]\text{ mm}$, holgura perimetral de $2\text{ mm}$ y arco central LiDAR ($244 \times 22\text{ mm}, R=178\text{ mm}$). |
| **Nervio trasero superior `[P05]`** | **$510 \times 35 \times 15\text{ mm}$** | Montado en $Z \in [565, 600]\text{ mm}, Y \in [-15, 0]\text{ mm}$, pegado bajo la tapa superior `[P06]`. |
| **Tapa superior doble `[P06]`+`[P07]`**| **$540 \times 478 \times 20\text{ mm}$** | 2 láminas superpuestas de $10\text{ mm}$ que cubren el $100\%$ de la planta superior ($Z \in [600, 620]\text{ mm}$). |

---

## 2. Cinemática del Cuadrilátero Articulado (Bisagra Garosa $80^\circ$ Sin Muelles + Actuador Dawnso)

### 2.1. Puntos del Mecanismo de 4 Barras (Coordenadas $(Y, Z)$ en $\text{mm}$)
* **Pivote fijo superior en costado ($O_1$)**: $(-451,0,\; 124,0\text{ mm})$ (a $27,0\text{ mm}$ del frente exterior).
* **Pivote fijo inferior en costado ($O_2$)**: $(-431,0,\; 80,0\text{ mm})$ (a $47,0\text{ mm}$ del frente exterior).
* **Articulaciones en pletina móvil del portón ($\theta = 0^\circ$ cerrado)**:
  * $P_1(0^\circ) = (-461,0,\; 84,0\text{ mm})$ $\implies$ Eslabón superior $L_1 = \|P_1 - O_1\| = \mathbf{58,21\text{ mm}}$ ($\alpha_{1c} = -104,0^\circ$).
  * $P_2(0^\circ) = (-461,0,\; 40,0\text{ mm})$ $\implies$ Eslabón inferior $L_2 = \|P_2 - O_2\| = \mathbf{48,88\text{ mm}}$ ($\alpha_{2c} = -127,9^\circ$).
  * Distancia rígida en puerta: $d_P = \|P_1 - P_2\| = \mathbf{44,00\text{ mm}}$.
* **Posición abierta a $\theta = 80^\circ$ (intersección exacta de circunferencias)**:
  * El portón se inclina $80^\circ$ hacia delante y arriba (vector unitario a lo largo de la puerta $u = (-0,9848,\; +0,1736)$):
  * $P_1(80^\circ) = (-509,1,\; 120,0\text{ mm})$ ($\alpha_{1o} = -176,1^\circ$, giro de eslabón $\Delta\alpha_1 = 72,1^\circ$).
  * $P_2(80^\circ) = (-465,8,\; 112,4\text{ mm})$ ($\alpha_{2o} = -137,0^\circ$, giro de eslabón $\Delta\alpha_2 = 9,1^\circ$).
  * El borde inferior del portón asciende hasta **$Z = 109,5\text{ mm}$** ($Y = -584,4\text{ mm}$), dejando paso libre total al robot Dreame ($96,5\text{ mm}$ de chasis y $103,8\text{ mm}$ de torreta LiDAR).

### 2.2. Actuadores Lineales Dawnso Mini 150N ($215\text{ mm} \to 325\text{ mm}$)
* **Pivote fijo trasero en costado ($A$)**: $A = (-225,7,\; 41,3\text{ mm})$ (a $252,3\text{ mm}$ del canto frontal).
* **Pivote móvil delantero en portón ($B$)**:
  * **Cerrado ($\theta = 0^\circ$)**: $B(0^\circ) = (-440,0,\; 24,0\text{ mm})$ $\implies L_c = \|B(0^\circ) - A\| = \mathbf{215,0\text{ mm}}$ ($\beta_c = -4,6^\circ$).
  * **Abierto ($\theta = 80^\circ$)**: $B(80^\circ) = (-546,9,\; 90,8\text{ mm})$ $\implies L_o = \|B(80^\circ) - A\| = \mathbf{325,0\text{ mm}}$ ($\beta_o = +8,8^\circ$).
  * **Carrera útil**: $325,0 - 215,0 = \mathbf{110,0\text{ mm}}$ ($100\%$ de aprovechamiento sin forzar topes).

---

## 3. Planos de Corte y Mecanizado Incluidos en `planos/`

1. [`planos/Planos_Corte_Madera_Diseño_Final_A4.pdf`](../planos/Planos_Corte_Madera_Diseño_Final_A4.pdf): Dossier de 2 hojas ISO A4 para taller.
2. [`planos/Plano_Corte_01_Mapas_Tableros_A4.pdf`](../planos/Plano_Corte_01_Mapas_Tableros_A4.pdf) / [`.png`](../planos/Plano_Corte_01_Mapas_Tableros_A4.png): Mapas de corte sobre los tableros de $1200 \times 600\text{ mm}$.
3. [`planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.pdf`](../planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.pdf) / [`.png`](../planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.png): Despiece individual acotado y plantilla de taladros.
4. [`planos/Planos_Mueble_Aspiradora_Completo_A4.pdf`](../planos/Planos_Mueble_Aspiradora_Completo_A4.pdf): Dossier completo de 6 hojas ISO A4.
