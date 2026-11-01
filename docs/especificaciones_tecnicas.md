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
* **Especificaciones del fabricante ($L_{min} = S + 57,5\text{ mm}$, carrera $S = 110\text{ mm}$)**:
  * **Orificios de pasador (`2-Ø4.2`)**: distancia entre centros $L_c = \mathbf{215,0\text{ mm}}$ retraído y $L_o = \mathbf{325,0\text{ mm}}$ extendido.
  * **Lengüeta trasera**: ancho $9,9\text{ mm} \times$ espesor $7,9\text{ mm}$ (taladro $\varnothing 4,2\text{ mm}$).
  * **Cabeza delantera del vástago**: $\varnothing 9,0\text{ mm} \times$ espesor plano $6,1\text{ mm}$ (taladro $\varnothing 4,2\text{ mm}$).
  * **Carcasa reductora**: $37,5 \times 19,9 \times 15,0\text{ mm}$; ancho total con aletas laterales $= 39,9\text{ mm}$; 4 taladros en aletas `4-Ø5.0` separados **$11,0\text{ mm}$ longitudinalmente $\times 29,9\text{ mm}$ transversalmente** (no se atornillan rígidamente para permitir el giro del actuador de $-4,6^\circ$ a $+8,8^\circ$).
* **Pivote fijo trasero en costado ($A$)**: $A = (-225,7,\; 41,3\text{ mm})$ (a $252,3\text{ mm}$ del canto frontal).
* **Pivote móvil delantero en portón ($B$)**:
  * **Cerrado ($\theta = 0^\circ$)**: $B(0^\circ) = (-440,0,\; 24,0\text{ mm})$ $\implies L_c = \|B(0^\circ) - A\| = \mathbf{215,0\text{ mm}}$ ($\beta_c = -4,6^\circ$).
  * **Abierto ($\theta = 80^\circ$)**: $B(80^\circ) = (-546,9,\; 90,8\text{ mm})$ $\implies L_o = \|B(80^\circ) - A\| = \mathbf{325,0\text{ mm}}$ ($\beta_o = +8,8^\circ$).
  * **Carrera útil**: $325,0 - 215,0 = \mathbf{110,0\text{ mm}}$ ($100\%$ de aprovechamiento sin forzar topes).

---

## 3. Tablas Maestras de Distancias de Agujeros de Montaje

### 3.1. Unión entre Piezas de Madera (`[P01]`–`[P07]`)
1. **En Costados `[P01]` y `[P02]` ($478 \times 600 \times 15\text{ mm}$) — 5 taladros $\varnothing 4\text{ mm}$ avellanados por costado**:
   * **Hacia `[P03]` Cubierta Frontal Fija** (línea a **$7,5\text{ mm}$ del canto frontal**, paso **$130,0\text{ mm}$**):
     * `M_F1`: $Z = \mathbf{180,0\text{ mm}}$ | `M_F2`: $Z = \mathbf{310,0\text{ mm}}$ | `M_F3`: $Z = \mathbf{440,0\text{ mm}}$ | `M_F4`: $Z = \mathbf{570,0\text{ mm}}$ (coinciden a $33, 163, 293\text{ y } 423\text{ mm}$ desde la base de `[P03]`).
   * **Hacia `[P05]` Nervio Trasero Superior** (a **$7,5\text{ mm}$ del canto trasero** = $470,5\text{ mm}$ del frente):
     * `M_N1`: $Z = \mathbf{582,5\text{ mm}}$ desde el suelo (a $17,5\text{ mm}$ del canto superior, centro exacto del nervio de $35\text{ mm}$).
2. **En Lámina Superior Base `[P06]` ($540 \times 478 \times 10\text{ mm}$) — 10 taladros $\varnothing 4\text{ mm}$ avellanados**:
   * **Hacia Costados `[P01]` y `[P02]`** (a **$7,5\text{ mm}$ de los bordes laterales**, $X = 7,5$ y $532,5\text{ mm}$): **3 taladros por lado** en $Y_{frente} = \mathbf{60,0\text{ mm}}$, $\mathbf{239,0\text{ mm}}$ y $\mathbf{418,0\text{ mm}}$ (**separación = $179,0\text{ mm}$**).
   * **Hacia `[P03]` (a $7,5\text{ mm}$ del frente) y `[P05]` (a $7,5\text{ mm}$ de la trasera)**: **2 taladros delanteros + 2 traseros** en $X = \mathbf{170,0\text{ mm}}$ y $X = \mathbf{370,0\text{ mm}}$ (**separación = $200,0\text{ mm}$**, equivalentes a $155,0\text{ mm}$ y $355,0\text{ mm}$ en coordenadas locales de `[P03]`/`[P05]`).

