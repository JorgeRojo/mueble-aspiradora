# Guía Maestra de Generación Visual y Renderizado: Mueble Aspiradora Cota Cero

Este documento recoge la metodología técnica, fórmulas cinemáticas, prompts exactos y algoritmos de postprocesado utilizados para generar las imágenes fotorrealistas y planos acotados del mueble recibidor para la estación Dreame a cota cero.

---

## 1. El Problema de la Proporción (Sesgo de Difusión a "Mueble Ancho")

### Causa del Fallo
Los modelos de difusión (Gemini/Imagen/Midjourney) poseen un fuerte sesgo hacia muebles aparadores anchos (120–160 cm) cuando se usan palabras como *"mueble recibidor"*, *"aparador"* o *"consola"*, o cuando el lienzo es apaisado (16:9 o 4:3). Esto provocaba que el mueble de 54x54 cm se representara deformado como un mueble bajo y muy ancho.

### Solución y Trucos de Prompt Engineering
1. **Lienzo Vertical (Portrait)**:
   * Forzar formato de aspecto vertical (ej. $896 \times 1200$ píxeles, ratio 3:4 o 9:16).
2. **Anclas Proporcionales Comparativas**:
   * En vez de dar solo números abstractos, dar objetos cotidianos de tamaño conocido como ancla de escala:
     * *"Encima de la encimera de 54x54 cm hay un portátil de 14 pulgadas (32 cm de ancho): el portátil ocupa MÁS DEL 60% del ancho de la encimera"*.
     * *"Consola esbelta y estilizada: la altura (75 cm) es un 40% mayor que la anchura (54 cm) (relación de aspecto vertical 1.39:1)"*.
3. **Ancla de Ocupación Interior**:
   * *"El ancho interior libre es de solo 49 cm y la base Dreame mide 42,3 cm: la base ocupa el 86% del hueco interior, dejando apenas 3,3 cm (un par de dedos) de holgura por lado"*. Esto elimina los laterales cavernosos vacíos.

---

## 2. Cinemática y Colocación de los Actuadores Lineales

### Causa del Fallo Inicial
La IA dibujaba los actuadores como varillas verticales flotantes o pegadas en plano al marco frontal superior, lo cual es físicamente absurdo porque las puertas abren hacia delante a 90°.

### Cinemática Horizontal Real (Teorema del Coseno)
Para abrir una puerta batiente de 268 mm de ancho a 90°:
* **Punto de giro**: Bisagras en el vértice frontal lateral ($O$).
* **Anclaje de chasis (A)**: En el techo interior (cara inferior de la encimera), a $x = 55\text{ mm}$ hacia el interior y $y = -225\text{ mm}$ hacia el fondo.
* **Anclaje en puerta (B)**: En la cara interior superior de la puerta batiente, a $B = 175\text{ mm}$ del eje de giro.
* **Recorrido del actuador**:
  * Puerta cerrada ($\gamma = 0^\circ$): longitud cerrada $L_c = 255\text{ mm}$.
  * Puerta abierta ($\gamma = 90^\circ$): longitud extendida $L_o = 405\text{ mm}$ (carrera de $150\text{ mm}$).
* **Ángulo de ataque inicial**: $\beta = 61.9^\circ$.
* **Par de arranque**: $\tau = F \cdot B \cdot \sin(\beta) = 150\text{ N} \cdot 0.175\text{ m} \cdot \sin(61.9^\circ) = 23.2\text{ N}\cdot\text{m}$ (sobrado para una puerta de 2.1 kg).

### Descripción del Prompt de Actuadores
* *"Modelo exacto: Micro Actuador Lineal Eléctrico Cilíndrico Delgado Dawnso Mini 150N 12V (cuerpo tubular fino de aluminio plateado de 20 mm, cabezal motor trasero negro con cable bipolar fino, y vástago cromado pulido extensible)"*.
* *"Soportes de horquilla metálica (clevis) traseros ATORNILLADOS DIRECTAMENTE A LA CARA INFERIOR DE LA ENCIMERA (al techo interior del mueble)"*.
* *"Los vástagos cromados se extienden en el plano horizontal superior proyectándose diagonalmente hacia delante, anclados a la cara interior superior de cada puerta abierta mediante otra pequeña horquilla con pasador"*.

---

## 3. Arquitectura Eléctrica y Automatización

### Actuadores
* **Modelo**: Dawnso Mini 150N, carrera 150 mm, 12V DC.
* **Corriente**: $\approx 0.6\text{A}$ nominal por unidad ($\approx 1.2\text{A}$ en paralelo, pico 1.5–2A).
* **Compatibilidad espacial**: Longitud cerrada 255 mm, carrera 150 mm. Cabe perfectamente en los 157 mm de luz superior sobre la estación Dreame y los 522 mm de fondo.

### Relé Zigbee (MHCOZY 2 Canales)
* **Especificación**: MHCOZY 2CH Zigbee (5V Micro-USB / 85–250V AC, contactos secos NO/NC/COM 10A).
* **Capacidad**: 10A por canal; 2 actuadores consumen $< 2\text{A}$ $\to$ margen de seguridad $> 500\%$.
* **Conexión en Paralelo con Puente H**:
  * Canal 1: Conecta +12V a cable rojo y GND a cable negro (Extensión / Apertura).
  * Canal 2: Conecta GND a cable rojo y +12V a cable negro (Retracción / Cierre).
