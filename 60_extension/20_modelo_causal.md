# Modelo causal del movimiento del precio — aislado del corpus

> **Capa de extensión — material de trabajo, NO doctrina nueva.** Todo lo afirmado aquí procede de v1 y de los extractos, con cita; este documento solo REORGANIZA el modelo causal que el corpus ya contiene, separándolo de la operativa (setups/gestión). v1 no se toca. Donde falta un eslabón se marca **ESLABÓN AUSENTE**, no se completa. Sin traducción a cripto ni propuestas de medida.
>
> Autor: proyecto (sesión 23). Fecha: 2026-08-16.
>
> Convención de respaldo externo: los eslabones corroborados por las cinco fuentes externas del corpus se marcan `⟨EXT: Stanford/EBS⟩` `⟨EXT: Farmer⟩` `⟨EXT: Oomen⟩` `⟨EXT: BoC⟩` `⟨EXT: HSBC LS⟩`. Todo eslabón sin marca es afirmación de EM sin corroboración externa en el repo.

---

## 1. Variables del modelo

### 1.1 El eje crítico: observable vs inferida

EM opera GBPUSD spot **OTC**: no hay libro central, el volumen fiable no existe ("**Cus FX there's no real volume data that's reliable**" [DISCORD: Disc 60, 63]) y la mayor parte de la liquidez es latente ("**most liquidity is hidden**" [DISCORD: Disc 63]). El propio método lo asume: "**you don't need volume data to see what's going on — it's present in the price**" [DISCORD: Disc 24]. Consecuencia estructural del modelo: **casi todas las variables causales son latentes y se infieren desde el precio**; las observables directas son un puñado.

| Variable | Observable / Inferida (en el entorno de EM) |
|---|---|
| Precio (anatomía, estructura) | **Observable** — es el único sensor primario |
| Tick rate / tempo de impresión | **Observable** (plataforma) |
| Volatilidad | **Observable** (derivada del precio) |
| Spread (el propio feed) | **Observable con reservas** — "the spread and price feed might be fake" en retail [DISCORD: Disc 37] |
| Slippage / rechazos propios | **Observable** solo vía ejecución propia |
| Hora/sesión, calendario de datos | **Observable** (exógena) |
| Profundidad del libro | **Inferida** en FX (quotes fragmentadas); observable en exchange (ES/futuros) |
| Market-to-limit-order ratio | **Inferida** del desplazamiento; observada una vez en DOM de ES [IMG-TWIT: Bid Void] |
| Skewed liquidity (distribución de limits) | **Inferida** |
| Liquidez disponible vs consumida (drain) | **Inferida** (grabs repetidos, deep tests, respuesta menguante) |
| Liquidez latente + conversion rate | **Inferida por definición** — se revela solo al convertirse |
| Volumen (market orders) | **Inferido** (no hay dato fiable en FX; proxy: tick rate + desplazamiento) |
| Urgencia | **Inferida** (limits persiguiendo precio) |
| Autocorrelación de flujo / metaorders | **Inferida** (drift persistente, "one big order all day") |
| Estilo del execution algorithm | **Inferido** de la morfología (fino / stair-step / drawback profundo) |
| Inventario de LPs, warehousing | **Inobservable** — mecanismo explicativo puro |
| Last look / rechazo, adverse selection | **Inobservable** salvo en ejecución propia; mecanismo explicativo |
| Clasificación del flujo (informed/uninformed/toxic) | **Inobservable** — privada de los dealers |
| Internalización, fragmentación | **Inobservable** — hecho estructural, no señal |
| Stops acumulados | **Inferidos** por ubicación (H/L, past shelf) |
| Sentimiento / macro | Observable como narrativa; su efecto sobre liquidez, **inferido** |
| **Estado de liquidez** (variable maestra) | **Inferida** — "price reflects the state of liquidity" es el axioma que permite inferirla |

La implicación epistémica —que el corpus no formula pero se sigue de la tabla— es que el modelo es **un modelo de variables latentes con un solo canal de observación (el precio)**: toda validación empírica de fase 2 hereda este cuello de botella. [INFERENCIA]

### 1.2 Fichas de variables

#### Estado de liquidez (variable maestra)
- **Sinónimos:** state of liquidity, liquidity state, liquidity landscape.
- **Definición:** "**price is always reflecting state of liquidity and its never a constant. All price movement can be explained when viewed through this prism. And each state has relative characteristics**" [DISCORD: Disc 6]; formulación de principio: "there's a principle... that **price reflects state of liquidity**" [VID-M2020: Session 3 @ 00:18:28–00:21:24].
- **Observable/inferida:** inferida — se lee en estructura, distancia, ritmo y tick rate [VID-M2020: Session 3 @ 00:18:28–00:21:24].
- **Qué la cambia:** retirada/repoblación de limits, consumo por market orders, eventos, sesión, conversión de latente. "Price environments are changing relentlessly" [VID-M2020: Session 13 @ 00:23:56–00:25:47].
- **Sobre qué actúa:** es el estado del que TODAS las demás lecturas del método (niveles, fases, gestión) son funciones.

#### Market-to-limit-order ratio
- **Sinónimos:** ratio market/limit; "the only absolute".
- **Definición:** si las market orders superan las limits disponibles en una dirección, consumen niveles y desplazan el best price [VID-M2020: Session 2 @ 00:26:04–00:33:35]. "There's only one absolute: **market to limit order ratio moves price**" [DISCORD: Disc 42, 43, 45].
- **Observable/inferida:** inferida en FX; observada directamente una vez en DOM de ES ("more market buying than selling and price still went lower as a result of bid void, thick sell limits") [IMG-TWIT: Bid Void].
- **Qué lo hace superar 1:** surge relativo de market orders en un lado [PDF: The Price Run p.7] o adelgazamiento del lado pasivo (retirada, drain).
- **Actúa sobre:** desplazamiento del precio (la única causa transaccional directa), volatilidad.

#### Profundidad del libro (depth)
- **Sinónimos:** depth, limit depth, fricción.
- **Definición:** limits pasivas = liquidez/fricción; "limit orders are friction. Market orders are consumption" [DISCORD: Disc 60, 63]. Es lo que los LPs observan: "it's the **depth of the book + volatility + spread** that's what they're observing" [DISCORD: Disc 18, 19, 20].
- **Observable/inferida:** inferida en FX OTC (quotes fragmentadas de dealers ≠ libro común [VID-M2020: Session 1 @ 00:10:01–00:12:17]); parcialmente observable en exchange, pero "displayed liquidity no es compromiso" (spoofing/cancelación) [VID-M2020: Session 4 @ 00:25:14–00:27:28].
- **Qué la sube/baja:** repoblación por LPs y latente convertida (sube); consumo, retirada defensiva, last look, eventos (baja).
- **Actúa sobre:** ratio M/L, volatilidad, distancia por unidad de volumen.

