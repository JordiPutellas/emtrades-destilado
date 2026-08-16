> ❄️ SNAPSHOT CONGELADO v1 — commit 83c2493, 2026-08-16.
> NO EDITAR salvo error factual demostrable, con entrada en
> CHANGELOG_v1.md. La versión viva de este documento está en
> ../05_trade_examples.md

# Trade examples (EMTrades — destilado)

> Trades reales documentados en el material, reconstruidos con su razonamiento completo. Las reglas de gestión extraídas de ellos están sistematizadas en 03_setups.md ("Gestión de trades").

## TE-01 · GBPUSD short, 31/07/2019, pre-FOMC [PDF/IMG: Trade Example _ Management]

**Contexto (por qué):**
- La subida previa corrió "through weak areas of sell liquidity in an exposed way", buscando fills hasta un pocket H1 de sell liquidity; runs ineficientes → sujetos a secarse y rebalancear. [p.1]
- Lectura del LLS previo: vendedores absorbidos en el nuevo pickup de liquidez compradora + higher low ⇒ lado vendedor débil ⇒ run alcista probable (así se anticipó la subida que luego se hizo fade). [p.2]
- Supuesto de trabajo: "price ranges around 80% of the time" — mientras el resto espera continuación, EM busca el fade. [p.1]

**Secuencia de trades:**
1. **First touch counter flow short** (p.3): pierna expuesta, primer toque, extremo bid-exhaustion del LIC. Expectativa: SOLO rebalance a inventario local (el swing previo recogió daily buyside ⇒ sin new lows esperables). El short "collapsed inside" el closest buy inventory.
2. **Short principal** (p.4): 1.22466, stop 10 pips. Confluencia: los 5 constituent features del run presentes (1 fractal base → 2 apex retest → 3 shifting point/release por sell liquidity débil no rellenada → 4 price pause → 5 continuation leg/parabolic phase = parte más débil), extremo bid-exhaustion del LIC, extensión.
3. **Gestión** (p.5–6): target 1 = shelf; parcial ahí ("paying for the trade", clave psicológica y por event risk FOMC); stop bajado a invalidación estructural (el high debía aguantar); al confirmar midflow, gestión suelta; compound evaluado y descartado por FOMC; multi-TF 1-5-15.
4. **Resolución** (p.6–7): FOMC = catalizador; venta continuada con midflow characteristics; invalidación tardía = "bottoming out at a mid price run level", improbable a las 1900 BST.

**Reglas que este trade fija (ver 03_setups.md · Gestión):** stop 10 pips, shelf como primer objetivo, regla del shelf washed, parcial discrecional, stop a invalidación, compound condicionado, contexto/event risk por encima de todo.

## TE-02 · GBPUSD long en vivo, 19/11/2020 [VID-M2020: Session 13]

**Contexto:** run bajista H1; break de midflow → extensión final muy ineficiente ("price went parabolic in his tick frequency, reaching for the level, stretching out") hacia un **fractal apex** (nivel bueno; "technically residual of this H1 price run" pero con estructura de apex fractal). [@ 01:08:51–01:16:08]

**Ejecución:** buy limit en el nivel; fill con slippage positivo en el low exacto; **stop 2.6 pips**; cerrado +38 pips (~14R) — cerrado "porque estaba en la call"; tarde en el día → no mantener overnight. [@ 00:50:16–00:50:46, 01:18:27–01:19:07]

**Plantilla extraída por el propio EM ("the three main components"):** extension into core liquidity + en fase parabólica o tras break de midflow + de un swing H1. Mismo día, trade análogo contra residual sin nivel = expectancy muy inferior "over a thousand samples". → S-08 en 03_setups.md. [@ 01:14:18–01:15:46]

**Frases operativas:** "My strategy is: **area of strength, move of weakness, I look for my manageable response. That's it.**" · "If you can make 7R 10 times a month, you're a genius." [@ 00:49:57–00:51:04]

## TE-03 · GBPUSD, anticipación pre-COVID documentada (feb-mar 2020) [IMG-MIET: 1.0–1.4, 2]

Proyección dibujada a mano el 26-feb-2020: extensión bajista hasta la daily buy base (~1.2725-1.2750) → giro en V hasta ~1.31. Serie de 5 pantallazos fechados mostrando el cumplimiento paso a paso hasta el high 1.32003 del 9-mar (~450 pips). Contexto H4: core area 1.3050-1.3200 como origen/imán. Es el patrón S-08 a escala HTF y la demostración más clara del enfoque anticipatorio en el material. (El 9-mar arrancó el crash COVID: la proyección murió justo al cumplirse — ejemplo de límite event-driven.)