### 3.2. Bisagras Garosa $135 \times 40 \times 35\text{ mm}$ ($80^\circ$ Sin Muelles, SKU `B0BX5QCP6J`) — Tornillos $\varnothing 4 \times 12\text{ mm}$
1. **`Placa_Costado` ($100 \times 36\text{ mm}$, base en $Z_0 = 2,0\text{ mm}$, paso Euro $32,0\text{ mm}$) en cara interior de `[P01]` y `[P02]`**:
   * **`H_C1` (Superior, $\varnothing 6,0\text{ mm}$)**: a **$41,0\text{ mm}$ del canto frontal** y **$Z = 98,0\text{ mm}$** del suelo.
   * **`H_C2` (Medio-Alto, $\varnothing 4,5\text{ mm}$)**: a **$38,0\text{ mm}$ del canto frontal** y **$Z = 66,0\text{ mm}$** del suelo (**separación vertical = $32,0\text{ mm}$**).
   * **`H_C3` (Medio-Bajo, $\varnothing 6,0\text{ mm}$)**: a **$35,0\text{ mm}$ del canto frontal** y **$Z = 34,0\text{ mm}$** del suelo (**separación vertical = $32,0\text{ mm}$**).
   * **`H_C4` (Inferior, $\varnothing 4,5\text{ mm}$)**: a **$25,0\text{ mm}$ del canto frontal** y **$Z = 6,5\text{ mm}$** del suelo (**separación vertical = $27,5\text{ mm}$**).
2. **`Escuadra_Puerta` ($62,5 \times 14\text{ mm}$, paso Euro $16,0\text{ mm}$) en cara interior de `[P04]` ($506 \times 143\text{ mm}$)**:
   * **`T_P1` (Ranura superior)**: a **$8,0\text{ mm}$ del borde lateral** ($X_{local} = 8,0 / 498,0\text{ mm}$) y **$Z_{local} = 112,0\text{ mm}$** de la base del portón.
   * **`T_P2` (Taladro circular central, $\varnothing 4,5\text{ mm}$)**: a **$5,0\text{ mm}$ del borde lateral** ($X_{local} = 5,0 / 501,0\text{ mm}$) y **$Z_{local} = 96,0\text{ mm}$** de la base (**separación = $16,0\text{ mm}$**).
   * **`T_P3` (Ranura inferior)**: a **$8,0\text{ mm}$ del borde lateral** ($X_{local} = 8,0 / 498,0\text{ mm}$) y **$Z_{local} = 80,0\text{ mm}$** de la base (**separación = $16,0\text{ mm}$ respecto a `T_P2` y $32,0\text{ mm}$ respecto a `T_P1`**).

### 3.3. Soportes `[H03]` de los Actuadores Lineales Dawnso Mini 150N — Tornillos $\varnothing 4 \times 12\text{ mm}$
1. **Soporte Trasero Fijo `A` en Costados `[P01]` y `[P02]`** (eje pasador M4 en $252,3\text{ mm}$ del frente y $Z_A = 41,3\text{ mm}$):
   * **`A_S1` (Superior)**: a **$252,3\text{ mm}$ del canto frontal** y **$Z = 54,3\text{ mm}$** del suelo.
   * **`A_S2` (Inferior)**: a **$252,3\text{ mm}$ del canto frontal** y **$Z = 28,3\text{ mm}$** del suelo (**separación entre agujeros = $26,0\text{ mm}$**).
2. **Soporte Delantero Móvil `B` en cara interior del Portón `[P04]`** (eje pasador M4 a $20,0\text{ mm}$ del borde lateral y $Z_{local} = 22,0\text{ mm}$):
   * **`B_S1` (Superior)**: a **$20,0\text{ mm}$ del borde lateral** ($X_{local} = 20,0 / 486,0\text{ mm}$) y **$Z_{local} = 32,0\text{ mm}$** de la base del portón.
   * **`B_S2` (Inferior)**: a **$20,0\text{ mm}$ del borde lateral** ($X_{local} = 20,0 / 486,0\text{ mm}$) y **$Z_{local} = 12,0\text{ mm}$** de la base del portón (**separación entre agujeros = $20,0\text{ mm}$**).

---

## 4. Planos de Corte y Mecanizado Incluidos en `planos/`

1. [`planos/Planos_Corte_Madera_Diseño_Final_A4.pdf`](../planos/Planos_Corte_Madera_Diseño_Final_A4.pdf): Dossier de 2 hojas ISO A4 para taller.
2. [`planos/Plano_Corte_01_Mapas_Tableros_A4.pdf`](../planos/Plano_Corte_01_Mapas_Tableros_A4.pdf) / [`.png`](../planos/Plano_Corte_01_Mapas_Tableros_A4.png): Mapas de corte sobre los tableros de $1200 \times 600\text{ mm}$.
3. [`planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.pdf`](../planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.pdf) / [`.png`](../planos/Plano_Corte_02_Despiece_Acotado_Piezas_A4.png): Despiece individual acotado y plantilla de taladros.
4. [`planos/Planos_Mueble_Aspiradora_Completo_A4.pdf`](../planos/Planos_Mueble_Aspiradora_Completo_A4.pdf): Dossier completo de 6 hojas ISO A4.
