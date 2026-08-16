# Setups (EMTrades — destilado)

> Formato obligatorio por setup: QUÉ describe / CUÁNDO entra / DÓNDE invalida / CÓMO gestiona. Si el material no lo especifica: "NO ESPECIFICADO EN FUENTES".

## S-01 · Midflow trading (continuación a favor del flujo)

- **QUÉ describe:** tras un shift en el estado de liquidez (apex + shelf flip), el precio entra en midflow: corre por liquidez residual débil en estructura stair-step (extension, fill, new range, repetir); las respuestas contrarias se absorben en el deal flow cercano y el movimiento continúa. [PDF: Price Swings Continued p.6, p.7]
- **Señal de agotamiento del midflow:** la primera ruptura del inventario que empuja ("first break of midflow") = primer signo de debilidad; después "it typically won't continue for a long while" (statement de EM a validar). El tipo de midflow importa: ineficiente/rápido → solo breakout-style, fills cortos; estable/eficiente → counter-trend viable, fills grandes. [VID-M2020: Session 13 @ 00:05:55–00:06:12, 00:53:20–00:54:42]
- **Escala mínima:** plan validado en mentoría: operar midflow solo en H1+ ("I won't be trading this 5 minute flow"). [VID-M2020: Session 13 @ 01:53:00–01:53:15]
- **CUÁNDO entra:** "wait for price to rebalance down to local liquidity base & look to trade the context" (ejemplo long en midflow alcista). [IMG: Price Swing Basics video p.6] Trigger de vela/nivel concreto: NO ESPECIFICADO EN FUENTES.
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES como regla; pista: "midflow is an EXPECTATION — when price fails to move into midflow stage it is a reason to reassess trade idea"; el run se debilita cuando el precio se vuelve ineficiente o absorbe el inventario del momentum. [PDF: Price Swings Continued p.7]
- **CÓMO gestiona:** duración variable según se opere con o contra flujo. [IMG: Price Swing Basics video p.6] Parciales/BE/targets: NO ESPECIFICADO EN FUENTES.

## S-02 · Counter flow trading (fade de extensión hacia base)

- **QUÉ describe:** en midflow, una pierna se estira más allá del extremo previo hacia liquidez residual, se seca, y el precio rebalancea a la base/inventario más cercano. [IMG: Price Swing Basics video p.6] Ejemplo real ("first touch counter flow short"): "short taken on the premise that price will rebalance an exposed leg down to shelf & ultimately continue (higher). This is because of 'WHAT' price had recently done — price put in low, dealt off shelf, higher low, shift." [PDF: Trade Example p.3]
- **CUÁNDO entra:** "shorting the extension past previous high & to fill it back down to base" [IMG: Price Swing Basics video p.6]; en el ejemplo real, entrada en primer toque de la pierna expuesta, diagnosticada en el extremo bid-exhaustion del LIC ("the run didn't look complete rather this leg looked exposed"). [IMG: Trade Example p.3] Trigger de vela: NO ESPECIFICADO EN FUENTES.
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES como stop; pistas: "cannot hold fades against efficiency" [PDF: módulo Price Inefficiencies]; plan B declarado: "if price started to show signs of breaking down further I can always take shelf flip trade". [IMG: Trade Example p.3]
- **CÓMO gestiona — regla de expectativa/target:** "**any trade against the recent shift is often just to rebalance a weak leg into local buy inventory — I wouldn't be expecting a full blown reversal & new lows. The only instance I would expect new low is if the bounce preceding the shift picked up residual liquidity** (débil); si recogió liquidez mayor (p.ej. daily buyside), solo rebalance." [PDF: Trade Example p.3] "Short holding times on trades." [IMG: Price Swing Basics video p.6] El timeframe limita la respuesta esperable: "nature of timeframe limits how much of a response you're going to get". [IMG: Trade Example p.7]

## S-03 · Fade de PI dentro de fractal (del módulo Price Inefficiencies)

