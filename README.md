# Mueble Recibidor Automatizado a Cota Cero para Robot Aspirador

Consola de entrada cuadrada y minimalista a medida diseñada para ocultar la estación de autovaciado y robot aspirador **Dreame (L10s / X40)** a **Cota Cero**, con sistema de **doble puerta batiente motorizada** con actuadores que abren hacia delante, interior 100% diáfano (sin balda) y control nativo por **Zigbee (Home Assistant)**.

| Plano con Cotas Milimétricas | Fotografía de Referencia Arquitectónica |
| :---: | :---: |
| ![Plano con Cotas Técnicas](foto_realista_mueble_cuadrado_cotas.jpg) | ![Fotografía Realista](foto_realista_mueble_cuadrado_dos_puertas.jpg) |

---

## 1. Planos Gráficos y Renders de Referencia

* **Plano Fotorrealista con Cotas Milimétricas**: [`foto_realista_mueble_cuadrado_cotas.jpg`](foto_realista_mueble_cuadrado_cotas.jpg)
  * Muestra todas las cotas acotadas sobre el modelo 3D fotorrealista con líneas y flechas arquitectónicas: $540\text{ mm}$ ancho, $540\text{ mm}$ fondo, $750\text{ mm}$ alto, $268\text{ mm}$ puerta, $490\text{ mm}$ hueco libre, $423\text{ mm}$ base y $157\text{ mm}$ espacio libre superior.
* **Fotografía Realista Exterior/Interior**: [`foto_realista_mueble_cuadrado_dos_puertas.jpg`](foto_realista_mueble_cuadrado_dos_puertas.jpg)
  * Muestra la consola cuadrada acabada en blanco satinado con ambas puertas abiertas hacia delante a cota cero, la estación Dreame interior y el robot saliendo por el centro sobre el parqué de espiga.

---

## 2. Dimensiones Generales Recalculadas (Encimera Cuadrada)

Para cumplir la condición de **hacer el mueble todo lo estrecho posible con encimera cuadrada ($Ancho = Fondo$)**, la cota viene fijada por la profundidad de la aspiradora:

| Cota | Medida | Justificación Técnica y Holguras |
| :--- | :---: | :--- |
| **Encimera (Planta Cuadrada)**| **$540 \times 540\text{ mm}$** | Planta simétrica perfecta ($54\text{ cm}$ de ancho por $54\text{ cm}$ de fondo). |
| **Alto exterior** | **750 mm** | Altura esbelta de consola recibidor bajo cintura. |
| **Cajeado trasero (Rodapié)** | **$18\text{ mm}$ (fondo) $\times 95\text{ mm}$ (alto)** | Vaciado inferior trasero en ambos costados para encajar el zócalo de pared de $15\text{ mm}$ y pegar el mueble 100% a la pared. |
| **Fondo interior útil libre** | **522 mm** | Desde la pared hasta la cara interior de las puertas cerradas ($540 - 18\text{ mm}$ puerta). |
| **Posición estación Dreame** | **508 mm desde pared** | $15\text{ mm}$ (rodapié) $+ 493\text{ mm}$ (estación con rampa y robot acoplado). |
| **Margen frontal libre** | **+14 mm libres** | **La aspiradora NO queda pegada a las puertas** (queda $1,4\text{ cm}$ de separación entre la rampa y las puertas). |
| **Ancho interior libre** | **490 mm** | $540 - 50\text{ mm}$ (costados regruesados a 25 mm). La base Dreame mide $423\text{ mm}$ $\to$ **$33,5\text{ mm}$ libres por lado**. |
| **Altura interior diáfana** | **725 mm libres** | **Sin balda interior**: Espacio único y continuo de suelo a techo. |
| **Margen superior para tapas** | **+157 mm libres** | Sobre los $568\text{ mm}$ de la estación, para abrir las tapas y extraer los depósitos de agua hacia arriba sin mover el mueble. |
| **Puertas frontales (x2 hojas)**| **$268 \times 723\text{ mm}$ cada una** | Dos hojas batientes que abren hacia delante, dejando 2 mm de holgura con el suelo para girar libremente. |

---

## 3. Componentes Comprados y su Aprovechamiento

### 3.1. Tableros de Contrachapado Comprados
* **5x Tablero contrachapado crudo $60 \times 120 \times 1,0\text{ cm}$**
* **2x Tablero contrachapado crudo $60 \times 120 \times 1,5\text{ cm}$**

#### Despiece optimizado sobre las láminas de $60 \times 120\text{ cm}$:
1. **Lámina 1 (10 mm)**: Costado izquierdo (**$725 \times 522\text{ mm}$**).
   * *Justificación de fondo ($522\text{ mm}$)*: Costado ($522\text{ mm}$) + Puerta cerrada ($18\text{ mm}$) = **$540\text{ mm}$** (enrasa a la perfección bajo la encimera de $540\text{ mm}$).
