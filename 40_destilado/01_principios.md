# Principios (EMTrades — destilado)

> Marco causal del método. Convenciones de fuentes en CLAUDE.md.

## Los 9 liquidity principles (lista canónica)

Del documento "Liquidity Principles" [PDF: Liquidity Principles]:

1. La volatilidad es una función de la liquidez disponible.
2. El precio va hacia el lado más débil / menos líquido.
3. El precio deja liquidez residual; la liquidez se transfiere a medida que el precio avanza. *(Ver C-001 en 91_contradicciones.md: [USUARIO] cuestiona "transfer of liquidity" como mecanismo.)*
4. Una base de liquidez tiene 3 lados: techo, medio y suelo.
5. Las bases de HTF acumulan más liquidez que las de LTF (liquidez = fricción).
6. El precio simplemente busca, encuentra y consume liquidez.
7. Las extensiones se rellenan — cuanto más lejos viaja el precio de forma ineficiente, más débil se vuelve.
8. Los price runs y swings son fractales: todas las escalas, todo el día.
9. La entrega eficiente de precio es muy fuerte... hasta que deja de serlo.

## Desarrollo (por módulo procesado)

### Volatilidad = f(liquidez disponible)

- "Liquidity (passive & active) is not a constant, volume is variable. Price goes to the weaker, less liquid side. Due to this price can move against the broader sentiment/trend even if it isn't a move with conviction." [PDF: The Price Run p.2]
- "If there's a void of offers above price and bids are coming in thicker (even slightly thicker), price will move through that weak area. Vice versa." [PDF: The Price Run p.4]
- Sentimiento ≠ volumen: en un chop de 9 días con sentimiento bajista estable (GBPUSD jul-2019), cada run alcista fue función de sell liquidity débil, no de cambio de sentimiento. [PDF: The Price Run p.4]

### Mecanismo institucional del price run (por qué existe la ineficiencia)

- Un LP institucional mueve sus quotes ante flujo entrante → respuesta en cadena de todos los LPs (protección anti-arbitraje: ensanchan spreads y sus pricing engines suben los precios) → los flujos "persiguen" las quotes → movimiento fino e ineficiente que **sobrepasa** (overshoot) y deja un **vacío de liquidez** detrás. [PDF: The Price Run p.1, p.8]
- Los LPs trocean órdenes grandes para casarlas sin mover el mercado; su trabajo termina cuando el inventario se llena — después el precio queda sin soporte y rebalancea por el vacío buscando liquidez. [PDF: The Price Run p.6, p.8]
- **Last look** (mecanismo del agotamiento, M2020): en el punto de exhaustion los dealers rechazan y re-cotizan más arriba ("they'll reject it and re-quote at a higher price — so there's absolutely no sell liquidity at the point of exhaustion"); pasado el shelf la liquidez se retira algorítmicamente para evitar adverse selection. Los dealers también retiran quotes ante flujo informado (no por visión direccional) → el precio se estira más de lo que la información justifica = **ineficiencia de mercado** → pockets of air que poco volumen atraviesa de vuelta. [VID-M2020: Session 12 @ 00:58:42–01:10:33]
- Estructura FX: ~15 investment banks + non-bank market makers en competencia imperfecta (oligopolio) con poder asimétrico (rechazar trades, slippage, spreads). "Price reflects the state of liquidity" (uno de los principios más importantes) y "the market-to-limit-order ratio" (puede subir el precio habiendo más vendedores que compradores) completan el marco. [VID-M2020: Session 12 @ 01:04:06–01:07:12] [VID-M2020: Session 15 @ 00:11:01–00:16:30]
- Síntesis del edge: "**we're trading that volatility. That volatility is predictable.** I don't care where cable is in a month — on the way there it will behave in a very consistent way." [VID-M2020: Session 12 @ 01:11:07–01:11:45]
- El disparador del run es **relativo**: "the 'increase' is relative, doesn't have to be massive, just more than the volume keeping price stable" — por eso muchos spikes se secan rápido y vuelven a la base. [PDF: The Price Run p.7, p.9]
- **Contraste externo** [PAPER: HSBC FX LS]: una ficha real de un LP (HSBC, 2019) corrobora el troceo de órdenes "into smaller slices scaled to current market liquidity" para minimizar footprint, la existencia literal de "Liquidity Seeking Algorithms" que persiguen el mercado hasta completar la orden, la ejecución siempre dependiente de liquidez y la ocultación de interés (iceberg). NO documenta en cambio el mecanismo de price-chasing defensivo de los pricing engines que EM usa para explicar el overshoot — esa cadena causal queda como afirmación de EM sin fuente externa. Ver `30_extractos/extracto_paper_fx_liquidity_seeking.md`.