- **QUÉ describe:** ineficiencias que gustan de "fade y ponerse delante — fade altamente probabilístico. Short dentro del fractal, normalmente en un área core de liquidez"; el precio es succionado de vuelta cuando los bids se secan y queda gap dentro de la pierna. [IMG: GBPUSD 1min, módulo Price Inefficiencies]
- **CUÁNDO entra / DÓNDE invalida / CÓMO gestiona:** NO ESPECIFICADO EN FUENTES (criterio tradeable vs non-tradeable PI pendiente — ver 90_preguntas_abiertas.md).

## S-04 · Trades dentro de apex HTF (contexto, no setup cerrado)

- **QUÉ describe:** mientras el big shelf de un run HTF flipa (lleva tiempo), dentro del apex HTF se forman apexes menores y swings LTF que ofrecen longs y shorts. Con contexto HTF considerado, "the play would be to hold shorts as bids inside shelf are weak, the HTF price run is likely dry". [IMG: Price Swings Continued p.14, p.15]
- **CUÁNDO entra:** NO ESPECIFICADO EN FUENTES (clave declarada: saber DÓNDE y CUÁNDO el run HTF probablemente se seca — HTF pocket of liquidity + anatomía del top, incl. parabolic phase). [IMG: Price Swings Continued p.14]
- **DÓNDE invalida / CÓMO gestiona:** NO ESPECIFICADO EN FUENTES.

## S-05 · Fade de void spike / extensión más allá de H-L

- **QUÉ describe:** el precio se extiende ineficientemente más allá de un high/low/shelf golpeando un liquidity void (los stops pueden agravar el surge), se estira, se seca y rebalancea "back to the last point of liquidity". "We like to fade inefficiency & extensions past highs & lows." "The inefficient spike and rebalance after hitting liquidity void is a highly consistent price behaviour, one we will use to catch highs and lows and also counter trend trades." [PDF: Liquidity Void p.6, p.12] [IMG: p.8]
- **CUÁNDO entra:** NO ESPECIFICADO EN FUENTES como trigger. Restricción explícita: "not all are tradeable, our job is to spot & trade the ones that are"; "sometimes the extension is big enough to take counter trend trade, often it's not". [PDF: Liquidity Void p.12, p.16]
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES como regla de stop. Criterio condicional sobre el shelf del rebalance (Gold 2min): "If price starts trading back below this red box (shelf), we are likely to see lower prices. If it can still hold this red box and continue to new highs, all depends on broader state of liquidity." [IMG: Liquidity Void p.8]
- **CÓMO gestiona:** target implícito = last point of liquidity / pierna débil. Diagnóstico obligatorio del continuum: si el movimiento es fill de extensión en tendencia, NO esperar giro ("trending extension fill ≠ reversal"). [PDF: Liquidity Void p.15–16; Liquidity Imbalance continuum p.2]
- **Contexto event-driven:** los spikes de datos son fadeables por la misma mecánica, SALVO sorpresa grande vs consenso (repricing agresivo sostenido) — anotar consenso y resultado. [PDF: Liquidity Void p.11]

## S-06 · Operar alrededor del LLS

- **QUÉ describe:** el LLS es el estado previo al price run; "LLS = opportunity not only before the break but during and after = price run & rebalances". [PDF: Low Liquidity State p.9]
- **CUÁNDO entra:** dos plantillas [PDF: Variable Volume Flow p.4]:
  1. Anticipación: "when price is in a low liq state forming in a desirable place ie after picking up a nice buy base with weakness on sell side — take trades there in anticipation of fill/run higher".
  2. Fade: "fade the actual extension out of the liquidity base, as the price run dries off... extended past a high into a feeder = potential short".
  El propio material avisa: "this isn't explaining HOW we will trade this". Triggers: NO ESPECIFICADO EN FUENTES.
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES.
- **CÓMO gestiona:** NO ESPECIFICADO EN FUENTES. Regla de ubicación: "we want to do our business whilst price is in the low liquidity state, anticipating which side is weaker & thus where price is likely to break (more on this during trade examples & trade management)". [PDF: Low Liquidity State p.9]

## S-07 · Tres entradas sobre un nivel (plantilla general)

