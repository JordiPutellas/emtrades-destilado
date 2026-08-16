# Extracto — [VID-M2020] Session 14: Drawing Levels

> **Fuente:** `00_fuentes/videos/2020 Mentorship/Session 14- drawing levels.mov` (51:37). Screencast Dukascopy (GBPUSD, nov-dic 2020; fecha visible 2020-12-17 → confirma época M2020). Formato: clase práctica en vivo mentor↔alumno. Objetivo: reglas de trazado y refinado de niveles de unfilled liquidity + práctica de tracking en vivo.
> Responde la pregunta abierta "drawing & refining levels" (antes solo cubierta en teoría por Tracking Unfilled Liquidity Presentation).

## 1. Regla central: el nivel es la parte NO recogida (unpicked)

- "The new area of unpicked liquidity would have been there... price came down and grabbed the top, it basically fed into it" — cada vez que el precio "come" parte de un nivel, el nivel vigente pasa a ser SOLO la parte no recogida. [VID-M2020: Session 14 @ 00:00:16–00:00:36]
- "We can just constantly see price reaches for the part of the level that isn't picked up." [@ 00:02:18]
- Un nivel recogido desaparece: "that original level's gone... this was the last pickup of that level, that's holding the liquidity now." [@ 00:10:37–00:11:08] "You could easily be mistaken and draw that whole level but that's technically incorrect." [@ 00:11:08]
- **Cada pickup genera a su vez su propia liquidez** ("every pickup itself has a certain bay of liquidity"), pero es típicamente más débil. Ante la duda nivel original vs pickup: "you will have to try both and you'll find that it's typically **the feeder, the original**" — el original prevalece. [@ 00:00:41–00:01:02] → define "feeder" = el nivel original al que el precio alimenta (vs el pickup derivado).
- En el apex igual: "the original pickup, the retest — price feeds off this and not that; it will usually reach for that (el OP) and work its way there." [@ 00:18:49–00:19:06]

## 2. Procedimiento de refinado (HTF → LTF)

1. Identificar el área grande en el TF alto (15min): al principio "the level would originally start off like this because it looks like price ran out and picked it one time and continued". [@ 00:03:03]
2. Zoom: "when you zoom into it you find that there's numerous levels inside of the level itself. **That's where the refining comes into place.**" [@ 00:03:17]
3. Redibujar cada subnivel a su liquidez real: dónde recogió, dónde volvió a entrar ("price moved out, came back in → refine that level to that"). [@ 00:03:43–00:04:08]
4. Bajar a 5min y repetir; separar TODOS los niveles aunque estén a 4 pips. [@ 00:04:14–00:04:38]
5. Ajustar el borde al **release point**: "this release point is where likely the shot of volume came to push that candle through — I would readjust it (the level) down to the release point where the candle released out from." [@ 00:04:44, 00:13:08]
6. Resultado típico: "I've turned this whole 15 minute area into two levels." [@ 00:05:00] (Frames @ 00:03:35 y 00:04:16: caja única de 15min → dos cajas en 5min.)
- Si el tramo no se ve (baja volatilidad, fin de día): bajar hasta tick charts; "there's no difference to tick charts, they're just faster". [@ 00:37:39–00:38:02, 00:50:30]

## 3. El shelf se dibuja distinto

- "**You draw the shelf just like you draw a level, but you pay no attention to where it was picked off. You just draw the FULL shelf.**" [@ 00:07:19–00:07:28] (El shelf entero es el inventario; los niveles se refinan, el shelf no.)
- Shelf = "**the last inventory that pushed price to new lows**" [@ 00:09:15]; distinguir small shelf (del fractal) vs "the largest swing shelf". [@ 00:09:29–00:09:51]

## 4. Crítica a order blocks / breakers (ICT) — [VID-M2020: Session 14 @ 00:08:01–00:09:05]

- El alumno dibuja un "order block"/"breaker"; EM: "technically wrong... (la lógica del breaker) says that trapped shorts here end up being long. **You're only a trapped short if you're speculative. What if the sell liquidity there is from an entity that has no interest about where price goes — they just need to transact for operational purposes? That's the FX market.**"
- Sobre volumen retail: "our volume doesn't end up in the market... it gets dealed off internally with the broker; the broker builds up a risk position that they might hedge out later — that's not your volume moving the market."

## 5. Washed / drained y cuándo un nivel no vale

- Área agarrada repetidamente = "**washed and drained** — grabbed it grabbed it grabbed it... the only area that wasn't drained was this one". [@ 00:12:40–00:12:52]
- Significado: "lack of sell liquidity there — you shouldn't really have any problems to get through; it's possible we see weakness and price pushes through". [@ 00:27:27–00:27:41]
- "Do you know the probability of a washed area responding? **Low.**" [@ 00:34:51–00:35:01]
- PERO contexto manda: dos áreas washed — precio llegando con "strong midflow, becoming inefficient into it" vs precio que "broke midflow, broke shelf, sideways pop into it" → la segunda es más probable que responda. "They're both washed but the contextual environment is completely different." [@ 00:35:11–00:35:40]
- Áreas "drifty": "whenever you have these small drifty type areas they're typically going to be drained... picked so many times". [@ 00:16:09–00:16:22]
- La invalidación práctica de un trade sobre pickup: "we got this pickup, price failed to continue pushing higher and it ended up **taking out the original pickup — that's where our invalidation would be**." [@ 00:06:36–00:06:46]
- Respuesta "manageable" = ~7-8 pips: "a manageable (response) would be a good 7-8 pips that we can manage because that response gives us a cushion of profit and then it's very unlikely we'll take a full loss — we know the original pickup should hold." [@ 00:06:19–00:06:34]

