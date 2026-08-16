# Extracto — M2020 Session 6

## Ficha

- **Fuente primaria:** `00_fuentes/videos/2020 Mentorship/Session 6-001.mov`.
- **Apoyos de navegación:** `10_transcripciones/Session 6-001/Session 6-001.md`, `.srt`, `.json`; 30 frames y `_index.md` en `20_frames/Session 6-001/`.
- **Duración revisada:** 01:24:21, vídeo completo.
- **Fecha visible:** 4-oct-2020 (barra de tareas).
- **Autor/docente:** EM/EssFX. Intervenciones de alumnos: preguntas orales; no se convierten en doctrina de EM salvo respuesta explícita.
- **Instrumentos visibles:** principalmente GBPUSD; también Dow como contraste pedagógico.
- **Material adicional mostrado:** esquema `Price chasing mechanism 2.png` (autoría no acreditada en pantalla) y ficha externa `HSBC FX Liquidity Seeking`, ya procesada por separado como `[PAPER]`.

## Resumen ejecutivo

EM reconstruye el price swing desde la microestructura: una base/origin con liquidez real, un desequilibrio de profundidad, market orders que consumen el lado fino, retirada/repricing de dealers, exhaustion y retorno hacia la liquidez más gruesa. La precisión importante es que el **origin no forma parte de los cinco eventos numerados**; es el punto de partida. Los cinco eventos que EM enumera son `volume shot → price run → exhaustion → shift → fill`.

La segunda mitad añade la pieza que faltaba para interpretar distintas morfologías de una ineficiencia: una orden grande se trocea mediante un execution algorithm. Su agresividad, límite de precio, ventana temporal y pool de liquidez determinan si el precio deja una extensión muy fina, una escalera más estable o un drawback profundo. Mientras el algoritmo siga activo y la liquidez lo persiga, el fill puede retrasarse. La sesión no entrega un trigger visual cerrado para saber en vivo que el algoritmo terminó ni un contrato de trade.

## 1. De book skew a exhaustion

### 1.1 Volumen y liquidez no son sinónimos

- EM fija su vocabulario: “**When I'm referring to volume, I'm always referring to market orders**”; la liquidez son limit orders. [VID-M2020: Session 6 @ 00:12:57–00:13:06]
- En un book sesgado el precio queda expuesto hacia el lado con menos profundidad, pero el momento en que llegará el flujo agresivo que active el movimiento es aleatorio. El skew es condición de vulnerabilidad, no reloj de entrada. [VID-M2020: Session 6 @ 00:05:34–00:08:50]
- El core/origin contiene la concentración más gruesa de liquidez real. Al alejarse de él, el run puede dejar pockets residuales, pero “much less” liquidity; EM no dice que el tramo quede literalmente a cero. [VID-M2020: Session 6 @ 00:09:01–00:12:57]

### 1.2 Fragmentación, retirada y dislocación

- En FX fragmentado, la voluntad real de comprar/vender puede permanecer dentro del rango original mientras el dealer que recibe el flujo y los demás venues reprician. La liquidez existente al mismo precio en otro book no se enruta automáticamente al ticket. [VID-M2020: Session 6 @ 00:17:22–00:20:12]
- EM afirma que, en un único venue, esa liquidez habría frenado antes el desplazamiento; en múltiples dealer venues la falta de acceso común permite una dislocación mayor respecto al área donde se facilitaba el matching. Es explicación de EM, no contraste externo validado aquí. [VID-M2020: Session 6 @ 00:17:22–00:20:12]
- Dealer A puede internalizar la orden de su cliente. Otros dealers suben sus quotes para no quedar arbitrables, retiran sell liquidity propia y pueden comprar las limits de sus clientes mientras distribuyen inventario detrás del ask. Stops y nuevas market orders añaden follow-through. [VID-M2020: Session 6 @ 00:23:59–00:31:16]

### 1.3 Exhaustion y máximo skew direccional

- A medida que se completan las compras agresivas, queda cada vez menos buy volume y una distribución relativamente más gruesa de sell liquidity. Ese finish es la condición de exhaustion. [VID-M2020: Session 6 @ 00:13:06–00:16:10]
- EM sitúa ahí el mayor skew direccional: un lado se ha secado y el contrario conserva liquidez; por eso un volumen opuesto ligero puede devolver precio hacia el core. No significa que se conozca cuál será la siguiente market order. [VID-M2020: Session 6 @ 00:37:11–00:39:58]

## 2. Los cinco eventos del price swing

EM los enumera literalmente así:

1. “**First price event obviously is the volume shot**”.
2. “**Second event is price obviously runs**”.
3. “**Third event is exhaustion**”.
4. “**Fourth event is the shift**”.
5. “**Fifth event is the ... fill, basically**”.

[VID-M2020: Session 6 @ 00:21:43–00:22:16]

**Aclaración de trazabilidad:** el origin/core es el lugar desde el que arranca el proceso y al que puede volver el fill; EM no lo incluye como evento número 1. El whiteboard final vuelve a representar la secuencia con números, dealer schematic y swing. [VID-M2020: Session 6 @ 01:22:32]

## 3. Fractalidad y grados relativos de ineficiencia

- El mismo proceso origin→pop→fill aparece en cualquier timeframe y con recorridos de 5, 60 o miles de pips. El LTF/tick chart funciona como “microscope” para timing, selección, avoidance y lectura de strength dentro del swing mayor. [VID-M2020: Session 6 @ 00:31:17–00:33:22]
- Un swing amplio aparentemente fino puede estar compuesto por ciclos repetidos de sideways→pop→drawback. Sus pockets internos son residual liquidity; el origin/core sigue siendo el área relativamente más gruesa. [VID-M2020: Session 6 @ 00:34:22–00:36:48]
- La ineficiencia admite **grados relativos**. Dos legs pueden ser finas, pero es más ineficiente la que deja menos/débil residual liquidity. La comparación se hace por densidad de liquidez residual, no por tamaño de vela aislado. [VID-M2020: Session 6 @ 00:35:55–00:37:07]
- El esquema mostrado resume: el buy flow se va llenando, bids/buys se secan, quedan “**micro gaps of liquidity / thin residual liquidity aka inefficient move**”, cambia el momentum y el precio “**bleeds back to base liquidity / point of origin**”. [VID-M2020: Session 6 @ 00:32:14]