#### Liquidez disponible vs consumida (drain)
- **Sinónimos:** drained, washed, "finite, quantitative".
- **Definición:** la liquidez de una base es stock finito: "The more we test the level, the weaker it gets — **the liquidity is being drained (finite, quantitative)**" [VID-M2020: Session 13 @ 01:03:29–01:05:24].
- **Observable/inferida:** inferida — repeated grabs, deep tests, cada feed empuja menos [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50].
- **Qué la consume:** tests repetidos/profundos, pickup del top, pokes. **Qué la repone:** ESLABÓN AUSENTE — el corpus documenta reposición del lado débil tras días ("weak side of book is replenished" [IMG-MIET: Tweet 4]) pero no da regla de cuándo/cómo una base drenada se repuebla.
- **Actúa sobre:** capacidad de respuesta del nivel, sostenimiento del midflow.

#### Liquidez visible vs latente + conversion rate
- **Sinónimos:** latent liquidity, hidden liquidity, real orderbook vs visible orderbook.
- **Definición:** "traders hide orders to limit information leakage... only reveal after they've been clipped or as price approaches levels — **conversion rate**" [DISCORD: Disc 21, 21.1]. "**The rate the latent liquidity converts into orders. If it doesn't... you have an open book**" [DISCORD: Disc 64, 65].
- **Observable/inferida:** latente = inobservable por definición; la conversión se infiere ex post (absorción vs open book).
- **Qué mueve el rate:** "directly linked to **conviction/certainty/willingness to transact**"; se frena por "uncertainty usually" [DISCORD: Disc 64, 65].
- **Actúa sobre:** si un nivel absorbe o deja pasar; movimientos de largo plazo ("long term moves are functions of slower liquidity aka **latent distribution**" [DISCORD: Disc 20]); comportamiento de LPs.

#### Fragmentación de liquidez
- **Definición:** liquidez repartida entre venues/dealers con price discovery interno ("most price discovery happens internally with each LP now → liquidity distributed unequally → **prices spike out on less volume than they should**") [DISCORD: Disc 29, 30, 31, 32]; misma liquidez duplicada entre ECNs (phantom liquidity) [IMG-TWIT: Screenshot_12]. En movimiento: "if it's being fragmented in one direction, **what's left behind is exposed**" [IMG-MIET: Tweet Fragmented Lq 1-2].
- **Observable/inferida:** hecho estructural inobservable; sus efectos (spikes con poco volumen) se infieren.
- **Actúa sobre:** volatilidad, tamaño de overshoots, vulnerabilidad de moves one-sided al fade.

#### Spread
- **Definición/rol:** coste de la urgencia y palanca defensiva de LPs — "widen spreads & their pricing engines start moving prices to avoid being clipped" [PDF: The Price Run p.1, p.8]; en eventos amplían tanto que el mercado sigue prácticamente ilíquido [DISCORD: Disc 100–101].
- **Observable/inferida:** observable en el feed propio, con la reserva retail [DISCORD: Disc 37].
- **Qué lo ensancha:** flujo informado, eventos, inventory risk. **Actúa sobre:** coste de ejecución, freno/amplificación de runs.

#### Volatilidad
- **Definición:** variable continua y dinámica, no régimen binario: "**volatility always shifting. It's dynamic**" [IMG-TWIT: Volatility]; lectura inversa: "**contraction = stable liquidity**" [IMG-TWIT: Volatility 2].
- **Observable/inferida:** observable (del precio).
- **Qué la sube:** falta de liquidez disponible (ver cadena 4). **Actúa sobre:** es OUTPUT del modelo, no causa — pero realimenta el comportamiento de LPs (la observan para cotizar [DISCORD: Disc 18–20]).

#### Volumen (market orders) — y su no-identidad con liquidez
- **Definición:** "`volume` = market orders" [VID-M2020: Session 7 @ 00:39:56–00:40:26]. Axioma: "**liquidity =/= volume**" [IMG-TWIT: Screenshot_7]; un seller enorme puede ser absorbido sin mover precio y un buyer menor barrer un ask fino [VID-M2020: Session 2 @ 00:33:35–00:38:11]. Puede haber volumen enorme y entrega ineficiente: lo no-transaccionado en medio es la ineficiencia [DISCORD: Disc 55, 56].
- **Observable/inferida:** inferido en FX (sin dato fiable); proxy: tick rate y desplazamiento.
- **Comportamiento propio:** variable, no constante (VVF): sube en shots y se contrae — "After any shot of high volume, **volume stabilizes. All the time**" [VID-M2020: Session 13 @ 00:46:21–00:46:39].
- **Actúa sobre:** consumo de profundidad (numerador del ratio M/L).

#### Tick rate / tempo de impresión
- **Definición:** la fase parabólica no es forma de vela sino tempo: "flash, flash, flash", "crazy fast" [VID-M2020: Session 4 @ 00:00:00–00:01:31]; el LLS tiene menor tick frequency [PDF: Low Liquidity State p.1].
- **Observable/inferida:** observable — uno de los pocos sensores directos además del precio.
- **Actúa sobre:** diagnóstico de fase (parabólica, LLS), inferencia de volumen.

#### Inventario de LPs / warehousing
- **Definición:** posición que el dealer acumula al dar contrapartida; puede mantener, casar o cubrir [VID-M2020: Session 1 @ 00:02:38–00:03:19]. **Warehousing:** "compound the move" almacenando inventario (estabilizar offers mientras los bids empujan) y/o ensanchando spreads [IMG-MIET: Vol is a F of Av Liq 1, 3] [IMG-TWIT: EMTRADES]. Tras un run "might have excess inventory... so it might have to unload by aggressively skewing bid/ask or quoting one-directionally" [DISCORD: stop cascades, Disc Misc].
- **Observable/inferida:** inobservable — mecanismo explicativo puro.
- **Qué lo mueve:** client orderflow ("LPs primarily base inventory decisions on client orderflow" [DISCORD: Disc 100–101]).
- **Actúa sobre:** retirada/skew de quotes, descargas agresivas, hot potato → volatilidad.