## 6. Categorizar SIEMPRE cada nivel

- "Give them a categorization. Always, always... This is the top side of the original pickup, that's completely different to the shifting point that absorbed the bids, completely different to a residual, completely different to an apex retest." [@ 00:20:21–00:20:43]
- Ejemplo de mapa completo en vivo [@ 00:13:53–00:15:36]: "small shelf, big shelf; **this is technically a BA, but it's washed**; this is the original pickup; this is a fractal shelf retest; these would be shifting points — the small levels that pushed through the bids". (Frame @ 00:13:45: decenas de cajas en 1min.)
- **OP = Original Pickup** (sigla nueva, usada repetidamente: "OP", "OP present, original pickup"). [@ 00:18:42, 00:32:13]
- Variaciones de liquidity bases: "many many different types — some close together, some drifty, some leave a whole bunch of sell liquidity... **you need to test every single type many times over so you know which one's the best one to use**." [@ 00:22:01–00:22:58]

## 7. Selección: pocos niveles y filtro por cómo llega el precio

- "I'm drawing like 50 levels here — realistically I'll draw one or two, the only ones that are of interest." [@ 00:16:29–00:16:36]
- Filtro de no-trade: "price came to the first one, it wasn't moving the right way, so I took no trade... finally it moves the right way." Concretamente: llegar **eficientemente** al nivel = no trade; volverse **ineficiente** hacia el nivel = interesante. [@ 00:16:43–00:17:07]
- Tamaños de respuesta observados en el ejercicio: 6, 11, 17, 40, 50 pips; niveles de 3-5 pips de ancho. [@ 00:05:27, 00:13:30–00:13:41, 00:19:17, 00:20:01–00:20:11]
- "Bear in mind: doesn't mean that price will always respond." [@ 00:05:21]

## 8. Tracking en vivo (práctica modelo, segunda mitad de la sesión)

- Mantra: "**observe, don't predict**" [@ 00:29:44]; "I shouldn't go into the territory of forecasting — we're just observing what's going on". [@ 00:33:53]
- Todo nivel debe estar dibujado ANTES: "all these levels should be drawn on already... draw all these levels on before it happens, and if price ends up rolling over them **you're not wrong about anything — it just became inefficient. That's the risk of it: when it breaks a shelf it becomes inefficient.**" [@ 00:34:05, 00:51:08]
- Confirmaciones de debilidad leídas en vivo: "the fact that it responds off residual liquidity is a kind of confirmation of how weak this run is" [@ 00:40:53]; "I want to see price reflect the weakness in the bids — fail to move up, make multiple attempts, then price moves down. **That's the way I'm going to manage my trade.**" [@ 00:42:07–00:42:27]
- "Price could come all the way back up and I still want the high to hold... **you have to test how often your trade works after the original pickup was invalidated, whether there's any positive expectancy in that action.**" [@ 00:42:29–00:42:44]
- Combinatoria contextual: con ~5 componentes contextuales presentes a la vez, "what is the likelihood you're going to experience this exact dynamic 100 times so you know the exact way to trade it? Very unlikely" → por eso se aprende por componentes, no por escenarios completos. [@ 00:32:24–00:32:55]
- "The most favourable probabilities of a trade were just THERE (un punto concreto), not here, not there." [@ 00:41:33–00:41:42]

## 9. Entorno HTF midflow (dinámica "unusual")

- "This residual/fractal price run is located in a higher time frame bullish midflow. **Midflow means imbalance.** HTF bullish midflow means these inventories are packing a big punch... **buy liquidity is turning up at residual levels — at fractal runs which SHOULD be weak — indicative of greater HTF imbalance.**" [@ 00:45:27–00:46:58]
- "In every single midflow, liquidity is accepting higher and higher prices." [@ 00:46:11]
- Consecuencia operativa: en HTF midflow los residual levels rebotan y las rupturas de shelf fractal dan fills pequeños ("you typically get bigger fills, here you're seeing very small fills") — entorno "frustrante" pero real, hay que adaptarse. [@ 00:48:45–00:49:13]
- Señal HTF: "this forms the daily/H4 shelf and it wouldn't be too much of a surprise to have thick concentrated buy liquidity throughout this area **because we're in a higher time frame price run, which is unusual — not a normal dynamic**." [@ 00:44:40–00:45:06]

## 10. Tareas prescritas al alumno (método de práctica)

1. Elegir gráficos históricos al azar y marcar TODOS los puntos de respuesta ("just so you're visually aware that there's liquidity almost everywhere"). [@ 00:02:51–00:03:03, 00:21:00]
2. Dibujar y refinar niveles, mirar cómo respondió el precio, "don't cheat, do it over and over". [@ 00:23:06]
3. Tracking continuo como tarea de desarrollo ("your developmental task remains now tracking"), con intensidad: "have a shit on the toilet — track it; wake up in the middle of the night — track it". [@ 00:23:18, 00:50:08]
4. "You will learn more from tracking price than anything you've ever learned from me." [@ 00:50:02]

## C-001 (transfer of liquidity)

- En toda la sesión NO usa "transfer of liquidity" como mecanismo; el vocabulario es feeds/grabs/picks/washed/drained/absorbed. (Un solo uso coloquial de "fed into it".) → Apoya la tesis de que en M2020 el término mecánico ya no se usa.

## Nuevo vocabulario detectado

- **OP (Original Pickup)** — confirmado. **Feeder** — aclarado (el nivel original vs su pickup). **Washed/drained** — criterio operativo. **"Bay of liquidity"** del pickup. **Ramp** ("this was a ramp on the way out" @ 00:16:02 — por confirmar).
