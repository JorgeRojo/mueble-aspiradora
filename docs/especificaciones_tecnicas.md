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

### 4.1. Fundamento Físico de Montaje (Triángulo Cinemático para 90°)
Un actuador colocado verticalmente sobre una puerta batiente no ejerce ningún par de giro alrededor del eje de las bisagras. Para abrir una puerta batiente que pivota horizontalmente, el actuador **debe trabajar en un plano horizontal**:

```
           Pared Trasera
+-----------------------------------+
|                                   |
|   Costado Interior                |
|   |                               |
|   |  [Punto Fijo A: Clevis]       |
|   |  (a ~280 mm del frente)       |
|   |      \                        |
|   |       \ Actuador 12V          |
|   |        \ (Carrera 150 mm)     |
|   |         \                     |
|   +----------[Punto B: Puerta]    |
| (Bisagra)    (a ~110 mm del eje)  |
|                                   |
+===================================+ Frente
```

1. **Ubicación en Altura**:
   * Instalados en el hueco diáfano superior ($Z = 650 - 680\text{ mm}$ desde el suelo), en los $157\text{ mm}$ que quedan entre la parte superior de la base Dreame ($568\text{ mm}$) y la encimera ($725\text{ mm}$).
   * Quedan completamente fuera de la trayectoria del robot y no obstaculizan la extracción de los depósitos de agua.
2. **Coordenadas de Anclaje Óptimas**:
   * **Punto Fijo (A) en el Costado**: Soporte en horquilla (*clevis bracket*) atornillado a la cara interior del costado a **$280\text{ mm}$** hacia el fondo desde la línea frontal de bisagras.
   * **Punto Móvil (B) en la Puerta**: Soporte en horquilla atornillado a la cara interior de la puerta a **$110\text{ mm}$** del eje de giro de las bisagras.
3. **Comportamiento Cinemático (*Push-to-Open*)**:
   * **Puerta Cerrada ($0^\circ$)**: Actuador completamente retraído ($L_{min} \approx 255\text{ mm}$). Brazo de palanca de inicio: $\approx 135\text{ mm}$. El par de arranque es máximo, despegando la puerta suavemente.
   * **Apertura ($0^\circ \to 90^\circ$)**: Al extender el vástago $150\text{ mm}$ ($L_{max} \approx 405\text{ mm}$), empuja la puerta hasta alcanzar exactamente $90^\circ$ perpendicular a la fachada.
   * **Par y Fuerza**: Con $150\text{ N}$ de fuerza y un brazo de palanca de $80 - 135\text{ mm}$, el actuador entrega más de $12\text{ N}\cdot\text{m}$ de par de rotación, abriendo una hoja ligera de $1,2\text{ kg}$ con suavidad absoluta y sin esfuerzo.
4. **Regla Crítica de Instalación (Eliminación de Cargas Laterales)**:
   * **Imprescindible usar soportes articulados en ambos extremos**: Ambos extremos deben pivotar mediante pasadores (*clevis pins*). Si se fijara rígidamente alguno de los extremos, la fuerza lateral inducida durante el giro de $90^\circ$ doblaría el vástago y quemaría el motor interno.

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