### Ciclo canónico del price run

Estabilidad de volumen (low liquid state) → surge relativo en un lado → run fino/ineficiente → agotamiento (top "jumpy", bids exhausted) → shift de liquidez → rebalance a través del vacío → respuesta en la core liquidity base. [PDF: The Price Run p.5–p.10] [IMG: The Price Run p.10]

- "Contraction leads to expansion" explicado vía liquidez: el precio entra casi siempre en áreas de volumen bajo y estable (LLS, en todos los timeframes) que quedan expuestas a un shot de volumen en un lado. [PDF: The Price Run p.5]

### Fractalidad

- Causa declarada: "price reflects traders behaviour — traders repeatedly do the same thing thus price reflects this on all scales". Todo comportamiento del precio es fractal (PIs, swings, ranges, responsive areas), sea cual sea el sentimiento o la dirección. [PDF: Fractals _ Scaling p.13]
- Entre escalas solo cambian distancia, tiempo y volatilidad relativa ("somewhat proportionately"); la **anatomía es la misma**. Los fractales dan timing y "tempo" del movimiento. [PDF: Fractals _ Scaling p.1, p.7] [PDF: Fractal _ Shift Basics p.1]
- Se repite incluso a escala de eventos macro (GFC y Brexit como "full repeat" en el semanal de GBPUSD). [IMG: Fractals _ Scaling p.5]
- Cada run deja "micro pgaps & inefficiency which will impact later price movements — tempo". [PDF: Fractal _ Shift Basics p.2]
- El estudio de la escala menor debe considerar qué papel juega en el timeframe mayor — es lo que permite operar el contexto amplio y evitar mala gestión. [PDF: Fractals _ Scaling p.1]
- **Enfoque anticipatorio, sin confirmación**: buscar los patrones precedentes que anuncian el run y su lado probable para posicionarse ANTES del movimiento, leyendo anatomía, fase y parámetros relativos de cada fase. [PDF: Fractal _ Shift Basics p.2]
- Todo swing contiene swings menores; el swing HTF es el contenedor de los fractales LTF. [IMG: Price Swing Basics video p.3–p.5]
- Los apexes fractales son auto-similares "regardless of scale or pip distance". [IMG: Price Swings Continued p.13]
- Los shelves son relativos a su timeframe: un shelf de 5min no afecta a un swing H1+; los shelves menores son el inventario de los swings fractales internos. [PDF: Price Swings Continued p.8]
- Mayor escala = más liquidez acumulada: "bigger shelf flips = bigger shifts in momentum, but bigger shelfs hold more liquidity — more work, more time". [PDF: Price Swings Continued p.10]

### Chain reaction (void → estiramiento → rebalance)

- Al golpear un liquidity void el comportamiento del precio cambia y el movimiento se agrava (compound): el run se hace más y más fino "like a chewing gum stretching out and breaking", hasta secarse o ser absorbido. [PDF: Liquidity Void p.1, p.5]
- Tras secarse, POR la forma ineficiente en que se entregó, el precio "sangra" a través del void y rebalancea "to the nearest yet thickest area" / "last point of liquidity". Esto es una restricción de microestructura, independiente de tendencia o sentimiento. [PDF: Liquidity Void p.5, p.12]
- Ocurre "all day long" a todas las escalas. [IMG: Liquidity Void p.7]
- Event-driven: ante datos/CB speak/NFP la liquidez se aleja del precio/TOB → cualquier peso pequeño causa spike ineficiente, igualmente sujeto a rebalance. PERO una sorpresa grande vs consenso puede hacer que el precio siga repricing agresivamente un tiempo — anotar consenso y resultado. [PDF: Liquidity Void p.11]

### Low Liquidity State (LLS): el estado por defecto

