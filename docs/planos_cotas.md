# Planos Técnicos y Esquemas de Cotas: Mueble Cuadrado 540 x 540 mm (2 Puertas)

Este documento recoge el esquema dimensional y los planos del mueble recibidor a **Cota Cero** con encimera cuadrada ($540 \times 540\text{ mm}$), dos puertas batientes y cajeado para rodapié de 15 mm.

---

## 1. Fotografía de Referencia

* **Fotografía Realista Principal (Doble Puerta Abierta hacia delante)**: [`../foto_realista_mueble_cuadrado_dos_puertas.jpg`](../foto_realista_mueble_cuadrado_dos_puertas.jpg)
  * Muestra la encimera cuadrada de $54 \times 54\text{ cm}$, las dos puertas batientes abiertas hacia delante, la estación Dreame a cota cero en el interior diáfano sin balda y el robot saliendo por el centro.

---

## 2. Esquema de Cotas en Alzado Frontal (Puertas Abiertas)

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

---

## 3. Esquema en Planta Superior (Fondo pegado a la Pared)

```
        Pared con Rodapié de 15 mm
=====================================================
|| [Cajeado 18x95]                 [Cajeado 18x95] ||
||<- Costado Izq                    Costado Der -> ||
||                                                 ||
||         +---------------------------+           ||
||         |  Base Dreame apoyada      |           ||
||         |  en rodapié (508 mm)      |           ||
||         |                           |           ||
||         |       ROBOT Ø350 mm       |           ||
||         +---------------------------+           ||
||                                                 ||
||<·········· Margen libre: 14 mm ················>||  (No toca las puertas)
||========================|========================||
       Puerta Izquierda       Puerta Derecha
        (268 mm ancho)         (268 mm ancho)
<----------------- 540 mm exterior --------------->
```

---

## 4. Tabla Resumen de Tolerancias y Holguras Críticas

| Componente | Dimensión Pieza | Dimensión Hueco | Holgura Resultante | Evaluación |
| :--- | :--- | :--- | :--- | :--- |
| **Encimera cuadrada** | 540 x 540 mm | Planta mueble | **0 mm (enrasada)** | Proporción simétrica perfecta 1:1. |
| **Base Dreame (Ancho)** | 423 mm | 490 mm interior | **67 mm total (33.5 mm/lado)** | Holgura muy amplia para bisagras y giro. |
| **Depósitos de agua (Alto)** | 568 mm base | 725 mm a encimera | **157 mm libres** | **Sin balda**: Extracción comodísima hacia arriba. |
| **Frente de la rampa Dreame**| 508 mm desde pared | 522 mm interior | **14 mm libres frontales** | La aspiradora **no toca las puertas**. |
| **Cajeado para rodapié** | 15 mm rodapié | 18 mm cajeado | **3 mm de margen** | Apoyo 100% enrasado del mueble contra la pared. |
| **Puertas batientes (x2)** | 2x 268 mm ancho | 540 mm exterior | **4 mm de junta central/lateral**| Cierre limpio sin rozamiento. |
| **Puertas respecto al suelo**| 723 mm alto puerta| 725 mm al suelo | **2 mm libres inferiores** | Giro libre sin rozar el parqué de espiga. |
