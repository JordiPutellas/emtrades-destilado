# Extracto — Liquidity Void.pdf

> **Fuente:** `00_fuentes/pdfs/Price Delivery/Liquidity Void.pdf` (16 diapositivas: "Liquidity Voids & PI"). Define el liquidity void, la chain reaction y dónde esperar voids. Contiene el primer criterio explícito de gestión sobre un shelf (ejemplo Gold).

## 1. Definición y chain reaction

- "Price behaviour changes when it hits a liquidity void, setting off chain reactions in price which we like to engage." [PDF: Liquidity Void p.1]
- "**Liquidity void is referring to areas in price where there is less liquidity or a complete void.** When price hits an area of liquidity void it compounds the move that's already running." [PDF: p.6]
- CHAIN REACTION [PDF: p.5]: "When price starts to become inefficient, whilst seeking liquidity, the move gets thinner & thinner leaving it subject to drying out or getting absorbed — **like a chewing gum stretching out and breaking**. After the move dries out, because of the WAY price was delivered (inefficiently), **price bleeds through the liquidity void and rebalances to the nearest yet thickest area before its next move**. Regardless of the trend or sentiment, this is the constraint for price from a market microstructure & liquidity POV."
- "Note the change in price behaviour, how price stretches out leaving it highly vulnerable to drying off & rebalancing lower = chain reaction." [PDF: p.3]

## 2. Dónde esperar voids ("distinct levels")

- "There are a few areas where liquidity voids are likely to be present, we'll call them **distinct levels**: past a shelf, or a high or low. Past a high there can even be buystops, whilst price is seeking sell liquidity, which can compound a surge into a liquidity void making it more inefficient — **we like to fade inefficiency & extensions past highs & lows**." [PDF: p.6]
- "Also likely past current day highs/lows, weekly, monthly, swing highs/lows, shelf inventory, low liquid state ranges." [PDF: p.6]
- "Horizontal black line @ swing high or low = liquidity void past the H/L." [IMG: p.13, GBPUSD 5min con círculos en spikes que atraviesan H/L y rebalancean; IMG: p.14, mismo mapeo en H1]
- "Price direction and surges do not reflect mass sentiment. A surge of orderflow can generate a price move in opposition to perceived sentiment, and itself can cause a shift in sentiment. **Price pushes to the less liquid side of the market**, that's why surges and inefficiencies are consistently being filled, drawing through thin spots/voids **to the last point of liquidity**." [PDF: p.6]

## 3. Ejemplos anotados

- GBPUSD t5 [IMG: p.2]: "Bids are running through, pushing on price but price is in relative stability → shot of buyside liquidity, RELATIVE spike & price gets pushed out inefficiently, seeking liquidity → liquidity void on sell side, remember buyers need sellers to fill market orders coming into market."
- Esquema conceptual [IMG: p.4]: "Buy liquidity base, price picked up the topside → Low Liquid State (con fractal LLS dentro) → price hits a liquidity void on the sell side PAST the shelf and starts to spread out, too many bids present, not enough sellers → price stretches out (green dots), liquidity getting thinner, leaving gaps = price inefficiency → **the bids become too thin and can't hold up the price swing anymore and price rebalances lower**. SHELF = bulk of left over sell inventory of the move down. **Residual sell liquidity doesn't have to be strong, just thicker than the buy liquidity pushing into the level.**"
- Sesión completa GBPUSD 5min [IMG: p.7]: "These moves are functions of natural flows... price is constantly hitting liquidity voids, stretching out, becoming inefficient & then drying off the rebalance — **all day long**. Even though buyers eventually bid this higher, we have multiple, volatile moves lower = volatility is a function of available liquidity."
- **Gold 2min** [IMG: p.8] — primer criterio de gestión explícito sobre shelf: "Price pushes past (a high), hitting liquidity void and stretches out inefficiently before drying off and filling back down to last point of liquidity (red box). **If price starts trading back below this red box, shelf, we are likely to see lower prices. If it can still hold this red box and continue to new highs, all depends on broader state of liquidity. BUT the inefficient spike and rebalance after hitting liquidity void is a highly consistent price behaviour, one we will use to catch highs and lows and also counter trend trades.**" También: "Void spike and rebalance to last point of liquidity" (dos casos previos en la misma sesión); "A high, where sellers are inside likely trying to defend their position. Buy stops past the high."

## 4. Voids event-driven [PDF: p.11]

- "Around big data, central bank speaks, NFP we see **liquidity draw further away from price/TOB**. It then doesn't take a lot of weight to push price on either side, to cause a liquidity seeking inefficient move which is still subject to rebalance. This explains the spikes around data events."
- "**If there is a big surprise in the data which the market isn't expecting, we can see price continue to reprice aggressively for a while — so it's important to make note of consensus and result.**"
- Ejemplo NFP [IMG: p.10]: "Low liquid state ahead of data → liquidity drawing out of the market, likely a liquidity void on either side → shot on the buy side → sell liquidity thinly spread out, price chasing it & spreading out itself → liquidity void left behind as price became inefficient on the way up → rebalance in liquidity, buyers step in → repeat."

## 5. Extensiones: asimétricas pero no todas tradeables

- Conceptual breakdown de LV past highs/lows [PDF: p.12]: "After price has extended past a high in an inefficient way, forming a liquidity void in the extension leg, price is subject to a rebalance **back to the last point of liquidity**. At that point price may break down or build up and continue depending on how strong buyers are, trend & mass sentiment. **We want to take note of extensions as these provide asymmetric trade opportunities; not all are tradeable — our job is to spot & trade the ones that are.**"
- Daily GBPUSD [IMG: p.15]: "**Trending extension fill aka short extension fill — no reversal, just rebalance to find sellers**: price extending into sell inventory in a down trend = sellers step in & continue pushing lower. Trend shifts to downside: every time price extends past lows it fills the leg but sellers continue to push. Long term swing extension fill & new short term trend."
- CONCLUSIÓN [PDF: p.16]: "One should validate these price behaviours after forming a comprehensive understanding of why the chain reaction takes place. These are highly asymmetric price behaviours **although they are not always favourable to take a trade based on — e.g. trend extension fill is not likely to generate a shift in the trend; sometimes the extension is big enough to take counter trend trade, often it's not.** We will take a deep dive into forming trade models around these price behaviours in due time."

## 6. Anclaje a principios [PDF: p.9]

- "Always relate back to principles... For liquidity voids: price inefficiencies are weak & subject to rebalance; extensions get filled; price seeks, finds & deals off liquidity."

## Aporta al destilado

- Definición formal de liquidity void + catálogo de ubicaciones esperables (distinct levels).
- Concepto **last point of liquidity** como target del rebalance.
- Primer criterio operativo condicional sobre shelf (Gold): recuperar/perder el shelf del rebalance decide sesgo.
- Distinción crítica **trending extension fill vs reversal**: el fill de una extensión en tendencia NO implica giro.
- Voids event-driven: liquidez se retira del TOB ante datos; sorpresa grande = repricing agresivo, no fade.
