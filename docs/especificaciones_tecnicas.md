# Especificaciones Técnicas y Constructivas: Mueble Recibidor Cuadrado con Doble Puerta

Proyecto de consola recibidor cuadrada a medida diseñada para ocultar la estación de autovaciado y robot aspirador **Dreame L10s / X40** a **Cota Cero**, con **doble puerta batiente motorizada** de apertura frontal, interior 100% diáfano (sin balda) y cajeado trasero para salvar rodapié de 1,5 cm.

![Mueble Recibidor Cuadrado con Doble Puerta Abierta](../foto_realista_mueble_cuadrado_dos_puertas.jpg)

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
| **Alto exterior** | **750 mm** | Proporción cúbica/armónica con los 54 cm de ancho y fondo. |
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

## 4. Mecanismo de Apertura y Automatización

1. **Cinemática de Apertura**:
   * Ambas hojas batientes abren hacia delante ($90^\circ - 100^\circ$) accionadas por dos micro actuadores lineales de 12V montados en el interior.
   * Sin compuerta inferior ni rieles: el frente completo queda despejado de suelo a techo a cota cero.
2. **Esquema Eléctrico (Inversión de Polaridad / Puente en H)**:
   * Los 2 actuadores se conectan en **paralelo** para moverse en perfecta sincronía.
   * **Relé Inteligente ZigBee 2 Canales MHCOZY**:
     * Modo: **Interlock** (enclavamiento hardware activado para que jamás coincidan ambos canales activos).
     * Canal 1: Aplica $+12\text{V}$ al polo A y GND al polo B $\to$ **Apertura de puertas**.
     * Canal 2: Aplica GND al polo A y $+12\text{V}$ al polo B $\to$ **Cierre de puertas**.
3. **Lógica de Automatización (Home Assistant)**:
   * **Trigger salida**: `vacuum.dreame_l10s` cambia a estado `cleaning`.
   * **Acción 1**: Activar Canal 1 del relé MHCOZY durante 8-10 segundos (apertura total de puertas).
   * **Acción 2**: El robot abandona la base y sale al salón.
   * **Trigger retorno**: `vacuum.dreame_l10s` cambia a `docked`.
   * **Acción 3**: Delay de 15 segundos (asegura acoplamiento e inicio de vaciado).
   * **Acción 4**: Activar Canal 2 del relé MHCOZY durante 8-10 segundos (cierre completo de ambas puertas).