- **QUÉ describe:** decidido el nivel (con shelf inventory localizado y tipo de respuesta esperada), hay tres formas de entrar, cada una con parámetros propios e independientes: (1) **fade del movimiento hacia el nivel**, (2) **esperar breakdown y tomar el retest del apex**, (3) **shelf flip trade**. [IMG: Fractals _ Scaling p.12]
- **CUÁNDO entra:** "over time you will come to know which entry is best — can only do that through exercising". Parámetros concretos por variante: NO ESPECIFICADO EN FUENTES.
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES.
- **CÓMO gestiona:** seguimiento del espectro favourable/unfavourable escalando al fractal para ver si el precio responde como debería. [IMG: Fractals _ Scaling p.12]

## Catálogo de comportamientos tradeables (menú declarado por EM)

"Extensions, ABR, Shelf flips, Midflow, Swing Retest of CLB, Residual Liquidity Base responses — everything is inside there... specify which behaviour you want to trade and form parameters to engage the specific feature — for example trading ABRs or shelf flips or swing retests of CLBs, Void Fills. Eventually will include time of day, timeframe alongside entry & execution parameters, developmental & management parameters." [IMG: Fractals _ Scaling p.8]

## S-08 · Fade de agotamiento en nivel bueno (plantilla de 3 componentes, TE-02)

- **QUÉ describe:** extensión muy ineficiente que se estira ("tick frequency goes parabolic reaching for the level") hasta un área core/fractal apex de un swing H1, tras break de midflow / en fase parabólica; el precio rebalancea con fuerza desde el nivel. [VID-M2020: Session 13 @ 01:08:51–01:09:10, 01:14:18]
- **CUÁNDO entra:** los "three main components": "**extension into core liquidity, in the parabolic phase or after a break of midflow, of a H1 price swing**". Ejecución con **buy/sell limit en el nivel** ("area of strength, move of weakness, manageable response"). Frecuencia baja: "you won't get that frequently — it was too good of a trade" (setup análogo en H1: 2-3/semana). [VID-M2020: Session 13 @ 01:14:18–01:14:54, 00:50:00, 01:56:44–01:56:49]
- **DÓNDE invalida:** stop de pips ínfimos tras el nivel (2.6 pips en TE-02; el nivel/OP debe aguantar — ver regla de invalidación del OP en Session 14). [VID-M2020: Session 13 @ 00:50:40] [VID-M2020: Session 14 @ 00:06:36]
- **CÓMO gestiona:** mantener solo mientras el precio "continuously reflects the weakness"; si rompe midflow en contra y hace pop → cortar o descargar. Hora del día pondera: tarde = tomar beneficio (la estabilización overnight puede atravesar el nivel); mañana/mediodía = mantener e incluso añadir. [VID-M2020: Session 13 @ 01:21:42–01:22:07, 01:18:27–01:19:07]
- Distinción crítica de expectancy: mismo patrón contra **residual** (sin nivel real) = trade distinto y peor "over a thousand samples" — el nivel golpeado ES el parámetro. [VID-M2020: Session 13 @ 01:14:56–01:15:46, 01:36:19–01:37:40]

## Response areas de alta probabilidad (lista explícita de EM)

"Look for areas where responses are highly likely with specific parameters, for example:" [PDF: Trade Example p.8]
- "Liquidity base with an inefficient run into the level"
- "Apex retest after shelf invalidated"
- "Mid price run level pickup with an inefficient leg into it"
- "Extension past previous highs into feeding liquidity"
- "Swing retest of apex base"
- "or any combination of highly probable features"

Calibración de variantes del mismo setup [PDF: Trade Example p.8]:
- ALTA probabilidad: "liquidity base, price runs inefficiently into it extending past highs **after a SWE**".
- BAJA probabilidad: "price moves **efficiently** into a sell liquidity base".

Filtro general para operar niveles de unfilled liquidity: "wouldn't blindly trade out of these levels, we want favourable, manageable price responses = why we look for **inefficient price delivery, extensions into these levels**; why we zoom in through the window of price (LTFs) and look at the anatomy, if the way price is developing **fits the setup type**". [PDF: Tracking Unfilled Liquidity p.3]

