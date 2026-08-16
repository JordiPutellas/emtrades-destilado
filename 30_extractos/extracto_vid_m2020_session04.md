# Extracto — M2020 Session 4: parabolic, exhaustion e ineficiencia HFT

> Fuente primaria: `Session 4.mp4` (01:01:05; pantalla fechada 29-sep-2020). Navegación: transcripción `.md/.srt/.json`. Revisados íntegramente la transcripción, los 13 frames indexados y los pasajes de vídeo relevantes para charts, operaciones y esquemas. Las explicaciones históricas e institucionales son afirmaciones de EM, no hechos verificados externamente. Correcciones conservadoras de Whisper: buy liquidity, spoofing, HFT, EBS, prime brokerage y S&P 500/E-mini.

## 1. `Parabolic` = velocidad de ticking, no patrón de velas

- EM compara directamente dos tramos del GBPUSD en chart de ticks: el movimiento ordinario imprime de forma irregular; en la fase parabólica los ticks llegan casi sin pausa, “**flash, flash, flash, flash**”. Su definición aquí es de **tempo/frecuencia**: “**parabolic means, like, crazy fast**”. Rechaza identificarla con morning/evening star o cualquier candlestick pattern. [VID-M2020: Session 4 @ 00:00:00–00:01:31]
- Afirma que solo opera los periodos donde el book está skewed y el comportamiento microestructural crea una oportunidad breve; en ese contexto espera reacción casi inmediata. `Almost instantaneously` describe su edge declarado, no una ley ni un horizonte cuantificado. [VID-M2020: Session 4 @ 00:01:37–00:02:20]
- El gráfico confirma el alcance: tick chart GBPUSD en Dukascopy, con los extremos/movimientos señalados; la vela agregada por sí sola no conserva la cadencia que EM está mostrando. [VID-M2020: Session 4 @ 00:00:05]

## 2. Operar exhaustion/finish point, no acertar dirección

- EM contrasta predecir un destino direccional con operar el **finish/exhaustion point**. Aunque el precio termine continuando hacia el box previsto, sostiene que desde el punto de finish obtiene primero una respuesta local: “**I will always get that initial response**”. Opera ambos lados y dice que no empieza el día con sesgo buy-only/sell-only. Es un claim contextual y comprobable, no una garantía aceptada. [VID-M2020: Session 4 @ 00:02:47–00:03:51]
- Su lectura de los charts es una secuencia repetida: volumen agresivo persigue quotes que se retiran, se estira y se agota; queda un vacuum de liquidez en el recorrido y hace falta menos flujo contrario para devolver el precio al último inventory. Quiere capturar la respuesta, no necesariamente el destino posterior. [VID-M2020: Session 4 @ 00:03:55–00:04:47]
- En el día mostrado enumera varias operaciones capturadas y omitidas. En una el stop planeado era **1,2 pips**, pero por su entrada/ejecución terminó siendo aproximadamente **3 pips**; no da precio de entrada ni resultado final de forma inequívoca. [VID-M2020: Session 4 @ 00:04:48–00:05:04]
- Un long fue stop por entrar “**too early**”. Otro trade no se tomó por una sola razón: “**It didn't reach my line**”. También deja pasar un retorno porque no llega al core/origin marcado. La sesión demuestra disciplina de nivel y el coste de anticiparse, pero no entrega un contrato formal de trigger. [VID-M2020: Session 4 @ 00:05:28–00:06:17]
- Ante el tramo muy fino, EM reconoce que podría responder en varios niveles, pero afirma que el vacuum “**will basically always fill**”. La frase no especifica muestra, plazo, nivel final ni separación entre fill parcial, retorno al origin y reversal. Se conserva para validación junto al `almost always fills` de Session 2. [VID-M2020: Session 4 @ 00:06:17–00:06:33]
- Distingue el entorno estable/eficiente, en el que quiere estar activo, de velas grandes event-driven/headline y de un entorno drift/ineficiente cuya volatilidad cambia constantemente. No convierte `stable` o `event-driven` en setup autónomo. [VID-M2020: Session 4 @ 00:05:23–00:08:59]

## 3. Del customer flow al hot potato

- EM retoma EBS sin añadir un mercado nuevo: un dealer puede asumir parte de una orden cliente y cubrir el resto en EBS. Al hacerlo filtra tamaño/dirección, otros dealers ajustan books y el inventario indeseado pasa entre contrapartes (`hot potato`), encareciendo la ejecución. [VID-M2020: Session 4 @ 00:18:18–00:21:20]
- El mismo leakage puede empezar con una **limit order** cliente: el dealer replica/hedgea una bid en EBS y otros participantes pueden adelantarse a la liquidez visible. El mecanismo relevante es que la gestión del dealer convierte información privada de cliente en cambios observables del book. [VID-M2020: Session 4 @ 00:21:20–00:25:14]

## 4. Liquidez mostrada, spoofing/layering y ventaja de latencia