## 4. Execution algorithms y forma de la extensión

### 4.1 Por qué se trocea una orden grande

- Una orden institucional grande no se ejecuta de una vez: revelaría tamaño/intención, movería el mercado contra el ejecutor y empeoraría el precio medio. Un standalone limit grande también delataría al comprador absorbente cuando ventas repetidas no consiguen bajar el precio. [VID-M2020: Session 6 @ 00:52:04–00:55:18]
- El execution algorithm divide la parent order en child slices y puede parametrizar maximum price/slippage, start/end time, pool interno o externo y estilo aggressive/neutral/passive. [VID-M2020: Session 6 @ 00:55:18–00:57:18] [VID-M2020: Session 6 @ 01:16:22–01:21:18]

### 4.2 Aggressive, neutral y passive

- **Aggressive:** child limits relativamente grandes dentro o muy cerca del spread. La liquidez persigue el precio y lo sostiene; el fill de la extensión puede quedar postergado hasta que se complete, pause/cancele la orden o alcance su limit price. [VID-M2020: Session 6 @ 00:57:34–01:00:00]
- EM llama “**stop pop**” a una morfología del ejemplo: pullbacks finos y nuevo pop bajo chasing liquidity. La usa descriptivamente; no define un setup, entrada, stop ni gestión. [VID-M2020: Session 6 @ 00:58:53–00:59:00]
- **Passive:** child orders pequeñas y más profundas, próximas al core; tolera drawbacks mayores para mejorar execution cost. **Neutral:** trabaja más cerca del top of book y puede producir una estructura escalonada intermedia. [VID-M2020: Session 6 @ 01:00:06–01:04:44]
- Una misma necesidad de ejecución puede producir continuación extremadamente fina, stair-step relativamente estable o fill profundo según el estilo y las condiciones. Por eso detectar ineficiencia no implica fill inmediato. [VID-M2020: Session 6 @ 01:20:26–01:22:55]

### 4.3 Qué sí y qué no permite inferir el chart

- EM dice que las condiciones del algoritmo terminan reflejándose en precio. La sesión ofrece morfologías compatibles, pero no un umbral para distinguirlas en vivo ni una señal inequívoca de que la parent order ha terminado. [VID-M2020: Session 6 @ 01:20:26–01:22:55]
- **Avance, no cierre:** la densidad de residual liquidity ayuda a comparar tradeable vs non-tradeable PI; y el estado de ejecución ayuda a explicar cuándo se retrasa un fill. Faltan trigger, invalidación, timing y tasa.

## 5. Material adicional mostrado

- La ficha visual de HSBC describe floating iceberg, slicing, start/end time, optional limit price, elección de liquidity pool y estilos passive/neutral/aggressive. Sirve como corroboración del vocabulario de ejecución, pero su contenido ya está destilado como `[PAPER: HSBC FX LS]`; no se atribuye a EM. [VID-M2020: Session 6 @ 01:16:22–01:21:18]
- `Price chasing mechanism 2.png` formula self-similarity y el retorno a point of origin. Es material mostrado por EM, pero la imagen por sí sola no aporta un contrato de trade. [VID-M2020: Session 6 @ 00:32:14]

## 6. Trades y setups

- **No hay trade real cerrado.** Los charts son ejemplos explicativos; no se especifican entrada, invalidación, gestión y resolución.
- `Stop pop` es una etiqueta morfológica, no un setup formal.
- No procede añadir ni modificar setups o trade examples.

## 7. Caza prioritaria — resultado individual

| Ítem | Resultado en Session 6 |
|---|---|
| CPS como setup | Ausente. |
| SWE / washed shelf | Ausente; no hay wash shelf-specific. |
| Washed IV/CPL parameters | Ausente. |
| Template formal de 4 apexes | Ausente. |
| Gestión dentro de apex | Ausente. |
| Poke past the low del OP | Ausente. |
| Responsive vs market-state-dependent | Ausente. |
| YO/WO/MO | `MO` es visible en un chart, pero EM no lo comenta ni da reglas: coincidencia visual, no evidencia operativa. [VID-M2020: Session 6 @ 00:35:14] |
| Momentum trade / trade models | Ausente. |
| Tradeable vs non-tradeable PI | **Avance cualitativo:** comparar densidad/cantidad de residual liquidity y estado de ejecución; sin clasificación cerrada. |
| Extensión suficiente / timing del fill | **Avance fuerte:** el fill puede retrasarse mientras el execution algo siga activo y la liquidez persiga precio; sin threshold ni timing exacto. |
| Fractal pushing | Ausente. |
| HOTW | Ausente. |
| Transfer of liquidity | Ausente en la revisión completa 00:00:00–01:24:21. |

## 8. Límites

- Las cadenas dealer/venue, la comparación FX–Dow y las consecuencias de fragmentación son afirmaciones pedagógicas de EM; esta extracción no las completa con teoría externa.
- La sesión no prueba probabilidades ni frecuencia de fill, response o reversal.
- `Origin/core`, los cinco eventos y los estilos de ejecución son capas distintas: no convertir su secuencia descriptiva en trigger mecánico.
- La presencia visual de `MO` no permite derivar reglas para monthly/weekly/yearly opens.