## Gestión de trades (reglas transversales del ejemplo real GBPUSD 31/07/2019)

Del único trade completamente documentado en PDFs [PDF/IMG: Trade Example p.1–p.7]:

1. **Stop inicial:** 10 pips en un fade sobre 15min/H1 (entrada 1.22466). Único dato numérico en PDFs.
2. **Primer objetivo estructural = el shelf.** "I never expect price to materially break through the shelf and go into midflow without picking up the liquidity inside there & dealing it off — only exception: shelf **washed**, & even then expect stalling & absorption."
3. **Parcial ("paying for the trade")** al llegar al shelf: asegura equity y sostiene psicológicamente el retorno del precio. Discrecional según tipo de trade, méritos y event risk (aquí FOMC).
4. **Stop a invalidación estructural**, no a BE mecánico: "stop moved down to invalidation = high had to hold for sell idea to remain valid. Not always will I move my stop down, but again event risk."
5. **Invalidación dinámica por fase**: más tarde "my invalidation is price bottoming out at a mid price run level — was unlikely due to time of day (1900HRS BST)". La hora del día pondera la probabilidad de la invalidación.
6. **Compound condicionado**: nueva entrada si hay evidencia nueva (liquidez del shelf absorbida en el high) y según convicción, debilidad del shelf, naturaleza del nivel, extensión y data risk. Para añadir en tendencia: "I usually would wait for a rally (fractal price run off residual into sell inventory to fade)".
7. **Soltar la gestión al confirmar midflow**: "continued selling, follow through, shifting point... here I stop managing so tightly & let the trade run, expecting midflow characteristics."
8. **Multi-timeframe**: "constantly shifting between 1-5-15 min timeframes for a broader look."
9. **Fractal ≠ broader**: el flip de apex/shelf del fractal en el high "doesn't mean a shift of the broader price swing, rather it opened up a run down to the shelf" — dimensionar expectativas a la escala del feature.
10. **Contexto SIEMPRE** ("CONTEXT MATTERS, ALWAYS"): catalizadores (FOMC) alteran las reglas por defecto.

Ampliación M2020 (Session 15) — estilo "take my money" y runners:
11. **Estilo base = trading the volatility**: "price spikes up, we short it, it moves 3-5R intraday, take my money. I'm not a swing trader." Cerrar la mayoría el primer día. [VID-M2020: Session 15 @ 00:34:45–00:35:15]
12. **Runner solo con ubicación HTF**: cuando el nivel/swing HTF da "greater probability of a bigger run", tomar beneficio y dejar un trozo pequeño correr ("leave a piece on, forget about it" — WTI desde $5 con 0.5 lots, cable 1.42004 con 0.8 lots). Matemática: buscar 10R sistemáticamente implica cortar varios 3-5R fallidos antes; el estilo activo renuncia a algunos runners a cambio de consistencia. [VID-M2020: Session 15 @ 00:35:36–00:39:16]
13. **Riesgo de cola overnight**: flash spikes en baja liquidez pueden slippear stops masivamente ("probably account gone if over-leveraged") → cuidado con posiciones/órdenes fuera de horario activo. [VID-M2020: Session 15 @ 01:02:21–01:03:28]
14. **No perseguir niveles no tocados**: "when price misses your level, don't chase — often it will end up spiking to it later". [VID-M2020: Session 15 @ 00:55:12–00:55:30]