## TE-04 · GBPUSD long post-COVID con compounding (mar-abr 2020) [IMG-MIET: GBP April, GBP screanshot]

Long real desde ~1.2290: pantallazo con +189.4 pips corriendo y **SL movido a -9 pips**; tweet del 2-abr: "Still long, **X2** atm" + la razón para mantener: "**runs like these typically end in parabolic phase — haven't had that yet**" (la ausencia de parabólica = señal de que el run no ha terminado). Confirma en real: compound a favor, stop a cuasi-BE, y la fase parabólica como criterio de salida.

Fuente del tweet con el chart completo: [IMG-TWIT: Screenshot_11] (2-abr-2020, 11:45) — GBPUSD H1 del crash COVID (1.14) a 1.24+ con los niveles del camino marcados; texto completo: "Runs like these you're seeing liquidity come in one sided (on aggregate) over relatively long period of time." Detalle: pestañas del workspace visibles — GBPUSD LTF · GBP/USD H1 · **XAU/USD M15 · XAU/USD D1 · USA500.IDX M15** → EM monitorizaba oro y S&P500 junto a cable.

## TE-05 · GBPUSD, fill del drift de Asia (20-abr-2020) [IMG-MIET: Asia trade 1-2]

Regla anotada: "Directional moves through Asia usually weak due to light volume & thin liquidity. **Often get filled** unless recent catalyst/aggressive sentiment shift." Ejecución en 1min: long 1.24530, **SL ~3.8 pips**, +21.5 pips. Variante intradía de S-08 con el drift asiático como extensión débil. Complemento (5-may-2020): "**first run out of Asia is usually really weak and dries off**" — fadeable ante absorción en el HOD (short +18.3 pips, SL -4.8). [IMG-MIET: First Run out of Asia]

## Candidatos evaluados y descartados

Auditoría 2026-08-16 (consulta acotada ±3 min por timestamp sobre `10_transcripciones/`). Criterio: un TE requiere **entrada + invalidación + gestión + resolución** juntas en la fuente; no se fabrican operaciones sintéticas ni se completan huecos por inferencia.

| Fuente | Qué muestra | Por qué se descarta |
|---|---|---|
| [VID-M2020: Session 8 @ 00:32:41] | "that area today where I took a short today" — usa el short del día para ilustrar condiciones de exhaustion (liquidez "super super stretched", weakness en bids por retirada de LPs) | Mención ilustrativa: sin entrada, invalidación, gestión ni resolución |
| [VID-M2020: Session 9 @ 00:06:20–00:07:30, 02:00:03–02:02:35] | Anécdotas del día ("I caught some nice trades early on... **Had to cut it for pretty much nothing**"); el nivel 1.29619 perdido ("I was on the shower... would have made you a week") con la regla de stop "**always past the level**"; la estrategia en dos palabras ("**fading weakness**... first touch of levels, extensions and inefficiencies only") | Todo es anécdota u hipotético; ningún trade reúne los cuatro campos. Lo doctrinal ya está en 03_setups/04_proceso |
| [VID-M2020: Session 11 part 1 @ 00:37:03–00:38:22] | Long real cuyo TP (sell limit) estaba "in an area where **I deemed it to be sell liquidity**"; un spike de ~35 pips en segundos lo llena ("price would have spent less than a second here") | Entrada = "long from somewhere earlier" (sin especificar) e invalidación ausente. Documenta la colocación de TP como limit en nivel, no un TE |
| [VID-M2020: Session 11 part 2 @ 01:25:33–01:28:25] | "**I actually shorted I think here, which is not my usual way of trading**" — contexto completo (low débil, break de shelf/último inventory, core evaluado débil desde la mañana) y desarrollo esperado (shelf retest → midflow → break) | Entrada imprecisa hasta para EM ("I think here"), sin stop y sin resolución declarada; la narración salta al breakout inesperado por headline (Brexit/pesca) |

**Nota de cierre:** La base empírica de gestión son 5 TEs (TE-01–TE-05, 2019–2020, GBPUSD). Insuficiente como muestra estadística; sirve como especificación de comportamiento, no como evidencia de edge.

**Contexto autobiográfico (no TE):** EM declara que su negocio habitual son varios trades pequeños de aprox. **25–36 pips en GBPUSD**, sin perseguir siempre el swing de 60–70 pips. Son datos autobiográficos, no targets del setup. [VID-M2020: Session 11 part 2 @ 01:52:20–01:54:14]