2. **Lámina 2 (10 mm)**: Costado derecho (**$725 \times 522\text{ mm}$**).
3. **Lámina 3 (10 mm)**: Encimera cuadrada (**$540 \times 540\text{ mm}$**).
4. **Lámina 4 (10 mm)**: **Puerta izquierda ($268 \times 723\text{ mm}$) + Puerta derecha ($268 \times 723\text{ mm}$)**.
   * *Ambas puertas caben juntas en un solo tablero*: $268 + 4 + 268 = 540\text{ mm} \le 600\text{ mm}$, y $723\text{ mm} \le 1200\text{ mm}$.
5. **Lámina 5 (10 mm)**: **Tablero de reserva completo** (la balda interior y la guillotina se han eliminado).
6. **Láminas de 15 mm (2 uds)**: Se cortan en tiras longitudinales de **$50\text{ mm}$ de ancho** para regruesar los cantos perimetrales a 25 mm.

### 3.2. Pintura y Acabado
* **1x Imprimación universal LUXENS 1 L** (2 manos en cantos cortados como tapaporos/sellador + 1 mano general).
* **1x Esmalte ecológico TITANLUX blanco satinado 750 ml** (2 manos de acabado sedoso y lavable).

### 3.3. Automatización y Herrajes
* **2x Micro Actuadores Lineales Dawnso Mini 150N 12V DC (carrera 150 mm)**:
  * **Características físicas**: Modelo cilíndrico delgado de aluminio plateado ($\approx 20\text{ mm}$ diámetro), motor trasero compacto negro en ángulo recto con fino cable bipolar y vástago cromado pulido extensible.
  * **Ubicación en altura**: Zona superior diáfana bajo la encimera ($157\text{ mm}$ libres sobre la base Dreame).
  * **Disposición cinemática**: **Diagonal en plano horizontal** (abren puertas batientes que giran $90^\circ$ hacia delante).
  * **Anclaje de chasis (Punto Fijo Cenital)**: Soporte metálico en horquilla (*clevis bracket*) con pasador **atornillado directamente a la cara inferior de la encimera superior** (retrasado $\approx 280\text{ mm}$ del frente y a $\approx 35\text{ mm}$ del costado). Se fija con tornillos para madera de $3,5 \times 16\text{ mm}$ en el regrueso de 25 mm de la encimera con máxima firmeza y sin asomar a la cara superior.
  * **Anclaje de puerta (Punto Móvil)**: Soporte metálico en horquilla con pasador atornillado a la cara interior superior de la puerta a $\approx 120\text{ mm}$ del eje de las bisagras.
  * **Modo Push-to-Open**: Con puerta cerrada, el actuador está retraído ($L_{min} = 255\text{ mm}$) con ángulo de ataque de $18,3^\circ$ (despegue instantáneo sin punto muerto). Al extenderse los $150\text{ mm}$ ($L_{max} = 405\text{ mm}$), empuja la puerta abriéndola a exactamente $90^\circ$ perpendicular a la fachada y sujetándola con firmeza.
  * **Pivotes articulados obligatorios**: Ambos extremos llevan pasador giratorio (*clevis pin*) para permitir la libre rotación horizontal y eliminar al 100% tensiones laterales (*side load*).
* **Ausencia Total de Suelo (Cota Cero Real)**: El mueble carece por completo de suelo de madera o travesaño inferior; el parqué de espiga entra de forma continua hasta la pared y la estación Dreame apoya directamente sobre él.
* **4x Bisagras estándar de cazoleta para muebles de cocina (Ø35 mm)**: 2 bisagras por puerta (4 en total, solape total, apertura $105^\circ-110^\circ$), embutidas a $12\text{ mm}$ en el regrueso interior de 15 mm mediante broca Forstner.
* **1x Módulo Relé Inteligente ZigBee 2 Canales MHCOZY** (85-250V AC / 5V USB, contactos secos en modo *Interlock* conmutando inversión de polaridad para apertura/cierre).
* **1x Fuente de alimentación 12V DC** ($\ge 2\text{A}$).

---

## 4. Esquema de Cotas en Alzado y Planta

### 4.1. Alzado Frontal (Puertas Abiertas hacia delante)

```
                     540 mm (Ancho Exterior)
                     490 mm (Hueco Interior Libre)
        <------------------------------------------------>
        +----+--------------------------------------+----+  ^
        |    |       ENCIMERA CUADRADA (25 mm)      |    |  |
        | 25 |                                      | 25 |  |
        | mm |                                      | mm |  |
        |    |                                      |    |  |
        | c  |    ESPACIO DIÁFANO SUPERIOR (157 mm) | c  |  | 750 mm
        | o  |     (Apertura libre de depósitos)    | o  |  | (Alto Total)
        | s  |                                      | s  |  |
        | t  + - - - - - - - - - - - - - - - - - - -+ t  |  |
        | a  |                                      | a  |  |  ^
        | d  |         BASE DREAME                  | d  |  |  |
        | o  |         (Ancho: 423 mm)              | o  |  |  | 568 mm (Alto Base)
        |    |         [Holgura: 33.5 mm por lado]  |    |  |  |
        | I  |                                      | D  |  |  |
        | z  |            ROBOT Ø350 mm             | e  |  |  |
  [Pta] | q  |          (Sale por el centro)        | r  |  |  |
 [Izquierda] +======================================+ [Pta Derecha] Suelo (Cota Cero)
```