* **Modo Interlock (Enclavamiento por Hardware)**:
  * **CRÍTICO**: Activar el modo *Interlock* mediante el botón físico de la placa.
  * Esto garantiza que al activar un canal, el otro se apaga automáticamente, haciendo **imposible** un cortocircuito accidental de la fuente de 12V.

---

## 4. Técnica de Cota Cero Total (Eliminación de Suelo de Madera)

### El Reto de Difusión
Los modelos de IA tienden a reintroducir un suelo de madera (zócalo o balda inferior) porque en su dataset casi todos los armarios tienen base inferior.

### Algoritmo de Postprocesado Fotométrico en Python
Para sustituir el suelo/zócalo interior por el parqué de espiga de roble de la vivienda de forma completamente invisible y continua:

1. **Muestreo de Textura Real de Parqué**:
   * Se extrajo el parqué en espiga del primer plano ($x \in [240, 330]$, $y \in [1030, 1180]$).
   * Respeta los dos ejes del parqué: vetas a $+39^\circ$ (sube hacia la derecha, pendiente $-0.81$) e interbloqueo a $+50^\circ$ (pendiente $+1.18$).

2. **Calibración Lumínica a la Sombra Interior (Ley de Paso Cero)**:
   * Si se pega el parqué del primer plano sin calibrar, su brillo es de $L \approx 185$ (iluminado), mientras que la sombra bajo el mueble es de $L \approx 90$ en el umbral y $L \approx 25$ en el fondo.
   * La función de modulación de luminancia calculada es:
     $$f(y) = \left(0.15 + 0.37 \cdot \left(\frac{y - 820}{1020 - 820}\right)^{1.2}\right) \cdot \text{wall\_ao}(x, y) \cdot \text{contact\_ao}(x, y)$$
   * Esto hace que en el umbral frontal ($y=1018$) el factor sea exactamente $0.48$ ($185 \cdot 0.48 \approx 89$, coincidencia exacta con el parqué adyacente $\Delta L = 0$).
   * En el fondo ($y=820$), el factor es $0.15$ ($185 \cdot 0.15 \approx 27$, coincidencia exacta con la sombra del rincón trasero $\Delta L = 0$).

3. **Oclusión Ambiental en Vértices (Crevice AO)**:
   * En el encuentro con los costados verticales ($x=282$ y $x=668$), la oclusión ambiental solo se aplica en el interior ($y < 1005$), decayendo a $1.0$ al cruzar el umbral hacia la puerta abierta.
   * Sombra de contacto suave en la curvatura del parachoques del robot ($x_{\text{base}}(y)$).

4. **Curvas de Transición Sigmoidales (Smoothstep)**:
   * Se eliminan completamente los cortes rectangulares aplicando la función de suavizado:
     $$S(t) = t^2 (3 - 2t), \quad t \in [0, 1]$$
   * Rampa superior ($y \in [815, 865]$): transición gradual desde la pared trasera.
   * Rampa inferior ($y \in [1014, 1026]$): borrado total del labio del zócalo antiguo y mezcla con el parqué real exterior.

---

## 5. Pipeline de Acotado Vectorial y Callouts (PIL Supersampling)

Para generar imágenes técnicas acotadas con calidad de publicación arquitectónica:
1. **Supersampling 2X**:
   * Generar las líneas, textos y llamadas sobre un lienzo ampliado al doble (`SCALE = 2`).
   * Redimensionar al final con filtro `LANCZOS` para obtener antialiasing perfecto en diagonales y flechas.
2. **Líneas con Halo Blanco**:
   * Trazar primero una línea blanca de grosor `width + 2.5 * SCALE` y encima la línea técnica oscura `(17, 24, 39)` de grosor `width`. Esto asegura máxima legibilidad sobre fondos oscuros o claros.
3. **Píldoras de Texto Semi-transparentes**:
   * Cajas de texto con fondo blanco satinado translúcido `(255, 255, 255, 245)`, borde fino gris grafito `(17, 24, 39, 220)` y radio de esquina de $3\text{ px}$.
4. **Callouts Esenciales en el Plano**:
   * Encimera: $540\text{ mm}$ (Ancho) $\times 540\text{ mm}$ (Fondo).
   * Altura Total: $750\text{ mm}$.
   * Hojas de puerta: $268\text{ mm}$ (Ancho) $\times 723\text{ mm}$ (Alto).
   * Hueco libre interior: $490\text{ mm}$.
   * Base Dreame: $423\text{ mm}$ (ocupa el $86\%$).
   * Holguras laterales: $33.5\text{ mm}$ por lado.
   * Espacio libre sobre tapas: $157\text{ mm}$.
   * Diámetro del robot: $\varnothing 350\text{ mm}$.
   * Callout actuadores: *Dawnso Mini 150N fijado bajo encimera*.
   * Callout bisagras: *Bisagras cazoleta 35 mm (x4 cocina)*.
   * Callout suelo: *Cota Cero Total: Sin suelo interior (parqué continuo)*.

---

## 6. Archivos Maestros en Producción

* [`foto_realista_mueble_cuadrado_dos_puertas.jpg`](file:///Users/jorge/projects/mueble-aspiradora/foto_realista_mueble_cuadrado_dos_puertas.jpg): Fotografía hiperrealista limpia del diseño final.
* [`foto_realista_mueble_cuadrado_cotas.jpg`](file:///Users/jorge/projects/mueble-aspiradora/foto_realista_mueble_cuadrado_cotas.jpg): Plano fotorrealista con acotado milimétrico y llamadas técnicas.
