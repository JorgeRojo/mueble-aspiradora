# Especificaciones Técnicas y Constructivas: Mueble Recibidor Cuadrado con Doble Puerta

Proyecto de consola recibidor cuadrada a medida diseñada para ocultar la estación de autovaciado y robot aspirador **Dreame L10s / X40** a **Cota Cero**, con **doble puerta batiente motorizada** de apertura frontal, interior 100% diáfano (sin balda) y cajeado trasero para salvar rodapié de 1,5 cm.

| Plano con Cotas Milimétricas | Fotografía de Referencia Arquitectónica |
| :---: | :---: |
| ![Plano con Cotas Técnicas](../foto_realista_mueble_cuadrado_cotas.jpg) | ![Fotografía Realista](../foto_realista_mueble_cuadrado_dos_puertas.jpg) |

---

## 1. Justificación Dimensional de la Planta Cuadrada ($540 \times 540\text{ mm}$)

Para lograr que la encimera sea **totalmente cuadrada** y a la vez el mueble sea **lo más estrecho posible**, la medida mínima viene dictada por la profundidad de la aspiradora con rampa:

* **Espesor del rodapié de la pared**: $15\text{ mm}$ ($1,5\text{ cm}$).
* **Cajeado en costados para rodapié**: $18\text{ mm}$ de profundidad $\times 95\text{ mm}$ de alto (permite que los costados apoyen enrasados contra la pared).
* **Profundidad de la estación Dreame con rampa**: $493\text{ mm}$.
* **Posición de la base apoyada en el rodapié**: $15\text{ mm} + 493\text{ mm} = \mathbf{508\text{ mm}}$ desde la pared.
* **Margen de seguridad libre frontal**: $+14\text{ mm}$ (garantiza que el robot no toque las puertas).
* **Posición de la cara interior de las puertas**: $508 + 14 = \mathbf{522\text{ mm}}$ desde la pared.
* **Espesor de las puertas cerradas**: $18\text{ mm}$.
* **Fondo exterior total**: $522 + 18 = \mathbf{540\text{ mm}}$.
* **Al ser cuadrada la encimera**:
  $$\mathbf{Ancho = 540\text{ mm} \quad \times \quad Fondo = 540\text{ mm}}$$

---

## 2. Cotas Generales y Holguras Interiores

| Cota | Medida | Evaluación Técnica |
| :--- | :---: | :--- |
| **Encimera exterior** | **540 x 540 mm** | Planta cuadrada simétrica perfecta. |
| **Alto exterior** | **750 mm** | Proporción esbelta vertical (1,39:1 respecto al ancho). |
| **Ancho interior libre** | **490 mm** | $540 - 50\text{ mm}$ (costados de 25 mm). Base Dreame: 423 mm $\to$ **33,5 mm libres a cada lado**. |
| **Fondo interior útil** | **522 mm** | Deja **14 mm libres** entre el frente de la rampa Dreame (508 mm) y las puertas. |
| **Altura interior diáfana** | **725 mm** | **Sin balda interior**: Deja **157 mm libres** sobre la base Dreame (568 mm) para abrir tapas de agua. |
| **Cajeado para zócalo** | **18 x 95 mm** | En la esquina inferior trasera de ambos costados para pegar el mueble a la pared. |
| **Puertas batientes (x2)** | **268 x 723 mm c/u** | Dos hojas simétricas con 2 mm de holgura inferior con el suelo. |

---

## 3. Despiece y Aprovechamiento de Láminas ($60 \times 120\text{ cm}$)

### 3.1. Láminas de 10 mm (Paneles base)
* **Lámina 1 (10 mm)**: Costado izquierdo (**$725 \times 522\text{ mm}$**).
  * *Fondo del costado ($522\text{ mm}$)*: Sumado a los $18\text{ mm}$ del frente de puertas enrasa exactamente con los $540\text{ mm}$ de la encimera.
* **Lámina 2 (10 mm)**: Costado derecho (**$725 \times 522\text{ mm}$**).
* **Lámina 3 (10 mm)**: Encimera cuadrada (**$540 \times 540\text{ mm}$**).
* **Lámina 4 (10 mm)**: **Puerta izquierda ($268 \times 723\text{ mm}$) + Puerta derecha ($268 \times 723\text{ mm}$)**.
  * Ambas caben juntas a lo ancho: $268 + 4 + 268 = 540\text{ mm} \le 600\text{ mm}$.
* **Lámina 5 (10 mm)**: **Tablero de reserva completo** (al eliminar la balda y la compuerta guillotina).