- EM ilustra **spoofing**: el participante vende primero, muestra después una sell order grande para aparentar supply y la cancela porque nunca tuvo intención de fill. `Layering` es el ejemplo siguiente, con múltiples órdenes distribuidas por el book. Son ejemplos de información estratégica/falsa; no toda order visible se trata como firme. [VID-M2020: Session 4 @ 00:25:14–00:27:28]
- En su ejemplo de latencia, una market buy empieza a consumir una offer; el HFT detecta el fill antes que el resto, compra la liquidez de precios superiores y se la revende al comprador más lento. No crea la orden original, pero aumenta el número de niveles recorridos y el slippage. [VID-M2020: Session 4 @ 00:29:50–00:33:55]
- EM corrige su propio ejemplo de tamaños: el HFT no espera normalmente a comprar cientos de miles de una vez, sino que repite muchas operaciones pequeñas y rápidas. Los importes del diagrama son pedagógicos, no calibración real. [VID-M2020: Session 4 @ 00:37:45–00:38:44]
- Cuando el flujo se vuelve fuertemente unilateral, el fast market maker puede retirar bids y pasar a vender; EM lo vincula con cascadas/flash crashes. La mecánica de retirada es parte del modelo; sus juicios sobre corrupción, regulación, exchanges y firmas HFT quedan como opinión explícita, no como evidencia externa. [VID-M2020: Session 4 @ 00:34:34–00:41:30]

## 5. Definición funcional de ineficiencia/dislocación

- Para EM, la función del mercado es encontrar contraparte. Si la organización o conducta de participantes retira al seller disponible y lo revende más caro, obliga al buyer a recorrer más precio del necesario: esa peor facilitación es la **ineficiencia operativa** cuyo efecto intenta explotar. [VID-M2020: Session 4 @ 00:41:37–00:42:07]
- Separa esta acepción de la **Efficient Market Hypothesis**. Su exposición de EMH es informal y polémica; no se usa como definición académica ni como validación de que el mercado sea batible. [VID-M2020: Session 4 @ 00:42:07–00:43:37]
- En el esquema HFT, la orden original habría podido casar dentro de pocos niveles, pero la retirada/reventa de liquidez estira el precio en un **thinly traded move**. EM lo llama “**a dislocation from its true value**” y lo define funcionalmente: “**price running further than it should**” por el comportamiento de participantes. `True value` aquí significa el área donde buyers y sellers podían casar antes de la distorsión, no valoración fundamental. [VID-M2020: Session 4 @ 00:43:37–00:46:55]
- Su consecuencia operativa: una vez se seca el volumen que impulsa la dislocación, el precio probablemente vuelve hacia donde estaban los buyers/contrapartida. Es expectativa condicional y probabilística; la sesión no define cómo detectar en vivo el último fill de la metaorder ni el timing exacto del drawback. [VID-M2020: Session 4 @ 00:47:18–00:47:48]
- Menciona como segundo significado de ineficiencia el arbitraje entre venues con distintos precios de BTC. Es una analogía distinta de la dislocación intrabook y no aporta una regla nueva para BTC/perpetuos. [VID-M2020: Session 4 @ 00:47:49–00:49:06]

## 6. Prime brokerage y entrada de non-banks en EBS

- Según EM, prime brokerage permitió a clientes non-bank operar bajo las relaciones de crédito/nombre del prime broker. El cambio de acceso a EBS acercó HFT/non-bank market makers al punto de price formation y les permitió explotar updates antes de su redistribución. [VID-M2020: Session 4 @ 00:49:59–00:53:26]
- Con velocidad suficiente podían cotizar spreads más estrechos, gestionar el riesgo más rápido y revender liquidez competitiva, quitando market share a los dealers bancarios; estos respondieron invirtiendo en tecnología. Es historia causal de EM, sin verificación externa de fechas, cuotas o universalidad. [VID-M2020: Session 4 @ 00:53:26–01:01:04]

## 7. Trades, setups y límites

- Los charts muestran líneas/boxes previos, operaciones capturadas, un stop y oportunidades omitidas, pero no permiten asociar de forma completa y no ambigua **entrada + nivel + invalidación + gestión + resolución** a una misma operación. **No crear TE** en `05_trade_examples.md`.
- No aparece setup nuevo ni se amplía S-01–S-09 con un contrato completo. Parabolic, exhaustion, vacuum y core/origin son piezas causales/diagnósticas; en esta sesión faltan trigger reproducible, invalidación estructural y gestión.
- La revisión completa no contiene CPS como setup, SWE/washed shelf, Washed IV/CPL, cuatro variaciones o gestión de apex, OP, responsive levels, YO/WO/MO, momentum trade, fractal pushing ni HOTW. El resultado negativo se consolidará con Sessions 5–6 en la matriz transversal, no se replica en maestros ahora.
- `transfer of liquidity` no aparece ni como término ni como mecanismo; EM usa consumption, withdrawal, repricing, exhaustion, dislocation y drawback. C-001 avanza a ocho sesiones M2020 sin el término. [VID-M2020: Session 4 — revisión completa 00:00:00–01:01:05]
- C-002 no se reabre: spoofing, cancellation y retirada de quotes refuerzan la distinción ya documentada entre book visible y liquidez total/firme; no hay contradicción directa.

## 8. Integración

- `01_principios.md`: dislocación funcional, retirada/reventa de liquidez y reparación tras secado.
- `02_conceptos.md`: definición por tick rate de parabolic e ineficiencia/dislocación.
- `04_proceso.md`: operar comportamiento/finish point, no anticiparse al nivel y separar claims de garantías.
- `90_preguntas_abiertas.md`: claims de respuesta inicial y vacuum fill añadidos a validación.
- `91_contradicciones.md`: C-001 ampliada a ocho sesiones; C-002 permanece cerrada.
- `03_setups.md`, `05_trade_examples.md` y `92_ideas_btc.md`: sin cambios por falta de contrato operativo/TE y por ausencia de consecuencia cross-asset nueva.