#### Last look / rechazo
- **Definición:** opción del dealer OTC de rechazar/re-cotizar una operación adversa; el quote no es limit firme [VID-M2020: Session 2 @ 01:13:13–01:17:08]. En exhaustion: "they'll reject it and re-quote at a higher price — **so there's absolutely no sell liquidity at the point of exhaustion**" [VID-M2020: Session 12 @ 00:58:42–01:10:33]. ⟨EXT: Oomen⟩ documenta reject rates por last look en agregadores [IMG-TWIT: Screenshot_8].
- **Observable/inferida:** inobservable salvo en la ejecución propia (rejects/slippage).
- **Actúa sobre:** evaporación de liquidez en extremos, estiramiento del run, integridad del stop.

#### Adverse selection
- **Definición:** riesgo del LP de "getting picked off and filling informed traders, **which leads to toxic inventory**" [DISCORD: stop cascades, Disc Misc]; pasado el shelf la liquidez se retira algorítmicamente para evitarla [VID-M2020: Session 12 @ 00:58:42–01:10:33]. ⟨EXT: BoC⟩: "LPs know more about price than orders coming in + have capabilities to exploit that" [IMG-TWIT: Screenshot_2]. ⟨EXT: Oomen⟩ (winner's curse en agregadores).
- **Observable/inferida:** inobservable — mecanismo explicativo.
- **Actúa sobre:** retirada de quotes, spreads, la ineficiencia misma ("el precio se estira más de lo que la información justifica" [VID-M2020: Session 12 @ 00:58:42–01:10:33]).

#### Clasificación del flujo: informed / uninformed / toxic
- **Definición:** "flow from clients is sometimes categorised as **toxic, informed or uninformed** — depending on who it's coming from it can be assumed that the flow is toxic before it's even fulfilled" [IMG-TWIT: Slahzer]. "**It matters who the market order is coming from** — if from an informed trader, market impact likely higher" [DISCORD: Disc 14, 17.1].
- **Observable/inferida:** inobservable — clasificación privada de los dealers vía sus redes internas [DISCORD: Disc 100–101].
- **Actúa sobre:** impacto de mercado por unidad de flujo, internalización vs cobertura, spreads recibidos.

#### Metaorders / order splitting
- **Sinónimos:** parent order, chunked order, "slow but larger liquidity".
- **Definición:** orden institucional grande troceada y ejecutada en el tiempo [IMG-MIET: Gold Ranges 5.1]; "**Most big traders are passive** — they'll chunk out a big order and it'll get filled over several hours... **THAT is more significant than pretty much all other traders**" [DISCORD: Disc 13]. ⟨EXT: HSBC LS⟩: "splitting the total order size into smaller slices scaled to current market liquidity" [PAPER: HSBC FX LS].
- **Observable/inferida:** inferida — del drift persistente: "**autocorrelation in flows is often one big order**" [DISCORD: Disc 47, 48, 50, 51].
- **Actúa sobre:** duración/forma del run (drift vs spike), autocorrelación, sostenimiento de extensiones sin fill.

#### Execution algorithms (estilo de ejecución)
- **Definición:** la parent order se ejecuta con parámetros (max price/slippage, ventana, pool, estilo `aggressive/neutral/passive`) [VID-M2020: Session 6 @ 00:52:04–00:57:18]. ⟨EXT: HSBC LS⟩ (estilos Passive/Neutral/Aggressive documentados) [PAPER: HSBC FX LS].
- **Observable/inferida:** inferido de la morfología: agresivo → run fino sostenido; neutral → stair-step; pasivo → drawbacks profundos [VID-M2020: Session 6 @ 00:57:34–01:04:44]. Sin trigger cerrado para identificar estilo ni final de la parent order [VID-M2020: Session 6 @ 01:20:26–01:22:55].
- **Actúa sobre:** timing del fill (mientras siga activo, la extensión puede no llenar), forma del leg.

#### Fast money vs slow/latent liquidity
- **Definición:** fast = HFTs, PTFs, LPs — "se vuelve aversa en los surges y dispersa la liquidez" [IMG-MIET: Gold Ranges 1.0]; slow = buyside/macro construyendo posición en el tiempo. "**Fast money isn't relevant on higher timeframes because they don't operate there**" [DISCORD: Disc 18, 19, 20].
- **Observable/inferida:** inferida; el reparto por TF es doctrinal, no medido.
- **Actúa sobre:** QUÉ mecanismo gobierna cada timeframe (ver cadena 8).

#### Autocorrelación de flujo
- **Definición:** el flujo HTF llega correlacionado consigo mismo ("HTF = autocorrelated flow" [DISCORD: Disc 18, 19, 20]); un día entero de drift = "they've been filling one big fuckoff order all day" [DISCORD: Disc 47–51].
- **Observable/inferida:** inferida del carácter del movimiento (drift que no llena).
- **Actúa sobre:** persistencia direccional, expectativa de continuación ("id expect bids to push it again tomorrow, at least try in the morning, same time" [DISCORD: Disc 51]).

#### Urgencia
- **Definición:** disposición a pagar por ejecutar YA. Market orders = time-sensitive [VID-M2020: Session 2 @ 00:23:14–00:24:44]; urgencia pasiva = "how aggressively it chases price: price moves up a hundred pips, **bids populate the book up there — thats urgency**" [DISCORD: Disc 9.1, 8].
- **Observable/inferida:** inferida (limits persiguiendo el precio; grinds sostenidos).
- **Actúa sobre:** sostenimiento de grinds ("price only sustains a grind **if theres urgency** — market orders will always taper off" [DISCORD: Disc 9.1]), slippage aceptado.

#### Stops (combustible secundario)
- **Definición:** órdenes acumuladas tras H/L y shelfs que agravan el surge al saltar [PDF: Liquidity Void p.6]. Matiz doctrinal explícito: "price movement in fast markets is **largely influenced by fragmenting liquidity rather than stops**. You can trigger stops but if some spec has large bids there its likely LP will take on the risk and deal it off the spread" [DISCORD: Disc 2]. En FX los LPs pueden absorber el flujo tóxico del run — "**Less so stop cascades**" [DISCORD: stop cascades, Disc Misc].
- **Observable/inferida:** inferidos por ubicación (distinct levels).
- **Actúa sobre:** amplificación puntual de runs; NUNCA como mecanismo primario ni intencional (anti stop-hunt: "There's no such thing as fake highs" [DISCORD: Disc 42, 43, 45]).

#### Internalización
- **Definición:** el dealer casa flujo dentro de su clientela y cubre solo el neto; el volumen retail no llega al mercado [VID-M2020: Session 1 @ 00:04:36–00:05:34] [VID-M2020: Session 14 @ 00:08:43–00:09:05]. Oculta tamaño/dirección (menos leakage) [VID-M2020: Session 3 @ 01:17:13–01:18:40].
- **Observable/inferida:** inobservable — estructural.
- **Actúa sobre:** cuánto flujo real toca el interdealer, fragmentación del price discovery, volatilidad histórica [DISCORD: Disc 29–32].

#### Sentimiento / macro (exógena)
- **Definición/rol:** afecta al estado de liquidez de la divisa "consistently. But not constantly. **And that's where shorter term price behaviours come into play**" [IMG-TWIT: Liquidity Providers 1-2]. Sentimiento ≠ volumen: el precio puede correr contra sentimiento por sell liquidity débil [PDF: The Price Run p.4].
- **Observable/inferida:** la narrativa es observable; su efecto sobre la liquidez, inferido.
- **Actúa sobre:** distribución latente HTF, dirección "consistente"; NO sobre la volatilidad corta ("Shorter term volatility is almost all due to liquidity dynamics" [IMG-TWIT: Liquidity Providers 1-2]).

#### Eventos / catalizadores (exógena)
- **Definición/rol:** ante datos/CB speak la liquidez se aleja del precio/TOB → cualquier peso pequeño causa spike ineficiente [PDF: Liquidity Void p.11]; un catalizador de calibre puede suspender el fade ("emergency cut = liquidity disappearing almost straight away **and it doesn't have to reappear for a while**" [IMG-TWIT: Emergency Cut]).
- **Observable/inferida:** el calendario es observable; la magnitud del efecto sobre liquidez, inferida ("long as you get the significance of the catalyst on available liquidity" [IMG-TWIT: Emergency Cut]).
- **Actúa sobre:** retirada de liquidez, régimen de fade/chase, riesgo de cola (stops ejecutados lejos) [VID-M2020: Session 13 @ 00:38:40–00:43:29].

#### Hora del día / sesión (exógena)
- **Definición/rol:** la liquidez se retira por horario (fin de día, Asia, pre-datos) formando LLS [PDF: Low Liquidity State p.1, p.9]; ciclo intradía: "Asia LLS → LPs abren libros en London open → surge" [IMG-MIET: Vol is a F of Av Liq 1, 3].
- **Observable/inferida:** observable.
- **Actúa sobre:** estado de liquidez base, dónde/cuándo esperar runs y fills (claims CL-35/36).

**Recuento: 23 variables** (1 maestra + 22). De ellas, **observables directas: 5** (precio, tick rate, volatilidad, spread-con-reservas, ejecución propia) más 3 exógenas de calendario; **todo lo demás es inferido o inobservable**.

---

## 2. Cadenas causales

Cada cadena como secuencia explícita; cita en cada eslabón; `⟨EXT⟩` = respaldo externo; sin marca = afirmación de EM.

### C1 — Por qué existe el price run (surge → respuesta LP → chasing → overshoot → vacío)

1. Estado previo: volumen bajo y estable (LLS); basta un surge **relativo** — "the 'increase' is relative... just more than the volume keeping price stable" [PDF: The Price Run p.7, p.9].
2. El flujo entrante consume un lado; un LP adelanta sus quotes para llenar slices de una orden grande [VID-M2020: Session 5 @ 01:42:44–01:59:38]. ⟨EXT: HSBC LS⟩ corrobora el troceo "scaled to current market liquidity" y los liquidity-seeking algos que "track the market until the whole order is executed" [PAPER: HSBC FX LS].
3. Los demás LPs responden en cadena (protección anti-arbitraje): ensanchan spreads y sus pricing engines suben precios [PDF: The Price Run p.1, p.8]. **Este eslabón —el price-chasing defensivo de los pricing engines— NO está documentado por ninguna fuente externa del repo** (el paper HSBC cubre el lado cliente, no el defensivo) [PAPER: HSBC FX LS, contraste].
4. Los flujos "persiguen" las quotes y toman precios peores [PDF: The Price Run p.8]; variante latencia: fast liquidity retira/toma offers delante del ejecutor lento y se las revende más caras [VID-M2020: Session 4 @ 00:29:50–00:33:55].
5. Resultado: movimiento fino que **sobrepasa** (overshoot) — "a dislocation from its true value" (= área previa de matching, no fair value) [VID-M2020: Session 4 @ 00:41:37–00:46:55] — y deja **vacío de liquidez** detrás [PDF: The Price Run p.1, p.8].
6. Sesgo direccional del run: hacia el lado con menos profundidad pasiva ⟨EXT: Stanford/EBS⟩ ("price goes to the weaker side of bid/ask depth" [IMG-TWIT: Screenshot_3]).
7. Fin del chasing: orden llena/pausa/cancela, o encuentra liquidez contraria suficiente. No implica drawback automático [VID-M2020: Session 5 @ 01:59:38–02:03:12].

### C2 — El ciclo de 7 pasos anotado en chart real

GBPUSD H4 post-COVID, numerado por EM [IMG-TWIT: EMTRADES] (toda la cadena de una sola fuente; sin respaldo externo):

1. Buy limit inventory (base).
2. Compra agresiva a mercado hacia área débil de offers; los LPs pueden "compound the move" por **warehousing** (estabilizar offers mientras los bids empujan) y/o ensanchar spreads.
3. El thin move deja **bid vacuum** detrás y toca residual sell liquidity — "exposing price to move lower even on light selling".
4. **Reload on bids** sobre el techo del inventario; reprecio al alza que "opens up the book".
5. Surge de venta, bids desaparecen, reprecio agresivo de vuelta al bid inventory dejando **offer vacuum**.
6. Reload en el inventario, la venta se seca; "light market buying coupled with offer vacuum = **seamless move higher**".
7. "**Ranges above ranges** as result of limit buys accepting higher prices alongside market buyers pushing, in a broadly weak area of offers."

Matiz agregado por EM: la liquidez one-sided "doesn't mean it's constantly coming in the same direction and same intensity — **it often tapers off**" [IMG-TWIT: EMTRADES].

### C3 — Por qué el precio rebalancea

1. El trabajo de los LPs/algos termina cuando el inventario/orden se llena — "después el precio queda sin soporte" [PDF: The Price Run p.6, p.8].
2. En exhaustion el skew es máximo: el volumen agresivo que empujaba queda mínimo frente a liquidez opuesta más gruesa — poco volumen contrario basta para iniciar el retorno (asimetría condicional, no predicción de la siguiente market order) [VID-M2020: Session 6 @ 00:13:06–00:16:10, 00:37:11–00:39:58].
3. El flujo contrario NATURAL basta: en el extremo exhaustion del continuum "el estado natural de venta basta para rebalancear" [PDF: Liquidity Imbalance continuum p.1]. La existencia permanente de ese flujo natural viene de la demanda two-sided no especulativa de FX [VID-M2020: Session 3 @ 00:52:41–00:54:39].
4. POR la forma ineficiente de la entrega, el precio "sangra" a través del void y rebalancea "to the nearest yet thickest area" / "last point of liquidity" — restricción de microestructura independiente de tendencia/sentimiento [PDF: Liquidity Void p.5, p.12].
5. **Indeterminación declarada (no eslabón ausente): el TIMING.** Un execution algorithm activo puede sostener la extensión sin fill ("ineficiencia no equivale a fill inmediato") [VID-M2020: Session 6 @ 01:20:26–01:22:55]; y "**A move like this doesn't have to [fill]**" [DISCORD: Disc 47–51].
6. **ESLABÓN AUSENTE:** ningún mecanismo del corpus especifica CUÁNTO flujo contrario natural es suficiente ni por qué comparece dentro de un horizonte dado — el corpus lo resuelve empíricamente ("extension almost always fills", CL-20) pero no causalmente.

### C4 — Por qué la volatilidad es función de la liquidez disponible

1. Liquidez = fricción disponible (limits), no volumen cruzado [VID-M2020: Session 2 @ 00:33:35–00:38:11]; axioma "liquidity =/= volume" [IMG-TWIT: Screenshot_7].
2. A menos profundidad, más desplazamiento por unidad de flujo (ratio M/L supera 1 antes) [VID-M2020: Session 2 @ 00:38:11–00:45:17].
3. La retirada de liquidez amplifica: "response functions which evaporate liquidity, even restrict stabilising liquidity from reaching the market" [IMG-TWIT: Screenshot_9]; el LP que reduce sell liquidity estira el run "más allá de la distancia atribuible al impulso inicial" [VID-M2020: Session 3 @ 00:13:17–00:16:26, 00:27:02–00:29:40].
4. Conclusión del principio: "Liquidity (passive & active) is not a constant, volume is variable. Price goes to the weaker, less liquid side" [PDF: The Price Run p.2]. ⟨EXT: Farmer⟩: los drivers de colas pesadas y volatilidad clusterizada "fluctuate because of **changes in the balance between liquidity taking and liquidity provision**... typically more important than the number of transactions or their size" [IMG-TWIT: Screenshot_13].
5. Corolario operativo: "we're trading that volatility. **That volatility is predictable**" [VID-M2020: Session 12 @ 01:11:07–01:11:45] — nótese que lo predicho es la volatilidad/comportamiento, no la dirección a largo plazo.

### C5 — Por qué el precio va al lado más débil

1. La distribución de limits es asimétrica (skewed liquidity): describe profundidad en reposo, no flujo direccional [VID-M2020: Session 3 @ 00:04:05–00:06:09].
2. El lado con menos depth necesita menos volumen para que el ratio M/L supere 1 [VID-M2020: Session 2 @ 00:38:11–00:45:17].
3. Por tanto el movimiento inmediato queda sesgado hacia el lado fino — incluso con MÁS volumen del lado contrario: "you could have more market selling than buying and price still goes up" [DISCORD: Disc 7]; observado en DOM: [IMG-TWIT: Bid Void].
4. ⟨EXT: Stanford/EBS⟩: "how price goes to the weaker side of bid/ask depth — whichever side had the imbalance" [IMG-TWIT: Screenshot_3].
5. Límite declarado: la asimetría máxima "dura muy poco y no es fácil de identificar en vivo" [VID-M2020: Session 2 @ 01:01:24–01:03:09].

### C6 — Mecanismo del shelf: por qué sostiene y por qué falla

Sostiene:
1. El shelf es "the **last inventory** that pushed price to new lows (highs)" [VID-M2020: Session 14 @ 00:09:15] — "bulk of the momentum pushing any single price move, every price swing has one" [PDF: Price Swings Continued p.8].
2. El run "continuously feeds into the nearest shelf, picks liquidity up and continues" [PDF: Price Swings Continued p.8] — el inventario aporta el combustible mientras conserve stock.
3. La liquidez de la base es finita y cuantitativa [VID-M2020: Session 13 @ 01:03:29–01:05:24]; mientras no se consuma, las respuestas contra flujo se absorben (midflow) [PDF: Price Swings Continued p.7].

Falla:
4. Consumo progresivo: repeated grabs, deep tests, top pickup; cada feed empuja menos o necesita penetrar más [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50]. Si el precio alcanza el **bottom**, toda la liquidez de la base se da por consumida [VID-M2020: Session 13 @ 01:03:29–01:05:24].
5. "Until the shelf isn't strong enough to continue supporting the run" [PDF: Price Swings Continued p.8] → break; tras él, los intentos residuales se secan rápido [VID-M2020: Session 11 part 2 @ 01:12:26–01:13:55].
6. La debilidad se confirma en la RESPUESTA, no en la ruptura: "it's confirmed in how price responds off it"; mejor señal: la primera pierna atraviesa de una vez [VID-M2020: Session 12 @ 00:12:22–00:13:04].
7. **ESLABÓN AUSENTE:** no hay umbral cuantitativo de drain (cuántos tests, qué profundidad) ni mecanismo de reposición de una base drenada. El diagnóstico es cualitativo-relacional en todo el corpus.

Sin respaldo externo en ningún eslabón: el shelf es vocabulario chartista de EM sobre el mecanismo de inventario.

### C7 — Mecanismo de exhaustion vía last look

1. El run entra en un extremo; el flujo que llega se percibe como informado/adverso [VID-M2020: Session 12 @ 00:58:42–01:10:33].
2. Los dealers ejercen last look: "they'll reject it and re-quote at a higher price — **so there's absolutely no sell liquidity at the point of exhaustion**" [VID-M2020: Session 12 @ 00:58:42–01:10:33]. ⟨EXT: Oomen⟩ documenta la existencia y mecánica del last look/reject en agregadores [IMG-TWIT: Screenshot_8]; **la LOCALIZACIÓN del efecto en los puntos de exhaustion es afirmación de EM.**
3. Pasado el shelf, la liquidez se retira algorítmicamente para evitar adverse selection [VID-M2020: Session 12 @ 00:58:42–01:10:33]. ⟨EXT: BoC⟩ apoya la asimetría informativa que motiva la retirada [IMG-TWIT: Screenshot_2].
4. Resultado: el precio se estira más de lo que la información justifica = **ineficiencia de mercado** → "pockets of air que poco volumen atraviesa de vuelta" [VID-M2020: Session 12 @ 00:58:42–01:10:33].

### C8 — Por qué el mecanismo CAMBIA por timeframe (y el comportamiento no)

1. "The LP-responding-to-flow dynamic really applies to **intraday/immediate timeframes**" [DISCORD: Disc 18, 19, 20].
2. Motivo: los LPs no cotizan según forecast — "**forecast =/= LP behaviour... i have a 1.50 forecast but the next 5 mins matter to me**... they can't provide liquidity in line with longer-term forecasts because they'll be exposed to huge drawdowns"; observan "depth of the book + volatility + spread" [DISCORD: Disc 18, 19, 20].
3. "**Fast money isn't relevant on higher timeframes because they don't operate there**" [DISCORD: Disc 18, 19, 20].
4. HTF se gobierna por otra pareja de causas: "autocorrelated flow" + "**latent liquidity distribution**" (sentiment/macro models de la liquidez lenta) [DISCORD: Disc 18, 19, 20] — "long term moves are functions of slower liquidity aka latent distribution" [DISCORD: Disc 20].
5. Por qué los niveles HTF pesan más pese al cambio de mecanismo: una vela diaria condensa 24–48h de volumen transaccionado → pockets y liquidez residual mucho mayores [VID-M2020: Session 15 @ 00:07:01–00:10:57]; "higher time frame pulls more liquidity" [VID-M2020: Session 13 @ 00:13:52–00:14:17].
6. Y sin embargo: "**What IS true though: price is fractal and similar behaviours are observed**" [DISCORD: Disc 18]. La causa general que EM da a la fractalidad es conductual: "price reflects traders behaviour — traders repeatedly do the same thing thus price reflects this on all scales" [PDF: Fractals _ Scaling p.13].
7. **ESLABÓN AUSENTE:** el corpus NO explica por qué dos mecanismos distintos (fast money/LP dinámico intradía vs latente/autocorrelado HTF) producen la MISMA anatomía. El eslabón conductual (6) es genérico y no conecta las dos mecánicas. Es el hueco causal más importante del modelo, porque la fractalidad —que justifica trasladar lecturas entre escalas— descansa sobre él.

Sin respaldo externo en (1)–(4); son doctrina Discord de EM.

### C9 — Por qué la liquidez "sigue" al precio y no se "transfiere"

1. Formulación temprana (superada): las core bases sucesivas "transferred down / transferring and passing on the liquidity" [VID-PS: PriceSwing_03 @ 00:07:42–00:08:12] [PRECURSOR: PS → refinado en M2020].
2. Corrección M2020: la liquidez no se transfiere — una orden grande se divide y la liquidez entregada por el algoritmo **follows/chases price** a lo largo de distintos precios; "misnomer" sin negar el comportamiento visual [VID-M2020: Session 10 @ 00:06:17–00:07:24].
3. Mecanismo: las bases sucesivas son EL MISMO interés re-cotizado a precios nuevos (slices de la parent order siguiendo al mercado), no un stock que viaja. ⟨EXT: HSBC LS⟩ corrobora literalmente: slices "passively placed... at different prices... **thereby tracking the market until the whole order is executed**" [PAPER: HSBC FX LS].
4. Registro de crítica: C-001 — [USUARIO] cuestiona "transfer of liquidity" como mecanismo real [91_contradicciones.md]; la corrección del propio EM en (2) converge con la objeción.

### C10 — Por qué la estabilidad es la norma y la dislocación la excepción

1. FX es un conduit: "importers, business, people, buyside for non-spec reasons... a channel to access assets" [DISCORD: Disc 35, 36] — demanda de liquidez two-sided no especulativa permanente [VID-M2020: Session 13 @ 00:43:35–00:45:29].
2. Cultura de minimización de coste/impacto: algos que trocean y ocultan órdenes [VID-M2020: Session 13 @ 00:43:35–00:45:29]. ⟨EXT: HSBC LS⟩ ("minimises footprint in the market as well as probability of adverse selection") [PAPER: HSBC FX LS].
3. Los dealers prefieren no desestabilizar: "they might even keep bids in a stable market to keep capturing the spread" [DISCORD: Disc 14]; estado ideal = casar flujo bilateral capturando spread sin riesgo direccional [VID-M2020: Session 2 @ 01:25:55–01:27:14].
4. "There's more money in the chop": los proveedores filtran las órdenes grandes al mercado de forma que "perpetuates intraday price behaviours & volatility"; "banks make more money executing orders compared to taking speculative positions" [IMG-TWIT: Liquidity Providers 1].
5. La dislocación exige la excepción: surge relativo + retirada/skew de liquidez (cadenas C1/C4); "distortions in liquid markets are repaired quickly creating opportunity" [DISCORD: Disc 85–88].
6. Cierre del modelo completo en una frase: "**market just pings from one pocket of liquidity, through weak spots into the next pocket of thick liq. That's it.**" [IMG-TWIT: Liquidity Providers 1]

---

## 3. Predicciones del modelo

Distinción central: **(a) PREDICTIVA** — dice qué pasará y podría fallar · **(b) EXPLICATIVA** — describe lo ocurrido, no arriesga nada · **(c) DEFINICIONAL** — verdad por construcción del vocabulario.

### 3.1 Las predicciones normalizadas ("Cuando X → más probable Y que Z, horizonte H")

Hallazgo transversal antes de la lista: **el campo H está sistemáticamente vacío en el corpus.** EM declara el timing incognoscible ("Outcome can be anticipated and what it will look like. **But never when it will happen**" [DISCORD: disc 11]), de modo que casi ninguna predicción lleva horizonte — lo que degrada su falsabilidad tal cual están formuladas (una predicción sin horizonte no puede fallar del todo). Donde EM sí acota horizonte se indica.

Del catálogo de claims (v1/30_claims_validables.md) y del resto del corpus:

| # | Cuando se observa X... | ...es más probable Y que Z | Horizonte | Fuente / CL |
|---|---|---|---|---|
| P1 | Shot de volumen alto | estabilización del volumen que continuación del shot | no especificado ("all the time") | CL-24 |
| P2 | Extensión ineficiente hacia un nivel (aun débil, con llegada más débil) | respuesta que atravesarlo sin reacción | inmediato ("initial response") | CL-14, CL-22 |
| P3 | Área washed | no-respuesta que respuesta | no especificado | CL-12 (excepción por modo de llegada: CL-13) |
| P4 | Primer break de midflow/inventario | pausa prolongada que continuación inmediata | "a long while" (sin cifra) | CL-02 |
| P5 | Apex en curso con OP intacto | reversal exitoso que fallo del apex | no especificado | CL-05 (invertido: poke del OP degrada, CL-06) |
| P6 | Liquidez one-sided poblando el libro | precio sostenido aunque las market orders se sequen | mientras dure la población | CL-29 |
| P7 | Imbalance de profundidad | movimiento hacia el lado con menos liquidez pasiva | inmediato, "dura muy poco" | CL-27 · C5 |
| P8 | LLS prolongado | run mayor a la salida, hacia CUALQUIER lado | no especificado | CL-26 + "cuanto más dura el LLS, mayor el movimiento de salida" [IMG: Low Liquidity State p.4] |
| P9 | Sideways tras primer break | pop/parabólica que continuación del sideways | no especificado | CL-03 |
| P10 | Fase parabólica | reversal/shift después que nueva pierna significativa | no especificado | CL-04 |
| P11 | Extensión/vacuum ineficiente | fill que no-fill | **sin horizonte — falsabilidad degradada** | CL-20, CL-21 |
| P12 | Fill de extensión EN TENDENCIA | continuación a nuevos extremos que reversal | no especificado | CL-23 |
| P13 | Primer paso limpio a través de un shelf | continuación que retorno | no especificado | CL-08 |
| P14 | Nivel testeado repetidamente | respuesta menguante que respuesta plena | acumulativo | CL-15 |
| P15 | Poor high/low | trade-through posterior que hold | "more times than not", sin horizonte | CL-18 |
| P16 | Run que NO llena (runs, doesn't fill) | cambio de régimen a ineficiente que reanudación del fill | "first sign" | CL-30 |
| P17 | Drift de metaorden todo el día | continuación al día siguiente, misma franja | ~24h (uno de los pocos horizontes explícitos) | [DISCORD: Disc 51] |
| P18 | Días de flujo one-sided agresivo | secado + reposición del lado débil + chop | días | [IMG-MIET: Tweet 4] |
| P19 | Catalizador de calibre (emergency cut) | continuación chaseable que fade | "for a while" | [IMG-TWIT: Emergency Cut] |
| P20 | Shift sin midflow posterior | tesis inválida (reevaluar) que continuación tardía | expectativa inmediata | "Midflow is an EXPECTATION" [PDF: Price Swings Continued p.7] |
| P21 | Precio separándose del inventario consumido (CPL) | fade atravesando la zona consumida que sostenimiento de la pierna | no especificado | [IMG: CLP/ED6JtkLXsAEu4X4.png] |
| P22 | Sell inventory contrario intacto en el camino | wash/deal-off previo antes de run alcista que run directo | secuencial | [IMG-TWIT: EC2rNRGX4AE0r9f] |
| P23 | Spike event-driven SIN sorpresa grande vs consenso | rebalance que continuación (con la excepción explícita de sorpresa grande) | no especificado | [PDF: Liquidity Void p.11] |
| P24 | Primer run tras Asia | secado/fade que continuación | sesión | CL-36 (también CL-35) |
| P25 | Distorsión de liquidez en mercado líquido | reparación rápida que persistencia | "quickly" | [DISCORD: Disc 80, 84–88] |

### 3.2 Clasificación (a)/(b)/(c) de los 38 claims de v1

| CL | Tipo | Nota de rigor |
|---|---|---|
| CL-01 | (a)− | condicionado a "successful swings" — survivorship en la formulación |
| CL-02 | (a) | |
| CL-03 | (a) | |
| CL-04 | (a) | |
| CL-05 | (a)− | condicionado al resultado ("successful apex"); usable solo invertido (OP roto → apex degradado) |
| CL-06 | (a) | |
| CL-07 | (a) | |
| CL-08 | (a)− | mitad diagnóstica ("confirmed in response" roza lo definicional), mitad predictiva (paso limpio → continuación) |
| CL-09 | (a) | |
| CL-10 | (a) | |
| CL-11 | (a) | único junto a CL-16 donde EM pide test |
| CL-12 | (a) | |
| CL-13 | (a) | |
| CL-14 | (a) | |
| CL-15 | (a) | |
| CL-16 | meta | es una TAREA de test, no un claim; la hipótesis implícita (expectancy negativa post-invalidación) sería (a) |
| CL-17 | (a) | |
| CL-18 | (a) | |
| CL-19 | (a) | |
| CL-20 | (a)− | **sin horizonte** — "almost always fills" es infalsable hasta fijar H |
| CL-21 | (a)− | sin horizonte (ídem) |
| CL-22 | (a)− | "response" sin magnitud/horizonte definidos |
| CL-23 | (a) | |
| CL-24 | (a) | informatividad baja (mean-reversion de volumen es propiedad genérica de mercados) — pero medible |
| CL-25 | (a) | depende de definición operativa de "range"; ya marcado NO VALIDADO (q12) |
| CL-26 | (a) | "susceptible" débilmente especificado; magnitud medible |
| CL-27 | (a)− | condicionante (depth) inobservable en FX — testable solo con datos de libro |
| CL-28 | **(c)** | verdad mecánica por construcción (solo cruces mueven el last price); el matiz indirecto ya lo reconoce la fuente |
| CL-29 | (a)− | riesgo de circularidad: la urgencia se infiere DEL grind que se sostiene — necesita medida independiente de urgencia |
| CL-30 | (a) | |
| CL-31 | (a)− | la etiqueta de régimen ("HTF inefficiency") requiere definición operativa previa |
| CL-32 | (a) | |
| CL-33 | (a)− | riesgo de circularidad: el balance se infiere del chop que se predice |
| CL-34 | **(b)** | claim histórico-explicativo (retrodicción sobre ATR); comprobable con datos pero no predice comportamiento futuro |
| CL-35 | (a) | |
| CL-36 | (a) | |
| CL-37 | (a) | |
| CL-38 | meta | claim de FRECUENCIA de aparición de patrones, no predicción condicional X→Y; calibra viabilidad de fase 2 |

### 3.3 Reparto y lectura honesta

**Reparto de los 38 claims: (a) plenas ×24 · (a)− degradadas ×10 · (b) ×1 · (c) ×1 · meta ×2.**

Es decir: **34 de 38 son predictivas** — la mayoría NO resulta (b)/(c). Pero esta cifra exige dos advertencias para no leerla como mejor noticia de lo que es:

1. **Sesgo de construcción del catálogo.** `30_claims_validables.md` se construyó (sesión 20) seleccionando del corpus precisamente lo empíricamente comprobable. El reparto 34/38 mide la calidad de ESE filtro, no la del corpus. **El grueso del corpus es (b) y (c)**: el prisma central — "all price movement can be explained when viewed through this prism" [DISCORD: Disc 6] — es un marco EXPLICATIVO que, como totalidad, no arriesga nada (cualquier movimiento se puede narrar ex post como estado de liquidez); y gran parte del vocabulario (shelf, apex, midflow, washed, core/residual...) es definicional: clasifica lo ocurrido. El valor predictivo del método vive en los 38 claims + las 25 predicciones de 3.1, no en el prisma.
2. **La degradación dominante es el horizonte ausente.** 10 de las 34 predictivas tienen defectos de falsabilidad, y el defecto más repetido (CL-20/21/22 y, de fondo, casi todas) es que EM declara el timing incognoscible por doctrina [DISCORD: disc 11]. Toda operacionalización en fase 2 tendrá que IMPONER horizontes que el corpus no da — y esa imposición será decisión del proyecto, no doctrina de EM.

Cruce con 3.1: las 25 predicciones normalizadas provienen 16 del catálogo CL y 9 de fuera de él (P8 parcial, P17–P23, P25) — el catálogo v1 no agotaba las predicciones del corpus, aunque cubría las principales.

---

## 4. Lo que el modelo NO explica

Reconocido por el propio corpus, con cita:

- **El timing, por principio.** "Cuándo golpea un market order is **entirely unpredictable**... **Outcome can be anticipated and what it will look like. But never when it will happen.**" [DISCORD: disc 11] El modelo predice forma y destino condicional, nunca momento.
- **Las causas específicas, por método.** "**Avoid finding causal and specific reasons for why [the market] does what it does — markets too random and complex. Hence why observing it against a prism of governing principles.**" [DISCORD: Disc 13] Y "**it's always a combo of things. I'm not a fan of causal reduction.**" [DISCORD: Disc 47–51] El modelo renuncia deliberadamente a la atribución causal puntual (quién, por qué): "Trying to predict why someone lifted the offer is futile." [DISCORD: Disc 42, 43, 45]
- **La dirección como forecast.** "Observe, don't predict"; "I shouldn't go into the territory of forecasting" [VID-M2020: Session 14 @ 00:29:44, 00:33:53]; "I don't care where cable is in a month" [VID-M2020: Session 12 @ 01:11:07–01:11:45]. Consecuencia interna: `response ≠ hold ≠ reversal` — el modelo predice la respuesta local, no lo que sigue [VID-M2020: Session 8 @ 00:56:19–00:57:19].
- **El marco de aleatoriedad.** "Distinction between **non-randomness & observable characteristics in something random** — earthquakes are 'random' but there's a measurable & observable impact of one allowing for **anticipation & response**" [IMG-TWIT: Randomness]; "**Something being observable doesn't make it not random**... But WHEN they will diverge is random"; "there's random probability of it happening, but **when it does happen it has repeating characteristics**" [DISCORD: Disc 44]. Corolario metodológico: "You can certainly anticipate things but **Bayesian observation is more important**" [DISCORD: Disc 49]; "**You'll hardly ever predict how price will unfold or trade will unfold accurately**" [DISCORD: Disc 94.1].
- **El límite sub-segundo declarado del edge.** "The market is **efficiently inefficient**": sin edge en escalas sub-segundo (los HFTs ven el precio verdadero antes); "you can't trade breakouts anymore — by the time the breakout is seen on our screen the volatility is finished" [VID-M2020: Session 13 @ 02:06:35–02:07:39].
- **El estado del execution algorithm.** No hay forma de saber desde el chart si la parent order terminó: mientras siga activa, la extensión puede no llenar — sin trigger cerrado para identificar estilo ni final [VID-M2020: Session 6 @ 01:20:26–01:22:55].
- **La liquidez que no se ve.** "**Most liquidity is hidden — you can have seemingly no clear level even though someone's eating it**" [DISCORD: Disc 60, 63]; la latente solo se conoce al convertirse (Disc 64–65). El sensor único (precio) no distingue todos los estados subyacentes.
- **Los eventos con sorpresa grande.** El rebalance post-spike tiene una excepción abierta: "una sorpresa grande vs consenso puede hacer que el precio siga repricing agresivamente un tiempo" — sin criterio de magnitud [PDF: Liquidity Void p.11]; ídem catalizador de calibre [IMG-TWIT: Emergency Cut] ("long as you get the significance of the catalyst" — el juicio de significancia no se especifica).
- **La enumeración completa de estados.** "Each state has relative characteristics, with their own implications, **which you'll have to experience**" [DISCORD: Disc 6]; "theres a whole spectrum of things that happen at highs and lows. **Any single aspect of it on its own is kinda irrelevant**" [DISCORD: Disc 25.1]. El modelo no es exhaustivo ni pretende serlo; remite a exposición.
- **Fuera de alcance por diseño:** valoración fundamental ("**We're not fair value traders**" [DISCORD: Disc 87–88]), mercados no-FX sin adaptación ("Some of you are talking about LPs in equities and others in FX — **they're worlds apart**" [DISCORD: Disc 2]), y sub-mecánica por mercado (gold/WTI con "different tendencies" [DISCORD: Disc 59, 62]).
- Higiene epistémica declarada del propio EM: "**info based on conjecture is the equivalent of false info**" [DISCORD: answers]; contra la sobre-optimización: "**overfitting — overly optimising for a string of data, exposing yourself to change**" [IMG-TWIT/DISCORD: Market randomness].

---

## Resumen estructural

- **23 variables** causales; solo 5 observables directas (+3 exógenas de calendario). Modelo de variables latentes con un único canal de observación: el precio.
- **10 cadenas causales**: 7 completas (C1, C2, C4, C5, C7, C9, C10), 3 con eslabón ausente o indeterminación estructural (C3: suficiencia/comparecencia del flujo contrario; C6: umbral de drain y reposición; C8: por qué mecanismos distintos por TF producen la misma anatomía — el hueco más importante, porque sostiene la fractalidad).
- **Respaldo externo:** Stanford/EBS → lado débil (C5, C1.6); Farmer → volatilidad=f(liquidez) (C4); Oomen → existencia de last look (C7, no su localización en exhaustion); BoC → asimetría informativa del dealer (C7); HSBC LS → troceo/tracking (C1.2, C9.3, C10.2). **Nunca corroborados:** el price-chasing defensivo de los pricing engines (C1.3, el eslabón que genera el overshoot), todo el ciclo de 7 pasos (C2), el mecanismo del shelf (C6) y el reparto de mecanismos por timeframe (C8).
- **Predicciones:** 25 normalizadas; los 38 claims reparten (a)×24 · (a)−×10 · (b)×1 · (c)×1 · meta×2 — mayoría predictiva, PERO el catálogo v1 ya era un filtro de testabilidad (el grueso del corpus es explicativo/definicional) y el horizonte H está sistemáticamente ausente por doctrina.