- El precio contrae en áreas de volumen bajo y estable (menor tick frequency) cuando la liquidez se retira: fin de día, Asia, pre-datos, incertidumbre; en HTF, por macro/espera de dirección. [PDF: Low Liquidity State p.1, p.9] [IMG: p.4]
- También entra en LLS "anywhere & everywhere, generally after pickups of liquidity, apexes, during price pauses of a broader price run". [PDF: Variable Volume Flow p.4]
- En LLS el precio es máximamente susceptible a un run hacia CUALQUIER lado, incluso contra sentimiento. El pop solo necesita volumen nuevo mayor que el transaccionado EN ESE MOMENTO. [PDF: Low Liquidity State p.2, p.5, p.9]
- Ciclo perpetuo en todos los TF: LLS → run ineficiente → secado → rebalance a base → nuevo LLS. "Price move, sideways, price move, sideways is trending structure, on ALL timeframes." [PDF: Low Liquidity State p.3] [IMG: p.4]
- Cuanto más dura el LLS, mayor tiende a ser el movimiento de salida. [IMG: Low Liquidity State p.4]
- Los LLS son fractales y se forman sobre LLS previos. [PDF: p.5] [IMG: p.7]
- "Price tends to range 80% of the time and move 20% of the time — prices generally draw back into ranges." [PDF: Low Liquidity State p.9]

### Liquidity Imbalance Continuum (diagnóstico de todo movimiento)

- Todo movimiento se genera entre dos condiciones extremas de un espectro: (1) **exhaustion** del lado que empujaba tras dejar void/ineficiencia — el estado natural de venta basta para rebalancear; (2) **presión genuina** con convicción (post shift bajo apex base). El precio se mueve de un extremo al otro del continuum prácticamente todo el tiempo. [PDF: Liquidity Imbalance continuum p.1]
- Implicación de gestión: saber en qué extremo del continuum está el trade — un short de extensión agotada es un trade de fill de pierna débil, no de tendencia. [PDF: Liquidity Imbalance continuum p.2]
- En tendencia: patrón "extension, fill, extension, fill" — cada rebalance contra tendencia encuentra liquidez a favor y empuja a nuevos extremos (trending extension fill ≠ reversal). [PDF: Liquidity Imbalance continuum p.1] [IMG: Liquidity Void p.15]

### Jerarquía de timeframes (principios dictados en M2020)

- "**Higher time frame pulls more liquidity**" y "**higher time frame governs lower time frame / takes precedence**" — dictados como principios para anotar. [VID-M2020: Session 13 @ 00:13:52–00:14:17]
- Un shelf LTF no influye en el TF superior: "if it's a H1 price run, you need a H1 shelf flip"; los flips fractales son inconsecuentes contra el midflow H1 — pero son la herramienta para operar el fill de extensiones (counter flow). [VID-M2020: Session 13 @ 00:13:13–00:15:07]
- "**View your price swings relative to the timeframe they're present on** — a one minute swing has one minute features, the daily swing has daily features"; y a la vez, para seleccionar/temporizar, saber en qué fase del swing mayor está el swing menor. [VID-M2020: Session 13 @ 00:17:41–00:21:18]
- Nivel HTF = más tiempo construyéndose = más liquidez = respuestas mayores y más probables que un nivel de 1min. [VID-M2020: Session 13 @ 00:16:40–00:17:06]

### Entornos de precio (espectro, no trend/range)

- "Price environments are changing relentlessly"; los cambios (aun sutiles) determinan qué niveles sirven, duración del trade, tamaño de la respuesta, frecuencia de trades y gestión. Trend/range es una taxonomía insuficiente: hay trends altamente ineficientes y trends modestamente eficientes que se operan de forma opuesta. [VID-M2020: Session 13 @ 00:23:56–00:25:47]
- Tres métricas permanentes: **volatilidad, estado de liquidez, fase del price swing**. [VID-M2020: Session 13 @ 00:56:47–00:57:33]
- "**After any shot of high volume, volume stabilizes. All the time.** It's an exploitable price behavior." [VID-M2020: Session 13 @ 00:46:21–00:46:39]
- Los movimientos HTF más rápidos son todos **event-driven** (2008, Brexit, flash crash 2019, COVID): la liquidez no comparece + hedging masivo + HFTs que "jump the queue" + flujo pasivo vuelto agresivo; al secarse el evento vuelve la estabilidad. Riesgo de cola: stops ejecutados muy lejos, balance negativo. [VID-M2020: Session 13 @ 00:38:40–00:43:29, 01:51:56–01:52:14]
- Por qué la estabilidad es la norma: demanda de liquidez two-sided no especulativa + cultura de minimización de coste/impacto (algos que trocean y ocultan órdenes). [VID-M2020: Session 13 @ 00:43:35–00:45:29] (Coincide con [PAPER: HSBC FX LS].)
- "The market is **efficiently inefficient**": sin edge en escalas sub-segundo (HFTs ven el precio verdadero antes); "you can't trade breakouts anymore — by the time the breakout is seen on our screen the volatility is finished". [VID-M2020: Session 13 @ 02:06:35–02:07:39]