Ampliación Twitter (2019-2020, capturas EM Twits):
15. **Limit en el punto más fino de liquidez, ejemplo real**: "Limit orders at the thinnest point of liquidity #GBPUSD" — panel visible: limit 1.30139, **SL 5 pips, target 25 pips (5R)**, GBPUSD 5min. La ilustración práctica de "trading at the thinnest point of liquidity with limit orders is highest probability entry type". [IMG-TWIT: Thinest point of LQ]
16. **Regla direccional de dealing ranges para holds**: "until we form a dealing range ABOVE the previous one I'd be v v cautious holding longs — by the time it happens & you get that shift in flow, another shift will be underway" (S&P500, crash COVID). [IMG-TWIT: Dealing Ranges]
17. **Filtro para faders en volatilidad event-driven**: "differentiate between **responsive and market-state-dependent levels** — will save faders a lot of pain". [IMG-TWIT: Inneficiency]
18. **Entradas "after high in" en baja volatilidad**: "this is what you can do in **low volatility (relative to recent weeks)** environments"; "volatility always shifting, it's dynamic — in broadly high vol environments you still have periods of vol contraction". [IMG-TWIT: Volatility]
19. **Otro trade real con stop de pips**: "Price goes to the less liquid side. See you tomorrow #GBPUSD" — long 15min corriendo **+72.6 pips con SL ~4.5 pips (~16R)**, 4-feb-2020. [IMG-TWIT: Excess demand- less liquid side] Y micro-trades del 5-feb con **SL 1.8 pips** (+22.2 pips corriendo). [IMG-TWIT: PA Only] (Consistente con la serie: stops 2-10 pips, targets estructurales.)
20. **Excepción con catalizador de calibre** (playbook invertido): tras un evento tipo emergency cut, con la liquidez desaparecida y el libro abierto en una dirección, "**you can chase price... trail stops, buy the retest of highs**" — lo contrario del fade por defecto. Condición: "long as you get the significance of the catalyst on available liquidity". [IMG-TWIT: Emergency Cut]

## Comportamientos de referencia (aún sin setup formalizado)

- **Gaps & rebalances**: "una de las mejores" conductas por consistencia. [PDF: módulo Price Inefficiencies]
- **BA (Breakout Accumulation)** como nivel de reacción: definida formalmente en M2020 (la base que empuja a través del shelf; sus retests = shelf retest / child shelf retest). "BA is quite responsive" — pero comprobar si está washed. [VID-M2020: Session 12 @ 00:02:14–00:03:04, 00:08:56] Reglas de entrada específicas: NO ESPECIFICADO EN FUENTES aún.
- **Estilo de entrada según calidad del nivel** [INFERENCIA de S12+S13]: limit resting pre-colocada solo en niveles top (fractal apex/core — TE-02); en niveles menores, entrada activa vigilando la llegada ("I can view incoming price action to determine if it's likely to continue or fail"). Stops de 2-3 pips pegados al nivel refinado, pre-planificados. [VID-M2020: Session 12 @ 00:00:41–00:01:09, 00:04:19–00:05:35]
- **Regla de expectancy de S12**: niveles residual+washed pueden responder pero no tienen edge ("you'd much rather wait for the 90/10 than the 60/40" — law of large numbers). [VID-M2020: Session 12 @ 00:22:20–00:27:12]
- **CPS como setup**: [USUARIO] indica que existe un setup concreto llamado CPS, a trabajar más adelante. NO ESPECIFICADO EN FUENTES procesadas.
- **Respuesta en core liquidity base**: la mayor respuesta contraria tras un ciclo completo de run+reversión aparece en la core base del run original. [IMG: Price Swings Continued p.3] [IMG: The Price Run p.10]
- **Template de variaciones de low** (precursor Twitter, jun-jul 2019): "This is a **variation of a low**... there's **2 or 3 other predominant variations for lows** — this is my favourite"; "**inside the accumulation at the low there's at least 5 trades**"; y la variación donde "price **extends a little deeper past the low**" dentro del broader fractal ("look at original template thingy"). Replicado en XAUUSD 1min, GBPUSD y WTI. [IMG-TWIT: Reversal, Reversal 2] [INFERENCIA] Probable precursor del template de 4 variaciones de apex de M2020 (pregunta 4) y de la lección del poke-past-the-low (pregunta 7).
- **"Washed IV"**: setup nombrado sin definición ("one of my favourite setups... price goes to the weaker side; weakness is a spectrum, never binary"), armado en WTI daily el 15-abr-2020 esperando "a parabolic move lower". [IMG-TWIT: Washed iv wti] Ver entrada en 02_conceptos.md.