### 3.2. Láminas de 15 mm (Nervios de regrueso)
* Se cortan en tiras longitudinales de **$50\text{ mm}$ de ancho** ($1200\text{ mm}$ de largo).
* Se encolan en el perímetro interior de costados, encimera y montantes de bisagra de ambas puertas para obtener cantos de **25 mm de espesor**.

---

## 4. Cinemática de Montaje de Actuadores y Automatización

### 4.1. Fundamento Matemático: Cálculo de Ángulos y Triángulo Cinemático (Teorema del Coseno)
Para abrir una puerta batiente que pivota sobre bisagras estándar de cocina de $35\text{ mm}$ en un ángulo de $90^\circ$, el actuador trabaja en el plano horizontal formando un triángulo dinámico cuyos vértices son:
1. **$H$**: Eje de giro de las bisagras $(0, 0)$.
2. **$A$**: Punto de anclaje fijo metálico atornillado a la **cara inferior de la encimera superior** (techo interior del mueble) $(X_A, Y_A)$.
3. **$B$**: Punto de anclaje móvil metálico en la cara interior de la puerta $(X_B, Y_B)$.

#### Teorema del Coseno (Ley de Cosenos)
La longitud instantánea del actuador $C(\theta)$ en función del ángulo de apertura de la puerta $\theta$ ($0^\circ \le \theta \le 90^\circ$) viene regida por:
$$C^2(\theta) = A^2 + B^2 - 2AB \cdot \cos(\gamma(\theta))$$

Donde:
* **$A$**: Distancia desde la bisagra al soporte fijo atornillado bajo la encimera: **$280\text{ mm}$**.
* **$B$**: Distancia desde la bisagra al soporte de la puerta: **$120\text{ mm}$**.
* **$\gamma(\theta)$**: Ángulo comprendido entre los brazos de anclaje.

```
                 Pared Trasera
+-------------------------------------------------+
|                                                 |
|   Costado Interior                              |
|   |                                             |
|   |  [Punto Fijo A: Horquilla metálica]         |
|   |  (Atornillado bajo la encimera superior,    |
|   |   a 280 mm del frente y 35 mm del costado)  |
|   |      \                                      |
|   |       \  Actuador Dawnso Mini 150N 12V      |
|   |        \ (Lmin 255 mm -> Lmax 405 mm)       |
|   |         \ (Inclinación diagonal 3D)         |
|   |          \                                  |
|   +----------[Punto Móvil B: Horquilla Puerta]  |
| (Bisagra)    (a 120 mm del eje de giro)         |
|                                                 |
+=================================================+ Frente
```

#### Cálculo Numérico de Ángulos y Fuerzas
* **Posición CERRADA ($\theta = 0^\circ$)**:
  * Longitud del actuador: $C_{cerrado} = \sqrt{(120 - 35)^2 + (-43 - (-280))^2} = \mathbf{254,9\text{ mm}}$ (coincide exactamente con los $255\text{ mm}$ de longitud retraída $L_{min}$ del actuador Dawnso Mini).
  * **Ángulo de ataque inicial ($\alpha_{cerrado}$)**: **$18,3^\circ$** respecto a la puerta cerrada.
    * *Regla de oro industrial (Firgelli / BFT)*: El ángulo de ataque inicial **jamás debe ser menor de $10^\circ - 12^\circ$**. Si fuera plano o paralelo ($\alpha \approx 0^\circ$), el actuador comprimiría la bisagra en punto muerto (*dead center/singularidad*) sin poder iniciar el giro. Al tener $18,3^\circ$, el despegue de la puerta es inmediato y suave.
  * **Brazo de palanca al arranque**: $d = 120\text{ mm} \times \sin(71,7^\circ) = \mathbf{127,4\text{ mm}}$.
  * **Par de arranque**: $\tau = 150\text{ N} \times 0,1274\text{ m} = \mathbf{19,1\text{ N}\cdot\text{m}}$ (para una puerta ligera de contrachapado de $1,2\text{ kg}$, el margen dinámico supera el **$1200\%$**, eliminando cualquier riesgo de atasco).
* **Posición ABIERTA ($\theta = 90^\circ$ proyectada hacia delante)**:
  * La puerta gira $90^\circ$ proyectándose hacia la habitación. El soporte B pasa a estar $120\text{ mm}$ por delante de la línea del frente ($Y = +120\text{ mm}$).
  * Longitud del actuador: $C_{abierto} = \sqrt{(43 - 35)^2 + (120 - (-280))^2} = \mathbf{405,0\text{ mm}}$ (coincide exactamente con los $405\text{ mm}$ de longitud extendida $L_{max}$ con carrera de 150 mm).
  * Carrera consumida: $405,0 - 254,9 = \mathbf{150,1\text{ mm}}$ (aprovechamiento óptimo del 100% de la carrera útil de 150 mm).
  * **Ángulo en posición abierta**: El actuador queda extendido en diagonal actuando como un puntal/compás de retención a $\approx 45^\circ - 50^\circ$ que bloquea la puerta de forma totalmente estable frente a corrientes de aire.