### Estados y shifts de liquidez

- El swing avanza alimentándose del shelf más cercano hasta que este no puede sostener el run; superar un shelf tras consumir la liquidez opuesta produce un **shift in the state of liquidity**: el otro lado toma el control. [PDF: Price Swings Continued p.8]
- Apex + shelf flip típicamente preceden shift y midflow. [PDF: Price Swings Continued p.8]
- Los **shifting points** son "decision points or momentum shifting, chain reaction effecting points — highly responsive areas". [IMG: Price Swings Continued p.4]
- Tras el shift, el precio corre por liquidez residual débil cuyas respuestas se absorben → midflow (continuación). [IMG: Price Swings Continued p.6]
- **"Midflow means imbalance."** En un HTF midflow la dinámica se invierte respecto a lo normal: la liquidez a favor acepta precios cada vez peores y "turns up at residual levels — at fractal runs which SHOULD be weak", señal de imbalance HTF; las rupturas de shelf fractal dan fills pequeños. Entorno "unusual, not a normal dynamic" que exige adaptar el trading. [VID-M2020: Session 14 @ 00:44:40–00:49:13]

### Formulaciones-tweet del marco (época 2019-2020, capturas MIET)

- "**Think of liquidity as friction. If it's being fragmented in one direction, what's left behind is exposed** — doesn't take much weight for price to push back. Most moves are functions of measures which limit adverse selection that fragment liquidity over a distance of prices → one-sided moves are highly vulnerable to being faded. Optimal: look for weakness in one-sided moves vs continuation. **Price behaviour will show you.**" [IMG-MIET: Tweet Fragmented Lq 1-2]
- "The process of information being embedded into price **'leaks' information. At all times price is reflecting the state of liquidity provision vs liquidity taking** — just a case of interpreting it." [IMG-MIET: First Run out of Asia]
- "Very liquid markets are quite efficient... **until there's a reflexive distortion underway OR, on a shorter term basis, the liquidity landscape is skewed in response to order flow — with the latter repeating and repairing quickly**." (= la definición del edge de EM: esa distorsión corta que repite y se repara.) [IMG-MIET: Efficient markets]
- "After a few days of liquidity hitting one side aggressively, flows dry off, **weak side of book is replenished**... if you missed the big move and you're still after it, you're gonna get chopped up." [IMG-MIET: Tweet 4]
- Mecanismo stop-run (esquema de Tilopa guardado por EM): acumulación de stops bajo el swing low → al saltar, "**price overshoots as market makers reprice and the market has to reach for counterparties**" → llega a buy limits → "price has little trouble retracing this move on relatively low volume". [IMG-MIET: Tilopa]
- "Without the constant change in the state of liquidity on all scales, specifically in FX, I wouldn't be able to trade the way I do... the infrastructure and behaviour of LPs **forces prices into very observable patterns**." [IMG-MIET: Liquidity Dynamics]

### Qué NO es el método (delimitación explícita)

- Contra order blocks/breakers (ICT): su lógica asume "trapped traders" especulativos; EM objeta que gran parte de la sell liquidity viene de entidades sin interés direccional ("they just need to transact for operational purposes — that's the FX market"). [VID-M2020: Session 14 @ 00:08:01–00:08:42]
- El volumen retail no llega al mercado: se internaliza en el broker; el broker cubre su riesgo neto después. [VID-M2020: Session 14 @ 00:08:43–00:09:05]
- No se predice, se observa: "observe, don't predict"; "I shouldn't go into the territory of forecasting". [VID-M2020: Session 14 @ 00:29:44, 00:33:53]
