# Extracto — fx-liquidity-seeking-ls.pdf [PAPER]

> **Fuente:** `00_fuentes/pdfs/Papers/fx-liquidity-seeking-ls.pdf` (2 páginas). **Contexto teórico EXTERNO, no material de EMTrades**: ficha de producto de HSBC (sept. 2019) del "FX Liquidity Seeking (LS) Algorithm". Sirve para contrastar las afirmaciones de microestructura de EM con documentación de un LP real.

## Qué describe el documento [PAPER: HSBC FX LS]

- "Similar to a floating iceberg order which aims to execute passively whilst **hiding the true extent of a client's execution interest**. This is achieved by **splitting the total order size into smaller slices scaled to current market liquidity** and by passively placing these slices at different prices across HSBC's network of FX liquidity pools, **thereby tracking the market until the whole order is executed**."
- "By tracking the market with these successive limit orders, the algorithm **minimises footprint in the market as well as probability of adverse selection and high-frequency trapping**."
- Estilos de ejecución: **Passive** (órdenes más pequeñas, más profundas en el libro, más tiempo), **Neutral** (child orders cerca del top of book pasivo), **Aggressive** ("orders inside the spread... larger quantities per unit of time, resulting in a shorter execution time").
- "**Execution will ultimately always be liquidity-dependent** — if the market becomes distressed, the algorithm may fail to complete the order."
- "The market might move considerably during the execution."
- "HSBC may be active in the market with its own orders at the same time as client orders... they may interact in the market and compete for the same liquidity."

## Contraste con las afirmaciones de EM

**Apoya:**
1. "Providers split big blocks of orders into smaller pieces to match them with counterparties as efficiently as possible without materially affecting the market" [PDF: The Price Run p.8] ← corroborado casi literalmente ("splitting the total order size into smaller slices scaled to current market liquidity... minimises footprint").
2. La existencia de "liquidity seeking algorithms" que persiguen liquidez hasta completar la orden — EM: "price & liquidity seeking algorithms to fill the new order" [PDF: Low Liquidity State p.2] ← el producto se llama literalmente "Liquidity Seeking Algorithm" y "tracks the market until the whole order is executed".
3. Ejecución dependiente de liquidez y sin garantía de precio ("the market might move considerably during the execution") — consistente con "flows chase the quotes & are forced to take higher prices" [PDF: The Price Run p.8].
4. Liquidez oculta/iceberg ("hiding the true extent of interest") — da base real a la dificultad de "ver" la liquidez y a la necesidad de inferirla por comportamiento (tracking unfilled liquidity). [INFERENCIA]
5. El estilo Aggressive (dentro del spread, más cantidad por unidad de tiempo) es el perfil de flujo que EM describe como surge que dispara runs. [INFERENCIA]

**No cubre / matiza:**
- El documento describe el lado *cliente-ejecución* (minimizar impacto), NO el mecanismo de *price-chasing defensivo de los pricing engines* que EM atribuye a los LPs ("widen spreads & their pricing engines start moving prices to avoid being clipped" [PDF: The Price Run p.1, p.8]). Ese mecanismo es plausible (protección anti-arbitraje/last look son práctica documentada en FX) pero **este paper no lo documenta** — la cadena causal exacta del overshoot queda como afirmación de EM sin fuente externa en el repo.
- Nada en el documento habla de voids, rebalances ni de que "price goes to the weaker side" — el apoyo es sobre los ingredientes (algos LS, troceo, iceberg), no sobre la dinámica de precio que EM deriva de ellos.

## Uso en los maestros

Referenciado en 01_principios.md (mecanismo institucional del run) con etiqueta [PAPER: HSBC FX LS]. No es material EMTrades: no genera entradas de glosario ni setups.
