# Conceptos / glosario vivo (EMTrades — destilado)

> Todo término propio del método, con definición, fuente y estado (**confirmado** = definido en material original / **por confirmar** = usado sin definición completa o aportado por el usuario).

## Índice

**Siglas:** [CPS](#cps--characteristics-of-a-price-swing-inferencia-fuerte) · [SWE](#swe--shelf-wash-extension) · [BA](#ba--breakout-accumulation) · [LLS](#lls--low-liquidity-state) · [PI](#pi--price-inefficiency) · [HTF/LTF](#htf--ltf) · [AB/ABR](#ab--abr--apex-base--apex-base-retest) · [ST/SB](#st--sb--shelf-top--shelf-bottom) · [CLB](#clb--core-liquidity-base) · [CBP](#clean-breaking-point-cbp) · [PoR](#por--point-of-release) · [LIC](#liquidity-imbalance-continuum-lic) · [TOB](#tob--top-of-book) · [HOTW](#hotw--high-of-the-week-inferencia)

**Estructura del run/swing:** [Price run](#price-run) · [Price spike](#price-spike) · [Skinny leg](#skinny-leg) · [Price pause](#price-pause) · [Parabolic phase](#parabolic-phase) · [Shelf](#shelf--shelf-liquidity) · [Shelf flip](#shelf-flip) · [Washed (shelf)](#washed-shelf) · [Apex](#apex--apex-base--apex-base-retest) · [Shifting point](#shifting-point) · [Shift in state of liquidity](#shift-in-state-of-liquidity) · [Midflow](#midflow) · [Core liquidity base](#core-liquidity-base)

**Liquidez y entrega:** [Residual liquidity](#residual-liquidity--residual-levels) · [Liquidity void](#liquidity-void--vacuum) · [Chain reaction](#chain-reaction) · [Gap slip](#gap-slip--gapslip) · [Last point of liquidity](#last-point-of-liquidity) · [Rebalance](#rebalance) · [Trending extension fill](#trending-extension-fill-short-extension-fill) · [Feeder](#feeder--feeding-liquidity) · [Volume stability / surge](#volume-stability--relative-volume-surge) · [Breakout PI](#breakout-pi--fractal-breakout-pi) · [Fractal pushing](#fractal-pushing)

**Trading y gestión:** [Midflow / counter flow trading](#midflow-trading--counter-flow-trading) · [Paying for the trade](#paying-for-the-trade) · [Compound](#compound)

> El esquema maestro que ordena casi todos estos términos es el **CPS de 13 componentes** [IMG: Tracking Unfilled Liquidity p.4] — ver entrada CPS y `40_destilado/00_indice.md`.

## Siglas

### CPS — Characteristics of a Price Swing ([INFERENCIA fuerte])
- **Estado:** por confirmar la expansión literal; la anatomía sí está confirmada en fuente.
- El material lo usa como **"CPS framework"**: "the CPS framework is what we use to navigate & trade price... clearly defines components of price which we can categorise throughout the duration of a swing formation... **a representation of HOW price moves rather than why** (!!!)". [PDF: Price Swings Continued p.2]
- [INFERENCIA fuerte] CPS = "**Characteristics of a Price Swing**": es el título literal del esquema maestro de 13 componentes [IMG: Tracking Unfilled Liquidity p.4], encaja letra a letra y con la frase "the CPS clearly defines components of price which we can categorise". (Descarta la hipótesis anterior "Core Price Swing".) Existe además la captura suelta `capturas/Characteristics of Price swing.png` — verificar que es el mismo esquema al procesar capturas.
- **Los 13 componentes del esquema CPS** [IMG: Tracking Unfilled Liquidity p.4], con eje "Mass Psychological Shift":
  1. Liquidity Base → 2. Point of Release (PoR) → 3. Skinny Leg → 4. Price Pause (Shelf Bottom) → 5. Continuation Leg → 6. Consolidation Apex → 7. Retest H/L → 8. Apex Base (break) Retest → 9. Shelf Top/Bottom Retest → 10. Gap slip → 11. Clean Breaking Point → 12. PoR (vuelta) → 13. Liquidity Base Bottom.
- Uso operativo: "Identify liquidity, use CPS to navigate through price & manage the trade." [PDF: Tracking Unfilled Liquidity p.4] "Use CPS features to determine selling continuation points." [PDF: Liquidity Imbalance continuum p.1]
- [USUARIO] CPS es además un setup muy concreto (a trabajar más adelante) — pendiente vídeos.

### SWE — Shelf Wash Extension
- **Estado:** sigla encontrada en fuente (sin expandir); expansión aportada por [USUARIO].
- Uso en fuente, como precursor de un setup de alta probabilidad: "You have a liquidity base, price runs inefficiently into it **extending past highs after a SWE — high probability**." [PDF: Trade Example p.8]
- [USUARIO] SWE = **Shelf Wash Extension**.
- Conexión con el "wash" del shelf: "Only time I will expect price to move through the shelf straight away is **if it is washed** & even then expect some stalling & absorption." [IMG: Trade Example p.5] [INFERENCIA] SWE = barrido del shelf seguido de extensión; definición operativa completa pendiente de vídeos/Discord.

### BA — Breakout Accumulation
- **Estado:** confirmado.
- Anotación en gráfico: "**Breakout accumulation, shifting point. Top, middle & bottom generated responses** (orange circles)". [IMG: Price Swings Continued p.3]
- [USUARIO] confirma BA = Breakout Accumulation.
- Es un punto de shift; sus tres zonas (top/middle/bottom) generan respuestas cuando el precio vuelve.

### LLS — Low Liquidity State
- **Estado:** confirmado.
- Área de contracción del precio con volumen bajo y estable y menor tick frequency, formada cuando la liquidez se retira del mercado (fin de día, Asia, pre-datos, incertidumbre; en HTF por macro). [PDF: Low Liquidity State p.1, p.9]
- También se forma tras pickups de liquidez, apexes y pausas de runs mayores. [PDF: Variable Volume Flow p.4]
- En LLS el precio es máximamente susceptible a un run hacia cualquier lado (incluso contra sentimiento): basta volumen nuevo mayor que el transaccionado en ese momento → pop ("contraction leads to expansion"). Fractal: LLS dentro de LLS, y los nuevos se forman sobre los previos. [PDF: Low Liquidity State p.2, p.5] [IMG: p.4, p.7]
- "LLS = opportunity not only before the break but during and after = price run & rebalances." [PDF: Low Liquidity State p.9]

### PI — Price Inefficiency
- **Estado:** confirmado.
- Segmento de precio con cambio extremo del estado de liquidez, entregado en un run fino por escasez de liquidez en un lado del libro. Sinónimos en el material: gap, liquidity gap. [PDF: Introduction Price Inefficiencies]

### HTF / LTF
- **Estado:** confirmado (uso estándar): higher/lower timeframe. Las bases y apexes HTF acumulan más liquidez. [PDF: Liquidity Principles; Price Swings Continued p.10, p.12]

## Anatomía del price swing

### Price run
- **Estado:** confirmado.
- Movimiento direccional fino disparado por un surge **relativo** de volumen contra un estado de baja liquidez; sobrepasa por el mecanismo de price-chasing de los LPs y deja vacío detrás. Ciclo: estabilidad → surge relativo → run → agotamiento → rebalance a core base. [PDF: The Price Run p.1–p.10]

### Price spike
- **Estado:** confirmado.
- Spike que no requiere gran volumen, solo un shot relativo vs condiciones previas; suele secarse rápido y "volver a la base". [IMG: The Price Run p.9]

### Shelf / shelf liquidity
- **Estado:** confirmado.
- "**Bulk of the momentum pushing any single price move, every price swing has one.** As price is running along, it continuously feeds into the nearest shelf, picks liquidity up and continues the price run until the shelf isn't strong enough to continue supporting the run." [PDF: Price Swings Continued p.8]
- Definición operativa M2020: "the **last inventory** that pushed price to new lows (highs)". Regla de trazado: "**you draw the shelf just like you draw a level but you pay no attention to where it was picked off — you just draw the FULL shelf**" (el shelf no se refina, los niveles sí). [VID-M2020: Session 14 @ 00:09:15, 00:07:19]
- Relativo al timeframe del swing; los shelves pequeños son inventario de los fractales internos. [PDF: Price Swings Continued p.8, p.10]
- Visual: rectángulo de consolidación pegado al tramo final del run ("bulk of buyers/sellers holding price"). No son limpios ni iguales. [IMG: Price Swings Continued p.9]

### Shelf flip
- **Estado:** confirmado (uso), definición implícita.
- Superación del shelf tras consumir su liquidez → el lado contrario toma control (shift). "Bigger shelf flips = bigger shifts in momentum" pero requieren más trabajo/tiempo. [PDF: Price Swings Continued p.8, p.10]

### Apex / apex base / apex base retest
- **Estado:** confirmado.
- "Apexes are areas where a price run meets opposing liquidity, generally in a weak way, and price rebalances lower to shelf liquidity." Auto-similares a cualquier escala. [IMG: Price Swings Continued p.13]
- **Apex base** = horizontal del extremo (leyenda del gráfico anotado); **apex base retest** = retest de esa zona, que típicamente precede shift + midflow junto al shelf flip. [IMG: Price Swings Continued p.3] [PDF: Price Swings Continued p.8]
- Tras causar un shift, el área del apex genera respuestas incluso si el precio la atraviesa después. "An apex that holds inside the shelf without draining or invalidating it is less likely to hold price down (needs your own validation)." [PDF: Price Swings Continued p.8]
- Los apexes HTF acumulan más liquidez; se refinan pockets con el LTF. [PDF: Price Swings Continued p.12, p.14]

### Shifting point
- **Estado:** confirmado.
- "Decision points or momentum shifting, chain reaction effecting points — highly responsive areas." [IMG: Price Swings Continued p.4]

### Shift in state of liquidity
- **Estado:** confirmado.
- Cambio de control de un lado al otro tras consumirse la liquidez que sostenía el run (post shelf flip / apex). "Offers cause momentum change." [PDF: Price Swings Continued p.8] [IMG: p.3]

### Midflow
- **Estado:** confirmado.
- Fase POSTERIOR al shift (post apex + shelf flip): el precio corre por liquidez residual débil con momentum liquidity fuerte a favor. Estructura stair-step: "extension, fill, new range, continuation extension, fill, new range". [PDF: Price Swings Continued p.7]
- "Midflow is an EXPECTATION": si el precio no entra en midflow tras el shift, es razón para reevaluar la idea de trade. [PDF: Price Swings Continued p.7]
- Continúa hasta volverse ineficiente o absorber el inventario del momentum. [PDF: Price Swings Continued p.7]
- **Post-shift stage** se usa como sinónimo/etiqueta visual (rectángulos negros tras el shelf). [IMG: Price Swings Continued p.6]

### Core liquidity base
- **Estado:** confirmado (uso), definición implícita.
- Base de origen de un price run ("core liquidity base of price run A–B"); genera la mayor respuesta cuando el precio retorna a ella tras el ciclo completo. [IMG: Price Swings Continued p.3] También "core area of liquidity" en fades de PI [IMG: GBPUSD 1min, módulo Price Inefficiencies] y "back down to core base" [IMG: The Price Run p.10].

### Residual liquidity / residual levels
- **Estado:** confirmado.
- Liquidez débil que queda tras un movimiento ("residual liquidity from the up move, weak, bottomside unfilled, top picked"). Las respuestas desde bases residuales son débiles y se absorben en midflow. [IMG: Price Swings Continued p.3, p.5] [PDF: p.7]

### Gap slip / gapslip
- **Estado:** confirmado (uso), definición implícita.
- Etiquetado sobre el tramo en que el precio "gaps through on the way down" al atravesar el void dejado por los bids. [IMG: Price Swings Continued p.3]

### Liquidity void / vacuum
- **Estado:** confirmado.
- "Areas in price where there is less liquidity or a complete void." Cuando el precio golpea uno, agrava (compound) el movimiento en curso y dispara la **chain reaction**. [PDF: Liquidity Void p.6, p.1]
- Ubicaciones probables ("**distinct levels**"): más allá de un shelf, de highs/lows (del día, semana, mes, swings — con stops que agravan el surge), shelf inventory y rangos de LLS. [PDF: Liquidity Void p.6] [IMG: p.13]
- El que deja detrás un run fino es el canal por el que el precio rebalancea al secarse el flujo. [PDF: The Price Run p.1, p.8]

### Chain reaction
- **Estado:** confirmado.
- Secuencia: precio golpea void → el movimiento se agrava y adelgaza ("chewing gum stretching out and breaking") → se seca o es absorbido → por la forma ineficiente de la entrega, sangra de vuelta por el void y rebalancea al área más cercana y gruesa. Restricción de microestructura independiente de tendencia/sentimiento. [PDF: Liquidity Void p.5]

### Last point of liquidity
- **Estado:** confirmado (uso).
- Target natural del rebalance tras un void spike: "price is subject to a rebalance back to the last point of liquidity". [PDF: Liquidity Void p.12] [IMG: p.8]

### Liquidity Imbalance Continuum (LIC)
- **Estado:** confirmado (también como sigla: "left end of the LIC spectrum" [PDF: Trade Example p.4]).
- Espectro entre las 2 condiciones que generan cualquier movimiento: **exhaustion** (secado del lado que empujaba tras void/ineficiencia; el estado natural del flujo contrario basta para rebalancear) vs **presión genuina** (convicción post-shift). El precio transita el continuum casi todo el tiempo; hay que saber en qué extremo se toma cada trade (gestión). [PDF: Liquidity Imbalance continuum p.1–2]

### Trending extension fill (short extension fill)
- **Estado:** confirmado.
- En tendencia, el fill de una extensión "aka short extension fill — no reversal, just rebalance to find sellers": los rebalances contra tendencia encuentran liquidez a favor y el precio sigue a nuevos extremos. No confundir fill con giro. [IMG: Liquidity Void p.15] [PDF: p.16]

### Feeder / feeding liquidity
- **Estado:** confirmado (uso aclarado en M2020).
- "After price has ran a fair bit, extended past a high into a feeder = potential short." [PDF: Variable Volume Flow p.4] "Extension past previous highs into feeding liquidity." [PDF: Trade Example p.8]
- Aclaración M2020: el feeder es **el nivel original al que el precio "alimenta"** (feeds into), por oposición al pickup derivado. Ante la duda de qué nivel usar (original vs pickup): "you'll find that it's typically **the feeder, the original**". El precio "feeds off" el original pickup también en apex retests. [VID-M2020: Session 14 @ 00:00:41–00:01:02, 00:18:49]
- Cada pickup genera su propia "bay of liquidity", típicamente más débil que el original. [VID-M2020: Session 14 @ 00:00:41]

### TOB — Top of Book
- **Estado:** confirmado (uso estándar de microestructura).
- "Around big data... we see liquidity draw further away from price/TOB." [PDF: Liquidity Void p.11]

### Rebalance
- **Estado:** confirmado.
- Vuelta del precio a través del tramo ineficiente/vacío hacia la liquidez/base que lo origina, al agotarse el flujo que empujaba. [PDF: The Price Run p.6–p.10; Introduction Price Inefficiencies]

### Low liquid state → ver LLS

### Volume stability / relative volume surge
- **Estado:** confirmado.
- Estado de volumen bajo y estable que mantiene el precio en rango; el run se dispara cuando entra un surge **relativo** ("just more than the volume keeping price stable"). [PDF: The Price Run p.7] [IMG: p.10]

### Parabolic phase
- **Estado:** confirmado (uso repetido); anatomía completa pendiente.
- Parte de la anatomía de un top/bottom HTF ("what a top looks like including parabolic phase"). [IMG: Price Swings Continued p.14]
- En el trade real equivale al componente 5: "continuation leg/parabolic phase — **weakest part of the run**". [IMG: Trade Example p.4]
- "The shelf which pushed price into parabolic phase" [IMG: Trade Example p.5]; "sideways pop into parabolic phase = often precedes highs". [IMG: Fractals _ Scaling p.8]

### Midflow trading / counter flow trading
- **Estado:** confirmado (nombres de estilo de trade). Ver 03_setups.md.
- Midflow trading = entrar a favor del flujo tras rebalance a base local; counter flow trading = fade de la extensión de vuelta a base, "short holding times". [IMG: Price Swing Basics video p.6]

### Fractal pushing
- **Estado:** por confirmar. Detectado en módulo Price Inefficiencies sin definición. [PDF: módulo Price Inefficiencies]

### AB / ABR — Apex Base / Apex Base Retest
- **Estado:** confirmado (siglas usadas como etiquetas de gráfico).
- "AB & ABR" marcando apex bases y sus retests. El ABR figura en el menú de comportamientos tradeables ("trading ABRs"). [IMG: Fractals _ Scaling p.2, p.8]

### ST / SB — Shelf Top / Shelf Bottom
- **Estado:** confirmado (siglas usadas como etiquetas de gráfico).
- "ST & SB (green eclipse = response)": techo y suelo del shelf como puntos de respuesta. [IMG: Fractals _ Scaling p.2] El esquema CPS incluye "Shelf Top/Bottom Retest" como componente 9. [IMG: Tracking Unfilled Liquidity p.4]

### CLB — Core Liquidity Base
- **Estado:** confirmado (sigla).
- Abreviatura de core liquidity base; "swing retests of CLBs" es un comportamiento tradeable del catálogo. [IMG: Fractals _ Scaling p.8]

### Clean Breaking Point (CBP)
- **Estado:** confirmado.
- Punto de ruptura limpia de una liquidity base; "support turns resistance" — suele albergar una base fractal del lado contrario. Componente 11 del esquema CPS. [IMG: Fractals _ Scaling p.2] [IMG: Tracking Unfilled Liquidity p.4]

### PoR — Point of Release
- **Estado:** confirmado.
- Punto donde el precio "se libera" de la liquidity base e inicia el run (componente 2 del esquema CPS; reaparece como componente 12 en el retorno). "Point of release of H1 fractal with parabolic phase also extending." [IMG: Tracking Unfilled Liquidity p.4] [IMG: Trade Example p.4]

### Skinny leg
- **Estado:** confirmado.
- Pierna fina/ineficiente post-release (componente 3 del esquema CPS). "LV & Extension through previous skinny leg." [IMG: Tracking Unfilled Liquidity p.4] [IMG: Fractals _ Scaling p.2]

### Price pause
- **Estado:** confirmado.
- Pausa tras la skinny leg (componente 4 del esquema CPS); una de las "constituent features of a price run" usadas como confluencia. [IMG: Tracking Unfilled Liquidity p.4] [PDF: Trade Example p.4]

### Paying for the trade
- **Estado:** confirmado.
- Asegurar equity parcial cuando el precio alcanza el primer objetivo estructural (el shelf), cubriendo el riesgo asumido: "I secured equity paying for my trade & the risk assumed... EXTREMELY important to manage my psychological profile & to be able to sustain price coming back on me." Discrecional: "sometimes I won't pay for the trade — depends on what kind of trade it is, merits of the trade & event risks." [PDF/IMG: Trade Example p.5]

### Compound
- **Estado:** confirmado (uso).
- Añadir una segunda posición en la misma idea cuando el precio ofrece nueva evidencia (p.ej. liquidez del shelf absorbida en el high). Condiciones citadas: convicción en la idea, cuán débil quedó el shelf (¿invalidado?), naturaleza del nivel que recoge, cuán extendido está, y data risk. En HTF: "I would definitely look for compounds & midflow trades beneath the shelf." [IMG: Trade Example p.6] [PDF: p.6]

### Washed / drained
- **Estado:** confirmado; relación directa con SWE.
- Un shelf "washed" (barrido) es la única condición bajo la que EM espera que el precio lo atraviese directamente sin dealing previo — "& even then expect some stalling & absorption". [IMG: Trade Example p.5]
- Nivel washed/drained = agarrado repetidamente ("grabbed it, grabbed it, grabbed it") → falta de liquidez: "you shouldn't really have any problems to get through". Probabilidad de respuesta de un área washed: "**low**". [VID-M2020: Session 14 @ 00:12:40, 00:27:27, 00:34:51]
- Excepción contextual: un área washed puede responder según CÓMO llega el precio — "broke midflow, broke shelf, sideways pop into it" responde más que "strong midflow becoming inefficient into it". "They're both washed but the contextual environment is completely different." [VID-M2020: Session 14 @ 00:35:11–00:35:40]
- Las áreas "drifty" están típicamente drained (picked muchas veces). [VID-M2020: Session 14 @ 00:16:09]

### OP — Original Pickup
- **Estado:** confirmado.
- El pickup original de un nivel/área; referencia prioritaria frente a pickups posteriores (ver Feeder). Usado como sigla: "OP present, original pickup", "the OP". [VID-M2020: Session 14 @ 00:18:42, 00:32:13]
- Invalidación práctica de un trade sobre pickup: "price failed to continue pushing & ended up **taking out the original pickup — that's where our invalidation would be**". [VID-M2020: Session 14 @ 00:06:36]

### HOTW — High Of The Week ([INFERENCIA])
- **Estado:** por confirmar.
- "All three levels of unfilled lq gave price responses, all tradeable, two formed HOTW." [PDF: Tracking Unfilled Liquidity p.3]

### Breakout PI / Fractal Breakout PI
- **Estado:** confirmado.
- "Breakout Price Inefficiency after sideways, inside of the broader price swing (**sideways pop into parabolic phase = often precedes highs**)". "Fractal Breakout PIs are components of gap fractals — a highly consistent price behaviour that turn up everywhere; allow us to anticipate a sequence of events (chain reaction) & where voids will develop." [IMG: Fractals _ Scaling p.8]
