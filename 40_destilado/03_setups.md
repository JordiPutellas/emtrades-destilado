# Setups (EMTrades — destilado)

> Formato obligatorio por setup: QUÉ describe / CUÁNDO entra / DÓNDE invalida / CÓMO gestiona. Si el material no lo especifica: "NO ESPECIFICADO EN FUENTES".

## S-01 · Midflow trading (continuación a favor del flujo)

- **QUÉ describe:** tras un shift en el estado de liquidez (apex + shelf flip), el precio entra en midflow: corre por liquidez residual débil en estructura stair-step (extension, fill, new range, repetir); las respuestas contrarias se absorben en el deal flow cercano y el movimiento continúa. [PDF: Price Swings Continued p.6, p.7]
- **CUÁNDO entra:** "wait for price to rebalance down to local liquidity base & look to trade the context" (ejemplo long en midflow alcista). [IMG: Price Swing Basics video p.6] Trigger de vela/nivel concreto: NO ESPECIFICADO EN FUENTES.
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES como regla; pista: "midflow is an EXPECTATION — when price fails to move into midflow stage it is a reason to reassess trade idea"; el run se debilita cuando el precio se vuelve ineficiente o absorbe el inventario del momentum. [PDF: Price Swings Continued p.7]
- **CÓMO gestiona:** duración variable según se opere con o contra flujo. [IMG: Price Swing Basics video p.6] Parciales/BE/targets: NO ESPECIFICADO EN FUENTES.

## S-02 · Counter flow trading (fade de extensión hacia base)

- **QUÉ describe:** en midflow, una pierna se estira más allá del extremo previo hacia liquidez residual, se seca, y el precio rebalancea a la base/inventario más cercano. [IMG: Price Swing Basics video p.6]
- **CUÁNDO entra:** "shorting the extension past previous high & to fill it back down to base — counter flow trading". [IMG: Price Swing Basics video p.6] Trigger concreto: NO ESPECIFICADO EN FUENTES.
- **DÓNDE invalida:** NO ESPECIFICADO EN FUENTES. Pista general del método: "cannot hold fades against efficiency" [PDF: módulo Price Inefficiencies]; en midflow, todo movimiento contra el flujo desde área residual "is subject to drying off". [PDF: Price Swings Continued p.7]
- **CÓMO gestiona:** "short holding times on trades". [IMG: Price Swing Basics video p.6] Resto: NO ESPECIFICADO EN FUENTES.

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

## Comportamientos de referencia (aún sin setup formalizado)

- **Gaps & rebalances**: "una de las mejores" conductas por consistencia. [PDF: módulo Price Inefficiencies]
- **BA (Breakout Accumulation)** como shifting point: sus zonas top/middle/bottom generan respuestas al retorno del precio — candidato a nivel de entrada/reacción. [IMG: Price Swings Continued p.3] Setup concreto: NO ESPECIFICADO EN FUENTES (pendiente vídeos).
- **CPS como setup**: [USUARIO] indica que existe un setup concreto llamado CPS, a trabajar más adelante. NO ESPECIFICADO EN FUENTES procesadas.
- **Respuesta en core liquidity base**: la mayor respuesta contraria tras un ciclo completo de run+reversión aparece en la core base del run original. [IMG: Price Swings Continued p.3] [IMG: The Price Run p.10]