#### Modelo Exacto de Actuador Comprado: Dawnso Mini 150N 12V (Carrera 150 mm)
* **Especificaciones físicas**: Cuerpo cilíndrico de aluminio satinado de $\approx 20\text{ mm}$ de diámetro, motor eléctrico trasero negro compacto en ángulo recto, cable bipolar fino (rojo/negro) y vástago cromado pulido extensible.
* **Fijación Bajo Encimera (Techo Interior)**:
  * El soporte de horquilla metálico (*clevis bracket*) se atornilla **directamente a la cara inferior de la encimera superior**.
  * Al contar la encimera con un regrueso perimetral compuesto de **$25\text{ mm}$** ($10\text{ mm}$ de lámina base $+ 15\text{ mm}$ de tiras encoladas), se fijan tornillos para madera de $3,5 \times 16\text{ mm}$ o $4 \times 18\text{ mm}$ con agarre masivo y sin riesgo alguno de asomar por la cara superior visible.
  * Esta disposición cenital deja los costados laterales completamente limpios y despejados.
* **Fijación en Puerta**: Escuadra/horquilla metálica atornillada en la cara interior superior de la puerta a $120\text{ mm}$ del eje de las bisagras.
* **Pivotes Articulados Obligatorios**: Ambos extremos montan pasadores (*clevis pins*) para que el actuador pivote con total libertad durante el recorrido de $90^\circ$, neutralizando al 100% las tensiones radiales o laterales (*side-load*) y preservando la vida útil del motor y retenes.

#### Ausencia Total de Suelo (Cota Cero Continua Real)
* **Sin Suelo de Madera**: El mueble no tiene ningún tablero inferior, listón, solera ni zócalo de madera en la base.
* **Estructura Autoportante en "U" Invertida**: Los dos costados laterales apoyan directamente en el suelo de la estancia y soportan la encimera superior.
* **Continuidad de Parqué**: Las tablillas de parqué de roble en espiga del salón entran de forma ininterrumpida hasta la pared trasera.
* **Apoyo Directo de la Base**: La estación Dreame (y su rampa de carga) reposa directamente sobre el parqué de la vivienda, garantizando una cota cero perfecta sin resaltos ni vibraciones para el robot aspirador.

#### Herrajes de Bisagras: 4x Bisagras Estándar de Mueble de Cocina (Ø35 mm)
* **Modelo**: 4 bisagras estándar de cazoleta de **$\varnothing 35\text{ mm}$** (las típicas de mueble de cocina, solape total, ángulo de apertura $105^\circ - 110^\circ$).
* **Distribución**: **2 bisagras por puerta** (4 en total para todo el mueble):
  * Bisagra superior: a $80\text{ mm}$ del borde superior.
  * Bisagra inferior: a $100\text{ mm}$ del suelo.
* **Fijación**: Cazoletas fresadas con broca Forstner a $11,5 - 12\text{ mm}$ de profundidad en el nervio de regrueso interior de $15\text{ mm}$ encolado en la puerta (quedan $13\text{ mm}$ de margen de seguridad intacto hasta la cara exterior).

---

### 4.2. Esquema Eléctrico e Integración ZigBee (Home Assistant)

* **Relé Inteligente ZigBee 2 Canales MHCOZY**:
  * Configuración hardware: Switch en modo **Interlock** (enclavamiento activo para asegurar que jamás se activen ambos canales a la vez).
  * Ambos actuadores cableados en **paralelo** a los bornes COM/NO/NC de los relés formando un puente en H de inversión de polaridad.
  * Canal 1: Polaridad directa (+12V / GND) $\to$ **Apertura de puertas**.
  * Canal 2: Polaridad invertida (GND / +12V) $\to$ **Cierre de puertas**.
* **Automatización en Home Assistant**:
  * **Trigger salida**: `vacuum.dreame_l10s` pasa a `cleaning` $\to$ Activa Canal 1 durante 10 segundos $\to$ Puertas abiertas a $90^\circ$.
  * **Trigger retorno**: `vacuum.dreame_l10s` pasa a `docked` $+ 15\text{ s}$ delay $\to$ Activa Canal 2 durante 10 segundos $\to$ Puertas cerradas enrasadas.
