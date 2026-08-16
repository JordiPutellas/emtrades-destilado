# Conceptos / glosario vivo (EMTrades — destilado)

> Todo término propio del método, con definición, fuente y estado (**confirmado** = definido en material original / **por confirmar** = usado sin definición completa o aportado por el usuario).

## Índice

**Siglas:** [CPS](#cps--characteristics-of-a-price-swing-inferencia-fuerte) · [SWE](#swe--shelf-wash-extension) · [BA](#ba--breakout-accumulation) · [LLS](#lls--low-liquidity-state) · [PI](#pi--price-inefficiency) · [HTF/LTF](#htf--ltf) · [AB/ABR](#ab--abr--apex-base--apex-base-retest) · [ST/SB](#st--sb--shelf-top--shelf-bottom) · [CLB](#clb--core-liquidity-base) · [CBP](#clean-breaking-point-cbp) · [PoR](#por--point-of-release) · [LIC](#liquidity-imbalance-continuum-lic) · [TOB](#tob--top-of-book) · [HOTW](#hotw--high-of-the-week-inferencia)

**Estructura del run/swing:** [Price run](#price-run) · [Price spike](#price-spike) · [Skinny leg](#skinny-leg) · [Price pause](#price-pause) · [Parabolic phase](#parabolic-phase) · [Shelf](#shelf--shelf-liquidity) · [Shelf flip](#shelf-flip) · [Washed (shelf)](#washed-shelf) · [Apex](#apex--apex-base--apex-base-retest) · [Shifting point](#shifting-point) · [Shift in state of liquidity](#shift-in-state-of-liquidity) · [Midflow](#midflow) · [Core liquidity base](#core-liquidity-base) · [Poor high/low](#poor-high--poor-low-unfinished-auction)

**Liquidez y entrega:** [Residual liquidity](#residual-liquidity--residual-levels) · [Liquidity void](#liquidity-void--vacuum) · [Chain reaction](#chain-reaction) · [Gap slip](#gap-slip--gapslip) · [Last point of liquidity](#last-point-of-liquidity) · [Rebalance](#rebalance) · [Trending extension fill](#trending-extension-fill-short-extension-fill) · [Feeder](#feeder--feeding-liquidity) · [Volume stability / surge](#volume-stability--relative-volume-surge) · [Balanced liquidity](#balanced-liquidity--equilibrium) · [Breakout PI](#breakout-pi--fractal-breakout-pi) · [Fractal pushing](#fractal-pushing) · [Latent liquidity / conversion rate](#latent-liquidity--conversion-rate) · [SR / SR flip](#sr--sr-flip)

**Organización de mercado:** [OTC / bilateral](#otc--bilateral--quote-driven) · [Exchange / multilateral](#exchange--multilateral--order-driven) · [Dealer / principal / internalización](#dealer--principal--internalización) · [CCP / settlement](#ccp--central-counterparty--settlement) · [MTF / ECN](#mtf--ecn)

**Trading y gestión:** [Midflow / counter flow trading](#midflow-trading--counter-flow-trading) · [Paying for the trade](#paying-for-the-trade) · [Compound](#compound) · [Dealing range](#dealing-range) · [Responsive vs market-state-dependent levels](#responsive-vs-market-state-dependent-levels) · [CPL](#cpl--consumption-response-leg) · [Washed IV](#washed-iv) · [Momentum](#momentum-definición-y-taxonomía)

> El esquema maestro que ordena casi todos estos términos es el **CPS de 13 componentes** [IMG: Tracking Unfilled Liquidity p.4] — ver entrada CPS y `40_destilado/00_indice.md`.

## Siglas

### CPS — Characteristics of a Price Swing (CONFIRMADO)
- **Estado:** confirmado (2026-08-16). Tres fuentes con el título literal y los mismos 13 componentes: [PDF: Tracking Unfilled Liquidity p.4], [IMG: Characteristics of Price swing.png] (versión alcista) e [IMG: Inverted Fractal.png] (versión bajista).
- **Procedencia:** el esquema lleva marcas "Pro Traders Club" y "ChrisLori.com" → la plantilla CPS procede de **Chris Lori / Pro Traders Club**; EM la adoptó y construyó encima su vocabulario propio (shelf/washed/OP/BA/LIC...). Confirmado además por [IMG-MIET: Chris Question.png]: frame de vídeo PTC (TeamLiquidity, 2-dic-2019) con el vocabulario fractal/pickup/absorption/dealing en charts de 34 ticks. Distinguir herencia vs desarrollo propio al validar.
- El material lo usa como **"CPS framework"**: "the CPS framework is what we use to navigate & trade price... clearly defines components of price which we can categorise throughout the duration of a swing formation... **a representation of HOW price moves rather than why** (!!!)". [PDF: Price Swings Continued p.2]
- **Los 13 componentes del esquema CPS** [IMG: Tracking Unfilled Liquidity p.4], con eje "Mass Psychological Shift":
  1. Liquidity Base → 2. Point of Release (PoR) → 3. Skinny Leg → 4. Price Pause (Shelf Bottom) → 5. Continuation Leg → 6. Consolidation Apex → 7. Retest H/L → 8. Apex Base (break) Retest → 9. Shelf Top/Bottom Retest → 10. Gap slip → 11. Clean Breaking Point → 12. PoR (vuelta) → 13. Liquidity Base Bottom.
- Uso operativo: "Identify liquidity, use CPS to navigate through price & manage the trade." [PDF: Tracking Unfilled Liquidity p.4] "Use CPS features to determine selling continuation points." [PDF: Liquidity Imbalance continuum p.1]
- [USUARIO] CPS es además un setup muy concreto (a trabajar más adelante) — pendiente vídeos.

### SWE — Shelf Wash Extension
- **Estado:** sigla encontrada en fuente (sin expandir); expansión aportada por [USUARIO].
- Uso en fuente, como precursor de un setup de alta probabilidad: "You have a liquidity base, price runs inefficiently into it **extending past highs after a SWE — high probability**." [PDF: Trade Example p.8]
- [USUARIO] SWE = **Shelf Wash Extension**.
- Conexión con el "wash" del shelf: "Only time I will expect price to move through the shelf straight away is **if it is washed** & even then expect some stalling & absorption." [IMG: Trade Example p.5] [INFERENCIA] SWE = barrido del shelf seguido de extensión; Discord, CLP y M2020 Session 1 quedaron agotados sin definición operativa completa. Candidatos: M2020 S2-S11; Price Swing como genealogía.

### BA — Breakout Accumulation
- **Estado:** confirmado (definición formal en M2020).
- **Definición:** "**The inventory, the liquidity base that pushed through the shelf is the breakout accumulation. That's the definition of it**" — la base que empuja el precio a través del shelf hacia midflow (si un intento rompe pero no logra midflow y otro posterior sí, la BA es la de este último). [VID-M2020: Session 12 @ 00:02:14–00:02:27, 00:54:27–00:54:49]
- Familia de retests [VID-M2020: Session 12 @ 00:02:27–00:03:04]: retorno a la BA = **shelf retest** (aunque no haya nivel BA ahí); segundo retest = "**child shelf retest** (the child of the first one)"; si el precio vuelve hasta el low sin romperlo y desde ahí continúa, esa zona "turns into the BA".
- Las BAs pueden estar washed/drenadas — mismo nombre, contexto distinto. [VID-M2020: Session 12 @ 00:54:58] [VID-M2020: Session 14 @ 00:13:55]
- Anotación temprana: "Breakout accumulation, shifting point. Top, middle & bottom generated responses". [IMG: Price Swings Continued p.3] [USUARIO] confirma la expansión.

### LLS — Low Liquidity State
- **Estado:** confirmado.
- Área de contracción del precio con volumen bajo y estable y menor tick frequency, formada cuando la liquidez se retira del mercado (fin de día, Asia, pre-datos, incertidumbre; en HTF por macro). [PDF: Low Liquidity State p.1, p.9]
- También se forma tras pickups de liquidez, apexes y pausas de runs mayores. [PDF: Variable Volume Flow p.4]
- En LLS el precio es máximamente susceptible a un run hacia cualquier lado (incluso contra sentimiento): basta volumen nuevo mayor que el transaccionado en ese momento → pop ("contraction leads to expansion"). Fractal: LLS dentro de LLS, y los nuevos se forman sobre los previos. [PDF: Low Liquidity State p.2, p.5] [IMG: p.4, p.7]
- "LLS = opportunity not only before the break but during and after = price run & rebalances." [PDF: Low Liquidity State p.9]

### PI — Price Inefficiency
- **Estado:** confirmado.
- Segmento de precio con cambio extremo del estado de liquidez, entregado en un run fino por escasez de liquidez en un lado del libro. Sinónimos en el material: gap, liquidity gap. [PDF: Introduction Price Inefficiencies]
- **Corrección doctrinal de EM (tweet 4-may-2020):** la ineficiencia es propiedad del MOVIMIENTO/ESTADO completo, no de micro skinny legs aisladas: "the whole move is inefficient, not just some 3 pip skinny leg from 143 hours ago". [IMG-MIET: InNeFFiciencY]
- **La definición más limpia** (Discord): "inefficiency is relative... but broadly defined as **thinly traded**. Doesnt mean less volume: **imagine a book quoting offers at price 1 and then price 100. You lift everything at price 1 with HUGE volume with remaining unfilled flow — price will run to 100. Thats huge volume, but everything from 2-99 is not traded.**" (Puede haber volumen enorme y ser ineficiente: lo no-transaccionado en medio es la ineficiencia.) [DISCORD: Disc 55, 56]

### YO / WO / MO — Yearly / Weekly / Monthly Open
- **Estado:** confirmado (uso como etiquetas de nivel en charts).
- Aperturas anuales/semanales/mensuales usadas como niveles de referencia en las anticipaciones dibujadas. [IMG-MIET: Prediction 1, Prediction 2, EXZchDyWAAE1rMG]

### HTF / LTF
- **Estado:** confirmado (uso estándar): higher/lower timeframe. Las bases y apexes HTF acumulan más liquidez. [PDF: Liquidity Principles; Price Swings Continued p.10, p.12]

## Organización de mercado

### OTC — bilateral / quote-driven

- **Estado:** confirmado en M2020. OTC es una transacción bilateral entre cliente y proveedor/dealer, comparable a comprar directamente a un shopkeeper. [VID-M2020: Session 1 @ 00:00:55–00:01:52]
- En FX el dealer publica **quotes**, no una orden central garantizada: puede re-cotizar/rechazar mediante last look o cambiar el precio si la liquidez desapareció antes de llegar la orden. [VID-M2020: Session 1 @ 00:11:09–00:11:58] [VID-M2020: Session 1 @ 00:14:29–00:14:53]

### Exchange — multilateral / order-driven

- **Estado:** confirmado en M2020. Una orden puede casarse con una o muchas contrapartes en un single order book. Las limits mostradas son accesibles y la actividad queda registrada; EM lo denomina **order-driven pricing** y lo contrasta con OTC quote-driven. [VID-M2020: Session 1 @ 00:05:34–00:06:59] [VID-M2020: Session 1 @ 00:10:01–00:12:17]
- “Más transparente” se refiere al libro mostrado/registro y firmeza de esas órdenes, no a que toda la liquidez latente sea visible (ver C-002). [VID-M2020: Session 1 @ 00:14:14–00:15:47] [DISCORD: answers] [DISCORD: Disc 64–65]

### Dealer / principal / internalización

- El dealer es contraparte/principal de la operación bilateral: proporciona liquidez y después decide mantener el riesgo, casar con otro cliente o cubrirlo fuera. El broker retail sigue siendo principal frente al cliente aunque se llame ECN/no-dealing-desk. [VID-M2020: Session 1 @ 00:01:54–00:03:19] [VID-M2020: Session 1 @ 00:04:07–00:04:35]
- **Internalización:** el broker/dealer absorbe o casa flow dentro de su propia clientela en vez de enviarlo al mercado amplio; puede agregar tickets pequeños y cubrir solo el neto. [VID-M2020: Session 1 @ 00:04:36–00:05:34]

### CCP — central counterparty / settlement

- Intermediario de un exchange que facilita matching/liquidación multilateral y concentra el counterparty risk; según EM no actúa como dealer ni toma la posición direccional que casa. [VID-M2020: Session 1 @ 00:07:07–00:09:59]
- En OTC el riesgo de contraparte queda contra el dealer/broker directo y persiste hasta settlement (EM explica T+2 en FX). [VID-M2020: Session 1 @ 00:16:34–00:18:18]

### MTF / ECN

- **MTF (multilateral trading facility):** modelo exchange-like dentro de FX; EM usa LMAX como ejemplo de single order book/order-driven con LMAX interpuesto como contraparte. [VID-M2020: Session 1 @ 00:22:34–00:24:22]
- **ECN/agregador:** Hotspot, FXall y Currenex agregan quotes/liquidez de bancos conectados y facilitan routing sin asumir el riesgo principal según EM. No elimina al broker como principal de la operación retail. [VID-M2020: Session 1 @ 00:24:30–00:25:57]

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
- **La debilidad del shelf se confirma en la RESPUESTA, no en la ruptura**: "the weakness isn't necessarily confirmed once price has pushed through — it's confirmed in how price responds off it". Mejor señal: primera pierna atraviesa el shelf de una vez (vs aguantar dentro). [VID-M2020: Session 12 @ 00:12:22–00:13:04]
- **Sin edge aislado**: "just waiting for price to break shelf and then buying it has no edge alone... introduce variables (core pickup, weakness previa, break de midflow + sideways pop hechos) — then there's a higher probability". [VID-M2020: Session 12 @ 01:24:28–01:25:44]

### Apex / apex base / apex base retest
- **Estado:** confirmado.
- "Apexes are areas where a price run meets opposing liquidity, generally in a weak way, and price rebalances lower to shelf liquidity." Auto-similares a cualquier escala. [IMG: Price Swings Continued p.13]
- **Apex base** = horizontal del extremo (leyenda del gráfico anotado); **apex base retest** = retest de esa zona, que típicamente precede shift + midflow junto al shelf flip. [IMG: Price Swings Continued p.3] [PDF: Price Swings Continued p.8]
- Tras causar un shift, el área del apex genera respuestas incluso si el precio la atraviesa después. "An apex that holds inside the shelf without draining or invalidating it is less likely to hold price down (needs your own validation)." [PDF: Price Swings Continued p.8]
- Los apexes HTF acumulan más liquidez; se refinan pockets con el LTF. [PDF: Price Swings Continued p.12, p.14]
- Características del apex favorable (M2020): el extremo aguanta, el apex retest aguanta, el shelf falla en empujar a nuevos extremos, se rompe el shelf y el precio **se estabiliza encima** antes del shift. En los más fuertes, el shelf cae al primer intento y el retest ni siquiera llega al fondo del pickup. [VID-M2020: Session 13 @ 00:58:02–00:58:36]
- **Consolidation apex**: debilidad del movimiento a favor + fuerza core del lado contrario; el shelf ya no tiene "punching power". [VID-M2020: Session 13 @ 01:01:08–01:06:13]
- Existen **4 variaciones principales de apex** (template anunciado por EM, pendiente de localizar en las sesiones). [VID-M2020: Session 13 @ 01:45:10–01:45:27]

### Shifting point
- **Estado:** confirmado.
- "Decision points or momentum shifting, chain reaction effecting points — highly responsive areas." [IMG: Price Swings Continued p.4]

### Shift in state of liquidity
- **Estado:** confirmado.
- Cambio de control de un lado al otro tras consumirse la liquidez que sostenía el run (post shelf flip / apex). "Offers cause momentum change." [PDF: Price Swings Continued p.8] [IMG: p.3]

### Midflow
- **Estado:** confirmado (definición formal en M2020).
- **Definición M2020:** "a **directional price move of imbalance**, with the characteristic that **the inventory that's pushing price holds. The first break of inventory shows a sign of the weakness of that momentum**." Statement de EM a validar: tras la primera ruptura de inventario "it typically won't continue for a long while after". [VID-M2020: Session 13 @ 00:05:44–00:06:12]
- Señal sutil: en midflow fuerte el precio apenas vuelve a meterse en el shelf; asomar/pasar el shelf = debilidad. [VID-M2020: Session 13 @ 00:06:30–00:06:53]
- Variantes: con o sin retorno al shelf; en ambas el último shelf aguanta. "Midflow means imbalance." [VID-M2020: Session 13 @ 00:05:00–00:05:44] [VID-M2020: Session 14 @ 00:45:43]
- Es el building block de la ineficiencia a toda escala (stability→surge→drawback→stability dentro de cualquier pierna). [VID-M2020: Session 13 @ 01:10:12–01:10:24]
- Fase POSTERIOR al shift (post apex + shelf flip): el precio corre por liquidez residual débil con momentum liquidity fuerte a favor. Estructura stair-step: "extension, fill, new range, continuation extension, fill, new range". [PDF: Price Swings Continued p.7]
- "Midflow is an EXPECTATION": si el precio no entra en midflow tras el shift, es razón para reevaluar la idea de trade. [PDF: Price Swings Continued p.7]
- Continúa hasta volverse ineficiente o absorber el inventario del momentum. [PDF: Price Swings Continued p.7]
- **Post-shift stage** se usa como sinónimo/etiqueta visual (rectángulos negros tras el shelf). [IMG: Price Swings Continued p.6]

### Liquidity base (y sus 3 lados)
- **Estado:** confirmado (definición formal en M2020).
- "**Simply an area where price was stable and trade was being facilitated**, and then you typically have a surge out from it (it can also grind out) — in either case the liquidity state shifts." [VID-M2020: Session 13 @ 01:02:13–01:02:43]
- "All types of liquidity bases (fractal core, residual...) have some form of liquidity in them and **there's three sides to it: a top, a middle and a bottom**." (= principio 4 de Liquidity Principles, por fin desarrollado.) [VID-M2020: Session 13 @ 01:03:05–01:03:27]
- Mecánica de drenaje: si el precio alcanza el **bottom**, toda la liquidez de la base se da por consumida; solo queda la del último pickup (débil). La forma de SALIR importa: si absorbió todo al salir, el retorno no tendrá combustible. "The more we test the level, the weaker it gets — the liquidity is being drained (finite, quantitative)." [VID-M2020: Session 13 @ 01:03:29–01:05:24]
- Variaciones visuales: compactas, drifty (típicamente drenadas), con mucha liquidez residual... "you need to test every single type many times over". [VID-M2020: Session 14 @ 00:22:01–00:22:58]

### Origin / fractal core
- **Estado:** confirmado.
- El origen del price run ("the origin of this price run is here — that'll be the fractal core aka origin"). La liquidez más fuerte de una pierna suele estar en su origen. [VID-M2020: Session 13 @ 00:04:44–00:04:52, 01:20:47–01:20:55]

### Core liquidity base
- **Estado:** confirmado (anatomía completa en M2020).
- Base de origen de un price run ("core liquidity base of price run A–B"); genera la mayor respuesta cuando el precio retorna a ella tras el ciclo completo. [IMG: Price Swings Continued p.3] [IMG: The Price Run p.10]
- **Anatomía interna (3 niveles):** "within core areas of liquidity you have **the pickup** (first pickup), **the fractal apex retest**, and **the BA** — three levels inside, which are quite significant". Se refinan por separado para apretar el riesgo (stops de 2-3 pips pegados al nivel, pre-planificados). [VID-M2020: Session 12 @ 00:03:04–00:05:35]
- "**Every single apex is classed as core liquidity relative to the timeframe of the price run.**" [VID-M2020: Session 12 @ 00:03:58]

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

### Balanced liquidity / equilibrium
- **Estado:** confirmado (definición explícita en Discord; no confundir con entrega eficiente de una pierna).
- Estado a corto plazo donde hay "**short term buy side liquidity and sell side liquidity having similar distribution**"; el precio refleja una opinión agregada que coincide y EssFX lo llama equilibrium. [DISCORD: Disc 86]
- Implicación: comprar o hacer trend trading en balance produce chop ("**you'll get chopped up**" / "**you'll do your arse**"). El edge exige una distribución sesgada/distorsión y desaparece al repararse. [DISCORD: Disc 80, 85–87]
- Terminología de EM: "**Value in markets = balanced liquidity**" e "**Inefficient = divergence from value**". No es un modelo de valoración fundamental: "**We're not fair value traders**"; se opera la reparación desde la distorsión hacia el balance. [DISCORD: Disc 87–88]

### Parabolic phase
- **Estado:** confirmado.
- Parte de la anatomía de un top/bottom HTF ("what a top looks like including parabolic phase"). [IMG: Price Swings Continued p.14]
- En el trade real equivale al componente 5: "continuation leg/parabolic phase — **weakest part of the run**". [IMG: Trade Example p.4]
- "The shelf which pushed price into parabolic phase" [IMG: Trade Example p.5]; "sideways pop into parabolic phase = often precedes highs". [IMG: Fractals _ Scaling p.8]
- Secuencia M2020: primer break de midflow → **sideways** (drena inventario) → **pop = parabólica** ("after the sideways comes the pop"); la parabólica lidera el último tramo antes del retorno al shelf. "**We typically don't see the parabolic leg be a leg of significance — we see a reversal and a shift after it.**" [VID-M2020: Session 13 @ 00:18:55–00:19:57, 01:23:47–01:24:00]

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
- **Regla relativa** (generalización en Discord): "**You can have a relatively weak level and an even weaker move into it — generating response until liquidity absorbs the response and continues.**" La respuesta es función de la fuerza del nivel RELATIVA a la debilidad del movimiento de llegada, no de la calidad absoluta del nivel. [DISCORD: Disc 6]
- Las áreas "drifty" están típicamente drained (picked muchas veces). [VID-M2020: Session 14 @ 00:16:09]

### OP — Original Pickup
- **Estado:** confirmado.
- El pickup original de un nivel/área; referencia prioritaria frente a pickups posteriores (ver Feeder). Usado como sigla: "OP present, original pickup", "the OP". [VID-M2020: Session 14 @ 00:18:42, 00:32:13] Definición explícita: "we actually call the pickup of a base the OP, the original pickup". [VID-M2020: Session 13 @ 01:04:15]
- **Regla de validación:** "the original pickup is only validated **once price has grabbed the level and it's gone to the shelf** — if price has just gone into the level and hasn't done anything, it's not classed as a pickup". [VID-M2020: Session 12 @ 00:30:31–00:30:43]
- Invalidación práctica de un trade sobre pickup: "price failed to continue pushing & ended up **taking out the original pickup — that's where our invalidation would be**". [VID-M2020: Session 14 @ 00:06:36] Un poke sutil más allá del low del OP "shifts the probabilities significantly". [VID-M2020: Session 12 @ 00:30:17–00:32:26]
- "In every successful apex, the original pickup will hold. The low held. That's it." [VID-M2020: Session 12 @ 00:10:02]

### HOTW — High Of The Week ([INFERENCIA])
- **Estado:** por confirmar.
- "All three levels of unfilled lq gave price responses, all tradeable, two formed HOTW." [PDF: Tracking Unfilled Liquidity p.3]

### Dealing range
- **Estado:** confirmado (uso).
- Rango donde "liquidity has stabilised again" tras un desplazamiento; el precio forma dealing ranges sucesivos (escalera) mientras la liquidez lenta institucional construye posición. [IMG-MIET: Gold Ranges 5.1]
- Definición explícita + regla direccional (sobre S&P500 en el crash COVID): "These are dealing ranges **in which orders get filled / big positions built / volume builds up. Until we form a dealing range ABOVE the previous one I'd be v v cautious holding longs** — and likely by the time it happens & you get that shift in flow, another shift will be underway." En ese entorno "limits and market orders broadly come in the same direction — **these states don't change quickly, often**". [IMG-TWIT: Dealing Ranges]

### Responsive vs market-state-dependent levels
- **Estado:** por confirmar (distinción enunciada sin criterios).
- "Tip would be to **differentiate between responsive and market-state-dependent levels. Will save faders a lot of pain** if you can do this properly" — dicho a raíz de "event driven volatility" que atrapó a "the new InEfFiCiEnCy boys". [IMG-TWIT: Inneficiency]
- [INFERENCIA] Encaja con la excepción contextual de washed en S14 ("how price arrives") y con las 3 métricas permanentes de S13: hay niveles que responden per se y niveles cuya respuesta depende del estado del mercado (volatilidad/evento). Criterios concretos: NO ESPECIFICADO EN FUENTES.

### Washed IV
- **Estado:** confirmado operativamente; expansión literal de `IV` no escrita.
- Setup nombrado: "**Washed IV setting up on WTI — need a parabolic move lower on daily**" (WTI D1, 15-abr-2020; 5 días antes del crudo negativo). Aclaración: "Doesn't mean WTI is bullish, **price just runs through thin spots to nearest yet thickest areas**." Citando su tweet de 8-sep-2019: "**One of my favourite setups. PaTtErN is present everywhere on every timeframe... really really simple — price goes to the weaker side. Weakness (or strength) is a spectrum, it's never binary.**" [IMG-TWIT: Washed iv wti]
- La serie etiqueta la zona como `Fractal IV`, `IV Consumed` y `Washed IV`. EM explica: "**Price consuming the inventory, weakening the area. Goes deep into it, better yet it pokes past it**". Por tanto, `IV` refiere operativamente al **inventario** (no al numeral cuatro) y `washed` a su consumo/debilitamiento por tests y penetraciones; la expansión literal de las letras no está escrita. [IMG: CLP/ED6JtkLXsAEu4X4.png] [IMG: CLP/EEBYb6-WsAAp2N-.png] [IMG: CLP/EEBe34cXoAEhKWw.png] [IMG: CLP/EUR CPL.jpg]
- Forma/setup: tras separarse el precio de la zona consumida en una CPL, EM busca fade de esa pierna vulnerable; el recorrido esperado atraviesa el inventario débil hacia la zona restante más gruesa. Entrada exacta, invalidación y gestión intermedia: NO ESPECIFICADO EN FUENTES. [IMG: CLP/ED6JtkLXsAEu4X4.png]

### CPL — Consumption response leg

- **Estado:** confirmado; expansión literal escrita por EM: `CPL - consumption response leg`. [IMG: CLP/ED6JtkLXsAEu4X4.png]
- Pierna de respuesta que consume/penetra inventario. Cuando el precio se separa de la consumption en la CPL, esa pierna suele quedar vulnerable: "**once price runs off the consumption in the CPL im looking to fade**"; cualquier liquidez que quede dentro de la response leg por debajo del punto que consumió el inventario es "**generally very weak**". [IMG: CLP/ED6JtkLXsAEu4X4.png]
- Visualmente aparece en XAUUSD 5s/30s/1m/5m, GBPUSD 5m/D1 y EURUSD D1, a ambos lados del mercado; la fuente la presenta como fractal, no ligada a un instrumento/TF. [IMG: CLP/EEBYb6-WsAAp2N-.png] [IMG: CLP/EEBaBCGXkAIIhpc.png] [IMG: CLP/EEBgtXpXUAAoEmR.png] [IMG: CLP/EEBhSR1XsAAh-uH.png] [IMG: CLP/EFyeKT-XkAAP053.png] [IMG: CLP/EUR CPL.jpg]

### Latent liquidity / conversion rate
- **Estado:** confirmado (definido en Discord con esquema propio).
- Esquema "**Visible orderbook vs Real orderbook**": el libro real esconde órdenes mucho mayores — "**traders hide orders to limit information leakage**... much more volume is traded vs available [visible] liquidity → participants hide orders and **only reveal after they've been clipped or as price approaches levels — conversion rate. Conversion of latent liquidity is a huge influence on LP behaviour or subsequent price behaviour.**" "Effect more pronounced in centrally traded products but the **information game is played in all markets**." [DISCORD: Disc 21, 21.1]
- Los movimientos de largo plazo son función de esta liquidez lenta/latente: "long term moves are functions of slower liquidity aka **latent distribution** — the normal digesting forces that dont turn up". [DISCORD: Disc 20]
- Vale también fuera de OTC: "[en futuros tampoco la ves] — **most liquidity is hidden. It shows up over time and has a conversion rate which varies.**" [DISCORD: answers]
- **Definición formal de conversion rate**: "**the rate the latent liquidity converts into orders. If it doesn't, there's only top-of-book liquidity plugged in by market makers — hence you have an open book.**" Lecturas: "**very fast rate as price approaches level = they'll absorb the move; little to no conversion = open book**"; se frena por "**uncertainty usually**" → "skewed latent liquidity, or a skewed book". Driver: "**directly linked to conviction/certainty/willingness to transact**." FX tiene demanda natural alta → "a pretty evenly distributed latent book over time — **hence the large large ranges**". Evidencia: "there's ALWAYS more volume transacted [per day] than the total visible liquidity net — because most of the liquidity is hidden, **to avoid information leakage**." [DISCORD: Disc 64, 65]
- Passive→aggressive: los que esperan su precio "can become aggressive **and populate the book in one direction whilst the opposite remains open** — cable March 2020; EURUSD 2014 is similar, almost unbelievable". [DISCORD: Disc 66]

### SR / SR flip
- **Estado:** confirmado (uso).
- El repertorio de EM incluye soporte/resistencia plano, distinto del shelf: ante una caja en su chart, "**thats not shelf. just SR... its just SR flip.** Reasoning — my eyes." Y el anti-mecanicismo: "the features are definable... but theres a whole spectrum of things that happen at highs and lows. **Any single aspect of it on its own is kinda irrelevant** — better for you to observe it yourself." [DISCORD: Disc 25.1]

### Metaorder / slow vs fast liquidity
- **Estado:** confirmado (uso).
- **Metaorder**: orden institucional grande troceada y ejecutada en el tiempo ("'slow' but larger liquidity building out positions over a period of time, usually automated"), que acepta precios peores para encontrar contrapartida. **Fast liquidity** = HFTs, PTFs, LPs — se vuelve aversa en los surges y dispersa la liquidez más allá del área débil. [IMG-MIET: Gold Ranges 5.1, Gold Ranges 1.0]
- **Warehousing**: los LPs pueden "compound the move" almacenando inventario (estabilizando offers mientras los bids empujan) y/o ensanchando spreads competitivamente; al soltarlo ("LPs unloading inventory") quedan **bid/offer vacuums**. Ciclo intradía: Asia LLS → LPs abren libros en London open → surge. [IMG-MIET: Vol is a F of Av Liq 1, 3]

### Momentum (definición y taxonomía)
- **Estado:** confirmado (definido en Discord, mayo-2020).
- Definición: "**momentum inherently requires an entity with intent to push on price over time OR metaorders being chunked out over a period of time**" — "consistently yeah, **not constantly**"; en FX no es lo habitual ("participants are heterogeneous; slower liquidity from buyside really only trades broader timeframes in line with macro view"). [DISCORD: Disc 4]
- Se lee en el precio: "momentum, strength is reflected in price movement... with basic logic (**limit orders friction, market orders move price**) you can infer what momentum looks like". [DISCORD: Disc 3.0] Antidefinición: "**thats not momentum btw, just fragmented liquidity during event**". [DISCORD: Disc 4]
- **Taxonomía por urgencia** (ejemplos con fecha, cable): (1) **intent con urgencia** — post-headline Brexit 10-oct-2019, "initially anyway"; (2) **momentum pasivo** — sell-off jun-ago 2019, "less urgency, more passive trading" (metaorder: "could simply be a huge order being filled over time, more limits than market selling"); (3) **one-sided liquidity** — marzo 2020. [DISCORD: Disc 5.1, 8]
- Reglas: "**price only sustains a grind if theres urgency** — market orders will always taper off"; urgencia pasiva = "how aggressively it chases price: price moves up a hundred pips, **bids populate the book up there — thats urgency**" (limits y no markets "cus you care about execution cost"). "**One sided liquidity means even if market orders are drying off, theres liquidity there holding price.**" [DISCORD: Disc 9.1, 8]

### Breakout PI / Fractal Breakout PI
- **Estado:** confirmado.
- "Breakout Price Inefficiency after sideways, inside of the broader price swing (**sideways pop into parabolic phase = often precedes highs**)". "Fractal Breakout PIs are components of gap fractals — a highly consistent price behaviour that turn up everywhere; allow us to anticipate a sequence of events (chain reaction) & where voids will develop." [IMG: Fractals _ Scaling p.8]

### Poor high / poor low (unfinished auction)
- **Estado:** confirmado (definición mecánica en Discord; vocabulario de market/volume profile traducido por EM a exhaustion).
- Extremo donde se facilitó poco trade porque se secó el volumen/la liquidez: "**Not a lot of trade was facilitated down there basically. Offers dried up**"; "**Little trade facilitated is poor high low. Or exhaustion basically**". No equivale a un high-volume node: "**high volume doesn't equate lots of facilitated trade**" y "**volume needs liquidity**". [DISCORD: Disc 73, 75–76]
- Mecánica: "**A buyer needs a seller. No seller = no trade. Market order causes price reach for seller leaving thinly traded area behind.**" Un poor low sigue siendo débil aunque entren bids porque no hubo matching real en el extremo. [DISCORD: Disc 73, 77]
- Implicación probabilística: suele dejar "unfinished business" y el precio tiende a volver; la reparación puede ser un simple retest, pero "**more times than not it'll trade through it**". NO garantiza que exista liquidez fresca inmediatamente más allá ("**not necessarily, may or may not be there**") ni que una orden antigua siga esperando indefinidamente. [DISCORD: Disc 73, 77]
- Para EM, la taxonomía de auction/market profile no añade un mecanismo distinto: "**VP is just complicated version to describe simple trade matching**" y poor high/low "**is just exhaustion**". [DISCORD: Disc 77–78]
