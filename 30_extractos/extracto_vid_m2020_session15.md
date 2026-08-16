# Extracto — [VID-M2020] Session 15

> **Fuente:** `00_fuentes/videos/2020 Mentorship/Session 15-007.mov` (1:19:24). Fecha visible en plataforma: **2021-03-21** (la mentoría abarca nov-2020→mar-2021). GBPUSD semanal ~1.38.
> ⚠️ **El template de las 4 variaciones de apex NO está en esta sesión** (ver dependencias en _pendientes.md). Contenido real: repaso de principios y microestructura, formalización de los pasos de exercising (2.1/2.2/2.3), workspace de charts, y estilo de gestión de EM con dos trades reales abiertos.

## 1. Microestructura (repaso ampliado)

- Órdenes grandes se trabajan en piezas (limits + market) vía algos de ejecución; "because they're structured and because they're parameterized, **it results in quite consistent behaviors. Think about midflow: why does the last buy base hold? Because there's liquidity accepting higher and higher prices.**" [VID-M2020: Session 15 @ 00:00:30–00:01:48]
- "Whenever the market becomes volatile, **the willingness to trade dissipates**... volume rises, volatility rises because the dealers don't want to get hit, creates the spike type movement, and as the spike continues the willingness to trade disperses and the volume dries off... that's why price draws back into range." [@ 00:02:24–00:03:08]
- **Market-to-limit-order ratio** (principio con ejemplo numérico): dos traders comprando/vendiendo lo mismo en el mismo segundo pueden subir el precio si la liquidez pasiva de un lado es menor; "there can be more sellers than buyers and still price goes up — a super weird result of market dynamics". Ratio >1 en un lado = precio se mueve. [@ 00:11:01–00:13:36]
- Por qué HTF pulls more liquidity (explicación completa): una vela diaria = 24-48h de volumen transaccionado → pockets concentrados y liquidez residual mucho mayores; "the higher time frame trades over a longer period of time, more volume transacts, more interest is in it". La granularidad LTF existe solo porque se cotiza a 5 decimales; en los niveles súper granulares hay menos liquidez. [@ 00:07:01–00:10:57]
- "**Price reflects the state of liquidity — arguably one of the most important principles.** Whatever price does, we can interpret it to determine the current state of the market... and if we're tracking it, we can be the ones that spot those changes very very quickly." [@ 00:14:05–00:16:30]

## 2. Countermeasures to randomness (repaso sistematizado)

1. "**Tracking price very closely.**" 2. "**Consider multiple outcomes**, because at any time the market can just change." 3. "**A probabilistic approach** — think about what is much more likely... rather than having stringent expectations." [@ 00:17:40–00:23:28]
- La capacidad de considerar outcomes correctos requiere haber visto miles de variaciones ("observe a thousand apexes... you will have experienced the variations: apexes that fail, apexes that work through the shelf slowly, apexes that miss the retest and come back"). [@ 00:20:04–00:22:57]

## 3. Los pasos de exercising, formalizados [@ 00:42:01–00:54:31]

- **Step 1**: construir el sample set y la capacidad de VER price swings y sus features en cualquier variación ("some are subtle, some vague, others clear — you need to see all of them").
- **Step 2** (aplicar a precio vivo) tiene **tres sub-pasos**:
  - **2.1 Track & explain**: "just identify and explain what price is doing... don't think about where it's going next. Simply identify all the information you can" (fases, niveles, core, cómo se mueve).
  - **2.2 Contextualizar con HTF + anticipar**: usar los stages para anticipar; aparecerán los fallos de expectativa que obligan a considerar múltiples outcomes; los niveles "dejan de funcionar" cuando cambia el estado HTF → eso enseña a mirar el HTF.
  - **2.3 Buscar respuestas**: "you're actually looking for responses (trades)" — antes solo se observaba.
- **Step 3**: "coming up with steps or observations about **how to trade this environment or that setup** — how to trade an efficient environment, the characteristics, the types of levels that work... Step 3 is probably for you a while out."
- El exercising no termina nunca: "should continue for the rest of your trading career". Rutina de EM: cada mañana (y tras fines de semana) trackea y dibuja niveles para "get back in my groove... it reminds me of small details". Ejemplo de recordatorio: "**when price misses your level, I know not to chase — often it will end up spiking to it later. I'll stay patient.**" [@ 00:54:31–00:55:59]