### 4.2. Planta Superior (Corte de Profundidad contra la Pared)

```
                 Pared con Rodapié de 15 mm
============================================================= ^
|| [Cajeado 18x95]                         [Cajeado 18x95] || |
||<- Costado Izq (522 mm fondo)     Costado Der (522 mm) ->|| |
||                                                         || |
||         +-------------------------------------+         || |
||         |  Base Dreame apoyada en rodapié     |         || | 522 mm
||         |  (Fondo total con rampa: 493 mm)    |         || | (Fondo costados)
||         |  [Posición frontal: 508 mm]         |         || |
||         |                                     |         || |
||         |            ROBOT Ø350 mm            |         || |
||         +-------------------------------------+         || |
||                                                         || v
||<·············· Margen libre frontal: 14 mm ············>|| === Frente costados
||===========================|=============================|| ^ 18 mm (Puertas)
       Puerta Izquierda               Puerta Derecha          v
        (268 mm ancho)                 (268 mm ancho)
<---------------------- 540 mm exterior -------------------->
<------------ 540 mm fondo total (Encimera cuadrada) ------->
```

---

## 5. Procedimiento de Fabricación Paso a Paso

```mermaid
flowchart TD
    A["Paso 1: Corte de costados, encimera y 2 puertas (60x120 cm)"] --> B["Paso 2: Cajeado para rodapié (18x95 mm) en costados traseros"]
    B --> C["Paso 3: Encolado de nervios de 15 mm (Regrueso perimetral a 25 mm)"]
    C --> D["Paso 4: Fresado de cazoletas de 35 mm para 4 bisagras (2 por puerta)"]
    D --> E["Paso 5: Sellado de cantos con imprimación Luxens y esmalte blanco"]
    E --> F["Paso 6: Ensamblaje estructural de costados y encimera a cota cero"]
    F --> G["Paso 7: Instalación de las 2 puertas y mecanismo de empuje/actuadores"]
    G --> H["Paso 8: Conexión eléctrica Zigbee y automatización Home Assistant"]
```

1. **Despiece y Cajeado de Rodapié**:
   * Corta los 2 costados a **$725 \times 522\text{ mm}$** y la encimera a **$540 \times 540\text{ mm}$**.
   * En la esquina inferior trasera de ambos costados, realiza con caladora el cajeado de **$18\text{ mm}$ de profundidad $\times 95\text{ mm}$ de altura** para librar el zócalo de la pared.
   * Corta las 2 puertas a **$268 \times 723\text{ mm}$** del tablero 4.
2. **Nervios de Regrueso a 25 mm**:
   * Encola tiras de $50\text{ mm}$ de ancho (tablero de 15 mm) en el perímetro interior de los costados, encimera y bordes de bisagra de ambas puertas.
   * Pasa lija P150 por los cantos para dejarlos enrasados y uniformes como un bloque de 25 mm.
3. **Fresado de Cazoletas de Bisagras**:
   * Con broca Forstner de 35 mm, fresa 2 cazoletas por puerta a 12 mm de profundidad sobre el nervio de 15 mm. Al tener 25 mm de espesor compuesto, no hay riesgo de perforar el frente.
4. **Tratamiento y Pintura**:
   * 2 manos de imprimación LUXENS en cantos cortados (como tapaporos) con lija P240 intermedia.
   * 1 mano general a todo el mueble y 2 manos de esmalte TITANLUX blanco satinado.
5. **Montaje e Instalación**:
   * Une los 2 costados y la encimera superior formando el puente estructural en "U" invertida (sin suelo de madera inferior).
   * Coloca el mueble pegado a la pared encajando el cajeado de $18 \times 95\text{ mm}$ en el rodapié de la vivienda.
   * Monta las 2 puertas con las 4 bisagras estándar de cocina de $35\text{ mm}$ (2 bisagras por puerta).
   * Atornilla los soportes de horquilla traseros metálicos de los actuadores Dawnso Mini directamente a la **cara inferior de la encimera superior** (retrasados $280\text{ mm}$ del frente y a $35\text{ mm}$ de cada costado) usando tornillos de $3,5 \times 16\text{ mm}$ en el regrueso de 25 mm.
   * Atornilla los soportes delanteros a la cara interior superior de cada puerta batiente (a $120\text{ mm}$ del eje de las bisagras) e inserta los pasadores articulados (*clevis pins*) en ambos extremos para permitir el libre giro horizontal sin cargas laterales.
6. **Conexión Eléctrica ZigBee y Home Assistant**:
   * Configura el relé MHCOZY de 2 canales en modo **Interlock** (enclavamiento mutuo) para evitar activación simultánea de apertura y cierre.
   * Conecta la fuente de 12V DC a los contactos COM/NO/NC configurando inversión de polaridad (puente en H) con ambos actuadores cableados en paralelo.
   * En Home Assistant, crea la automatización: al pasar la entidad de la Dreame a `cleaning`, activa el Canal 1 (abrir puertas); al volver a `docked` y transcurrir 15 segundos, activa el Canal 2 (cerrar puertas).
