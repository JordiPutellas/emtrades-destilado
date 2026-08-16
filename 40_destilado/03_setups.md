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

## Comportamientos de referencia (aún sin setup formalizado)

- **Gaps & rebalances**: "una de las mejores" conductas por consistencia. [PDF: módulo Price Inefficiencies]
- **BA (Breakout Accumulation)** como shifting point: sus zonas top/middle/bottom generan respuestas al retorno del precio — candidato a nivel de entrada/reacción. [IMG: Price Swings Continued p.3] Setup concreto: NO ESPECIFICADO EN FUENTES (pendiente vídeos).
- **CPS como setup**: [USUARIO] indica que existe un setup concreto llamado CPS, a trabajar más adelante. NO ESPECIFICADO EN FUENTES procesadas.
- **Respuesta en core liquidity base**: la mayor respuesta contraria tras un ciclo completo de run+reversión aparece en la core base del run original. [IMG: Price Swings Continued p.3] [IMG: The Price Run p.10]