## 4. Workspace de charts de EM [@ 00:56:22–00:57:45] (frame @ 00:57:16)

- **Local PA** (chart de tracking del día, 1min/5min) · **Levels** (chart separado solo para identificar/refinar niveles históricos sin scrollear) · **HTF** (H1/H4/daily) · **Higher-higher TF** (weekly, separado "porque no quiero un weekly shelf estirado como caja negra en mi H1").

## 5. Filosofía de edge [@ 00:27:41–00:32:23]

- Pattern-fitting sin mecanismo (medias móviles, RSI) = riesgo de que el patrón muera sin avisar; caso real: prop traders que "ladder-tradeaban" noticias perdieron el edge en cuanto llegaron los algos ("his edge disappeared one second ago").
- Modelos matemáticos = lagging por construcción; "you have to be forward looking... we take a **probabilistic anticipatory approach trading the properties of price behaviors which are a result of market mechanisms**."
- "We don't care where the market goes, we care about its behavior. If it's going from A to B, I don't care — **I care HOW it's going to get there**... Ultimately **we're trading the volatility**, not taking directional bets."
- Contra la predicción de valor: quants con satélites contando coches en parkings de Walmart — "we can never compete with that".

## 6. Trades reales abiertos (estilo de gestión)

- **Short GBPUSD desde 1.42004** (retest del daily shelf tras romperlo): +250-300 pips, cerró la mayoría el primer día, dejó **0.8 lots como runner**. "I'm not a swing trader. We're trading the volatility: price spikes up, we short it, it moves 3-4-5R intraday, take my money." [@ 00:33:26–00:35:15]
- **Long WTI desde $5** (CFD; el contrato real llegó a negativo — explicación de por qué los CFD cotizan distinto del exchange): "months, bro... only 0.5 lots on. It's absolutely mental to think I would sit there for 12 months with full size — no one's doing that unless you're a fund." [@ 00:35:45–00:41:50]
- **Matemática del runner**: "for you to get that 10R trade you will probably have had 3-4 trades that hit 3-5R and went back on you... when you're looking for runners you're going to have more trades that fail; when you trade my way (take your money) there's going to be that one trade you close that would have run a thousand." Runner solo cuando la **ubicación HTF** lo justifica: parcial + dejar un trozo + olvidarse. [@ 00:37:06–00:39:16]
- Caso cable (nov-feb): entorno HTF eficiente = "close your eyes, it comes back into profit, it's forgiving"; cuando vira a ineficiente: "if you don't spot the change, you mess up". Primer aviso del cambio: "runs, **doesn't fill** — that's your first sign"; luego "extension beneath Asia range and continuing the trend is a very common characteristic of higher time frame inefficiency". Sus dos shorts fallidos en ese viraje: BE + small loss ("my high becomes the invalidation"). [@ 01:00:00–01:06:07]
- **Flash spike** (spike overnight en low liquidity): "if you shorted here you're down... probably account gone if over-leveraged, your stop would have got slipped 100%... luckily that was at 1am and I'm not trading." [@ 01:02:21–01:03:28]

## 7. Niveles como sensor de régimen

- "When the levels are going to work, they respond — it will be very easy to trade. When it doesn't respond, that itself is giving you information about the new state... and when it's the time that it runs out, none of these levels are going to work and you'll see them get rolled over." [@ 01:17:59–01:18:44]
- HTF governs aplicado: en HTF bullish midflow eficiente, los fractales internos NO deberían rellenar a core ("if it filled, it wouldn't be relatively inefficient"). [@ 00:43:00–00:43:38]

## 8. Otros

- FX no es una asset class sino "a conduit to access different asset classes" — no forma burbujas como los risk assets; dinámica narrativa de burbujas (price up → reason → buy more). [@ 00:48:38–00:50:52]
- C-001: **sin rastro de "transfer of liquidity"** en toda la sesión.

## Dependencia NO resuelta

- El template de las **4 variaciones de apex** + gestión de trades en apex + "second level information" (prometido en Session 13 @ 01:45:10 para "next session") no está en Session 14 ni en Session 15. Dado el salto temporal (S14 dic-2020 → S15 mar-2021) pudo entregarse fuera de las grabaciones (como archivo del drive). Candidatos: capturas sueltas (`Inverted Fractal.png`, carpetas EM Twits/Most Important EM Trades) o Sessions 1-11 si la numeración no es cronológica. → anotado en _pendientes.md.
