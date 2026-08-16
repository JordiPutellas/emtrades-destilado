> ❄️ SNAPSHOT CONGELADO v1 — commit 83c2493, 2026-08-16.
> NO EDITAR salvo error factual demostrable, con entrada en
> CHANGELOG_v1.md. Documento exclusivo del snapshot (sin versión viva en ../).

# v1 · Ontología de niveles y máquina de estados

> Parte del snapshot congelado v1 (ver 00_README_v1.md). Tres capas: (1) ontología de niveles, (2) máquina de estados del price swing, (3) capa de microestructura (DESCRIPTIVA). Etiquetas epistémicas según CLAUDE.md. Los huecos se dejan marcados; nada se rellena por inferencia.

---

## 1. Ontología de niveles

Principio organizador: **todo nivel es una liquidity base** — "simply an area where price was stable and trade was being facilitated", con **tres lados: top, middle y bottom** [VID-M2020: Session 13 @ 01:02:13–01:03:27] [CONFIRMADO] — pero **no todas las bases son equivalentes**: EM enumera shelf/inventory, apex top/bottom, BA y shifting point como **tipos por ubicación**, con características y entornos propios [VID-M2020: Session 8 @ 01:00:24–01:04:55] [CONFIRMADO]. El eje maestro de calidad es **core vs residual**, y es **relativo al timeframe del run** ("every single apex is classed as core liquidity relative to the timeframe of the price run" [VID-M2020: Session 12 @ 00:03:58]).

### Jerarquía

```
LIQUIDITY BASE (top / middle / bottom)                       [CONFIRMADO]
│
├─ CORE (base de origen del run; máxima respuesta)           [CONFIRMADO]
│   ├─ pickup / OP (primer pickup; valida el nivel)          [CONFIRMADO]
│   ├─ fractal apex retest                                   [CONFIRMADO]
│   └─ BA (breakout accumulation)                            [CONFIRMADO]
│       — los "three levels inside" del core (S12)
│
├─ SHELF (inventory del run; el último que creó extremo)     [CONFIRMADO]
│   ├─ ST / SB (shelf top / bottom como puntos de respuesta) [CONFIRMADO]
│   └─ estado: activo → tested → drained/washed              [CONFIRMADO]
│
├─ RESIDUAL (pockets débiles del recorrido; densidad relativa)[CONFIRMADO]
│
├─ FEEDER (nivel original al que el precio alimenta)         [CONFIRMADO]
│   └─ pickups derivados ("bay of liquidity", más débiles)   [CONFIRMADO]
│
├─ APEX BASE (horizontal del extremo) / ABR (su retest)      [CONFIRMADO]
├─ CBP (clean breaking point; "support turns resistance")    [CONFIRMADO]
├─ PoR (point of release; borde de salida y de retorno)      [CONFIRMADO]
└─ SR / SR flip (plano, distinto del shelf; "just SR")       [CONFIRMADO]
```

Niveles descriptivos fuera de la jerarquía funcional: **YO/WO/MO** y **HOTW** — etiquetas de referencia en charts, sin reglas de uso en 26 vídeos; [USUARIO] confirma que eran descriptivos, sin prioridad sobre shelf/CPS. HOTW = [INFERENCIA] en su expansión.

### Fichas (definición · trazado · drain · respuesta esperada · estado)

**Core liquidity base / CLB** [CONFIRMADO]
- Definición: base de origen del price run ("core liquidity base of price run A–B"); "the origin of this price run... the fractal core aka origin". [IMG: Price Swings Continued p.3] [VID-M2020: Session 13 @ 00:04:44]
- Anatomía interna: "within core areas of liquidity you have **the pickup, the fractal apex retest, and the BA** — three levels inside, quite significant"; se refinan por separado (stops de 2-3 pips pegados al nivel). [VID-M2020: Session 12 @ 00:03:04–00:05:35]
- Trazado: nivel = parte unpicked; refinado HTF→LTF hasta tick charts; borde en el release point. [VID-M2020: Session 14]
- Respuesta esperada: la mayor respuesta contraria tras el ciclo completo del run. [IMG: The Price Run p.10] Matiz M2020: response ≠ hold ≠ reversal.
- Drain: mecánica general de los 3 lados (abajo).

**OP — Original Pickup** [CONFIRMADO]
- "We actually call the pickup of a base the OP, the original pickup." [VID-M2020: Session 13 @ 01:04:15]
- Validación: "the original pickup is only validated **once price has grabbed the level and it's gone to the shelf**". [VID-M2020: Session 12 @ 00:30:31–00:30:43]
- Uso como invalidación: "price... ended up **taking out the original pickup — that's where our invalidation would be**". [VID-M2020: Session 14 @ 00:06:36] Un poke sutil más allá del low del OP "shifts the probabilities significantly" — la lección completa del poke: [NO-LOCALIZADO] (q7). [VID-M2020: Session 12 @ 00:30:17–00:32:26]
- Claim asociado: "in every successful apex, the original pickup will hold." [VID-M2020: Session 12 @ 00:10:02] → 30_claims_validables.md.

**Shelf** [CONFIRMADO]
- Definición: "bulk of the momentum pushing any single price move, every price swing has one" [PDF: Price Swings Continued p.8]; operativa M2020: "the **last inventory** that pushed price to new lows (highs)". [VID-M2020: Session 14 @ 00:09:15]
- Trazado: "**you draw the FULL shelf**, pay no attention to where it was picked off" — el shelf NO se refina; los niveles sí. [VID-M2020: Session 14 @ 00:07:19]
- Drain (criterio funcional S11.2): repeated grabs, top pickup, deep tests y aproximación al bottom; el diagnóstico se confirma cuando cada feed empuja menos, falla en alcanzar el core del fractal o requiere penetraciones crecientes; tras el break, los intentos residuales se secan rápido. [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50, 01:12:26–01:13:55] Threshold cuantitativo: NO ESPECIFICADO EN FUENTES.
- Wash shelf-specific temprano: top y bottom/middle picked = inventory de la región consumido; la salida es el SWE. [VID-PS: PriceSwing_04/08] [PRECURSOR: PS → refinado en M2020]; la etiqueta SWE es [SOLO-PS: no confirmado después].
- Respuesta esperada: mientras sostiene, el run continúa; washed = "probability of a washed area responding: **low**" [VID-M2020: Session 14 @ 00:34:51], con excepción contextual por CÓMO llega el precio [S14 @ 00:35:11] y regla relativa nivel-vs-llegada [DISCORD: Disc 6].
- Relación con inventory: dentro del midflow, "shelf or inventory, which is the same thing" (sinonimia funcional acotada al último base que creó extremo). [VID-M2020: Session 10 @ 00:08:06–00:08:45]

**Residual liquidity / residual levels** [CONFIRMADO]
- Definición: liquidez débil que queda tras un movimiento ("weak, bottomside unfilled, top picked"). [IMG: Price Swings Continued p.3, p.5]
- Es relativa, no cero: el criterio es **densidad residual**, no una vela grande aislada. [VID-M2020: Session 6 @ 00:34:22–00:37:07]
- Respuesta esperada: débil, absorbida en midflow; un middle/residual level solo justifica duración corta y respuesta local. [VID-M2020: Session 11 part 1 @ 00:38:22–00:41:40]

**Feeder / feeding liquidity** [CONFIRMADO]
- El nivel original al que el precio "feeds into", por oposición al pickup derivado. Ante la duda: "it's typically **the feeder, the original**". Cada pickup genera su "bay of liquidity", típicamente más débil. [VID-M2020: Session 14 @ 00:00:41–00:01:02]

**BA — Breakout Accumulation** [CONFIRMADO]
- "**The inventory, the liquidity base that pushed through the shelf** is the breakout accumulation." Retornos: primero = shelf retest; segundo = "child shelf retest". Las BAs pueden estar washed. [VID-M2020: Session 12 @ 00:02:14–00:03:04, 00:54:27–00:54:58]
- "BA is quite responsive — pero comprobar si está washed." Reglas de entrada: NO ESPECIFICADO EN FUENTES.

**Apex base / ABR** [CONFIRMADO]
- Horizontal del extremo; su retest típicamente precede shift + midflow junto al shelf flip. Tras causar shift, el área genera respuestas incluso si luego se atraviesa. [IMG: Price Swings Continued p.3] [PDF: p.8]

**CBP — Clean Breaking Point** [CONFIRMADO]
- Punto de ruptura limpia de una base; "support turns resistance", suele albergar base fractal contraria. Componente 11 del CPS. Puede responder antes de que el precio llegue a PoR/core: candidato untested, no entrada obligatoria. [IMG: Fractals _ Scaling p.2] [VID-PS: PriceSwing_02 @ 00:04:40–00:05:24] [CONFIRMADO: PS→M2020]

**PoR — Point of Release** [CONFIRMADO]
- Donde el precio se libera de la base e inicia el run (componentes 2 y 12 del CPS). Genealogía PS02: bodies/volumen se aquietan, el precio construye contra el borde y sale en skinny leg. [IMG: Tracking Unfilled Liquidity p.4] [VID-PS: PriceSwing_02 @ 00:01:20–00:02:57] [PRECURSOR: PS → refinado en M2020]

**SR / SR flip** [CONFIRMADO]
- Soporte/resistencia plano, distinto del shelf: "thats not shelf. just SR... its just SR flip. Reasoning — my eyes." [DISCORD: Disc 25.1]

### Mecánica transversal de drain (los 3 lados)

Si el precio alcanza el **bottom** de la base, toda su liquidez se da por consumida; solo queda la del último pickup (débil). La forma de SALIR importa: si absorbió todo al salir, el retorno no tiene combustible. "**The more we test the level, the weaker it gets** — the liquidity is being drained (finite, quantitative)." [VID-M2020: Session 13 @ 01:03:29–01:05:24] [CONFIRMADO]

Jerarquía por timeframe: "**higher time frame pulls more liquidity**" y "**HTF governs LTF**" [VID-M2020: Session 13 @ 00:13:52–00:14:17]; mecanismo: una vela diaria condensa 24–48h de volumen → pockets mayores; la granularidad LTF es artefacto de cotización a 5 decimales. [VID-M2020: Session 15 @ 00:07:01–00:10:57] [CONFIRMADO]

Distinción sin criterios en fuente: **responsive vs market-state-dependent levels** — enunciada, criterios NO ESPECIFICADO EN FUENTES ([IMG-TWIT: Inneficiency], q19).

---

## 2. Máquina de estados del price swing

Esqueleto = CPS de 13 componentes (plantilla Chris Lori/PTC adoptada por EM [IMG: Tracking Unfilled Liquidity p.4]); aquí como estados con transiciones y evidencia observable. **Fractal a toda escala**: la misma máquina corre en tick y en weekly; cada swing se analiza en su TF y se sitúa en la fase del swing superior [VID-M2020: Session 10 @ 00:14:08–00:29:20] [VID-M2020: Session 13 @ 00:17:41–00:21:18] [CONFIRMADO]. Advertencia doctrinal: price pause, apex retest, wash completo y fill exacto son **features posibles, no pasos obligatorios** [VID-PS: PriceSwing_09] [CONFIRMADO: PS→M2020]; y "when price does break midflow, before it continues, **it looks like an apex anyway**" — expectativas siempre múltiples/bayesianas [VID-M2020: Session 13 @ 01:26:45–01:28:02].

```
LLS ──(surge relativo)──▶ PRICE RUN ──(void)──▶ EXHAUSTION ──▶ APEX
 ▲                          │ midflow: inventory holds                │
 │                          │ technical break = 1ª debilidad          ▼
 │                          │ sideways → pop → PARABÓLICA      SHELF FLIP
 │                          ▼                                        │
 └── nuevo LLS ◀── REBALANCE (gap slip → last point ◀── SHIFT ── MIDFLOW
                    of liquidity / CLB retest)          (nuevo inventory
                                                         gobierna)
```

### Transiciones

**LLS → price run** [CONFIRMADO]
- Dispara: surge **relativo** de volumen ("just more than the volume keeping price stable") contra el estado de baja liquidez; en LLS el precio es máximamente susceptible a un run hacia cualquier lado, incluso contra sentimiento. [PDF: Low Liquidity State p.2, p.5] [PDF: The Price Run p.7]
- Confirma: run fino/skinny leg desde el PoR; tick frequency sube.
- Invalida (como run): el spike se seca y "vuelve a la base" (price spike sin continuidad). [IMG: The Price Run p.9]
- Timing del pop: NO ESPECIFICADO EN FUENTES (dirección tampoco — solo susceptibilidad).

**Price run → void / chain reaction** [CONFIRMADO]
- Dispara: el run golpea un área con poca/ninguna liquidez ("distinct levels": más allá de shelf, H/L de día/semana/mes, rangos LLS). [PDF: Liquidity Void p.6]
- Confirma: el movimiento se agrava y adelgaza ("chewing gum stretching out"), compound por stops.
- Consecuencia estructural: queda deuda — el tramo thinly traded por el que después rebalanceará. [PDF: Liquidity Void p.5]

**Midflow (estado sostenido del run)** [CONFIRMADO]
- Definición: "directional price move of imbalance, with the characteristic that **the inventory that's pushing price holds**". [VID-M2020: Session 13 @ 00:05:44]
- Confirma que sigue vivo: cada base válida sostiene; el precio "hardly pokes back INTO the shelf".
- Primera debilidad = **technical break**: ruptura del último base que creó extremo; NO obliga a reversal ni es trigger por sí solo; puede aparecer pronto, faltar, o quedar dentro del fractal mayor. [VID-M2020: Session 8 @ 01:25:00–01:27:52] [VID-M2020: Session 9 @ 01:16:49–01:45:46]
- Claim asociado: tras el primer break "typically won't continue for a long while after" → 30_claims.

**Break → sideways → pop → parabólica → exhaustion** [CONFIRMADO]
- Secuencia: primer break → sideways (drena inventario con multiple pick-offs) → "**after the sideways comes the pop**" → parabólica = último tramo. Variante sin break limpio: "it doesn't always have to break midflow, but it will typically be a sideways pop". [VID-M2020: Session 13 @ 00:18:38–00:19:57] [VID-M2020: Session 10 @ 00:46:46–00:47:03]
- Parabólica definida por **tempo de impresión** (flash-flash-flash, no forma de vela). [VID-M2020: Session 4 @ 00:00:00–00:01:31]
- Confirma exhaustion: delivery cada vez más fina que "reaches" al nivel; VVF: el volumen sube a clímax y "takes a cliff dive". [VID-M2020: Session 11 part 2 @ 00:17:06–00:18:56]
- Claim: "we typically don't see the parabolic leg be a leg of significance". → 30_claims.

**Exhaustion → apex → shelf flip → shift** [CONFIRMADO]
- Apex favorable: extremo aguanta, apex retest aguanta, shelf falla en empujar a nuevos extremos, se rompe el shelf y el precio **se estabiliza encima** antes del shift; en los más fuertes el shelf cae al primer intento. [VID-M2020: Session 13 @ 00:58:02–00:58:36]
- La debilidad del shelf se confirma **en la respuesta, no en la ruptura**. [VID-M2020: Session 12 @ 00:12:22–00:13:04]
- Lectura del nivel golpeado: el primer break típicamente golpea residual; el tipo de nivel que creó el extremo pondera si aguanta (residual → no; core → mayor probabilidad). [VID-M2020: Session 13 @ 01:28:30–01:29:49]
- Invalida (la hipótesis de giro): el extremo no aguanta; permanencia material dentro del apex; buildup que absorbe el extremo (pain trade legacy [PRECURSOR: PS → refinado en M2020]).
- Escala: "if it's a H1 price run, **you need a H1 shelf flip**" — flips fractales no combaten midflow HTF (pero sirven para el fill de extensiones, counter flow). [VID-M2020: Session 13 @ 00:13:13–00:15:07]
- Template de 4 variaciones de apex + gestión por variante: **anunciado y nunca entregado** — [NO-LOCALIZADO] (q4). Solo hay dos morfologías comparadas (reach limpio vs buildup/swipes) en S11.2.

**Shift → midflow nuevo** [CONFIRMADO]
- El otro lado toma control tras consumirse la liquidez que sostenía; "offers cause momentum change". [PDF: Price Swings Continued p.8]
- **Midflow es una EXPECTATIVA**: si no aparece tras el shift, reevaluar la idea. [PDF: Price Swings Continued p.7]
- Estructura stair-step: "extension, fill, new range, continuation extension...". [PDF: p.7]

**Rebalance → nuevo LLS** [CONFIRMADO]
- Vuelta por el tramo ineficiente (gap slip) hacia el **last point of liquidity** / core base, al agotarse el flujo. [PDF: The Price Run p.6–p.10] [PDF: Liquidity Void p.12]
- Sin timing automático: una ejecución algorítmica activa puede sostener la extensión sin fill. [VID-M2020: Session 6 @ 01:20:26–01:22:55]
- Diagnóstico **LIC**: exhaustion (basta el flujo contrario natural → solo rebalance) vs presión genuina (convicción post-shift) — decide target y gestión. [PDF: Liquidity Imbalance continuum p.1–2]
- En tendencia: **trending extension fill** = "no reversal, just rebalance to find sellers" — no confundir fill con giro. [IMG: Liquidity Void p.15]
- El ciclo se repite: nuevos LLS se forman sobre los previos, en todos los TF. [PDF: Low Liquidity State p.5]

### Ejes transversales (no dibujables en el diagrama)

- **Inventory**: "the stock, the momentum liquidity of a directional move" — designación dinámica: cada base que crea nuevo extremo pasa a gobernar. [VID-M2020: Session 8 @ 01:05:30–01:07:50] [CONFIRMADO]
- **Technical break**: ver arriba; cambia probabilidades, no activa ni confirma. [CONFIRMADO]
- **First touch vs retest**: EM prefiere first touch de la exhaustion; el retest del extremo vuelve a liquidez aún más débil (el first touch la consumió) — retest de core/origin es familia distinta. Es filtro personal/contextual, no ley. [VID-M2020: Session 10 @ 00:56:05–00:58:18] [VID-M2020: Session 9 @ 00:15:31–00:16:25] [CONFIRMADO]
- **Entornos**: trend/range es taxonomía insuficiente; midflow rápido/ineficiente vs lento/eficiente se operan de forma opuesta; tres métricas permanentes: **volatilidad, estado de liquidez, fase del swing**. Los entornos cambian "relentlessly" y determinan niveles útiles, duración, tamaño de respuesta, frecuencia y gestión. [VID-M2020: Session 13 @ 00:23:56–00:25:47, 00:53:20–00:57:33] [CONFIRMADO]
- **Detección del viraje de régimen**: "runs, **doesn't fill** — that's your first sign"; "extension beneath Asia range and continuing the trend is a very common characteristic of HTF inefficiency". [VID-M2020: Session 15 @ 01:00:00–01:06:07] [CONFIRMADO]

---

## 3. Capa de microestructura (DESCRIPTIVA)

> ⚠️ Esta capa explica POR QUÉ el precio se comporta como describe la máquina de estados. **NO es fuente de reglas operativas**: EM la enseña como fundamento ("if you want to trade these behaviors, first you have to know why they exist" [VID-M2020: Session 11 part 1 @ 00:34:42]) y el único puente operativo que él mismo declara es leerlo todo EN el precio ("you don't need volume data to see what's going on — it's present in the price").

- **OTC quote-driven vs exchange order-driven** [CONFIRMADO]: FX spot es bilateral (dealer cotiza, puede internalizar, last look, re-quote) frente al single book multilateral con CCP. [VID-M2020: Session 1] Fragmentación + phantom liquidity (misma liquidez duplicada entre ECNs). [IMG-TWIT: Screenshot_12]
- **Market-to-limit-order ratio** [CONFIRMADO]: el único absoluto — "market to limit order ratio moves price"; puede subir el precio habiendo más vendedores que compradores (depth ≠ volumen). [VID-M2020: Session 2 @ 00:26:04–00:45:17] [VID-M2020: Session 15 @ 00:11:01–00:13:36] "Limit orders are friction. Market orders are consumption." [DISCORD: Disc 60]
- **Latent liquidity / conversion rate** [CONFIRMADO]: la mayor parte de la liquidez está oculta (information leakage); conversion rate = "the rate the latent liquidity converts into orders" — rápida al acercarse el precio = absorción; nula = open book; se frena por incertidumbre; ligada a conviction/willingness. [DISCORD: Disc 21, 64–66]
- **Fast vs slow liquidity** [CONFIRMADO]: HFTs/PTFs/LPs (aversos en surges, dispersan liquidez) vs metaorders institucionales troceadas en el tiempo (aceptan peores precios por contrapartida). Warehousing y descarga de inventario crean vacuums. [IMG-MIET: Gold Ranges 5.1, Vol is a F of Av Liq 1, 3]
- **Mecanismo por timeframe** [CONFIRMADO]: el LP-responding-to-flow aplica a timeframes intradía/inmediatos; HTF = flujo autocorrelacionado + distribución de liquidez latente (macro/sentiment). "Price is fractal and similar behaviours are observed" aunque el mecanismo cambie. [DISCORD: Disc 18–20]
- **Volatilidad = f(liquidez)** [CONFIRMADO]: "whenever the market becomes volatile, the willingness to trade dissipates... volume rises, volatility rises because dealers don't want to get hit". [VID-M2020: Session 15 @ 00:02:24–00:03:08]
- **Por qué la estabilidad es el estado por defecto** [CONFIRMADO]: demanda two-sided no especulativa + minimización de costes → ejecución troceada y oculta por algos. [VID-M2020: Session 13 @ 00:43:35–00:45:29] La cifra "~80% del tiempo en rango" es claim NO VALIDADO, posible lore Lori/PTC (q12).
- **Event-driven** [CONFIRMADO]: los movimientos HTF más rápidos son event-driven (liquidez no comparece + hedging masivo + HFTs "jump the queue" + flujo pasivo vuelto agresivo). [VID-M2020: Session 13 @ 00:38:40–00:43:29]
- **Corrección C-001** [CONFIRMADO]: "Liquidity doesn't get transferred. Liquidity **follows**" — la liquidez entregada por el algoritmo persigue el precio; "transfer of liquidity" fue misnomer temprano [PRECURSOR: PS → refinado en M2020]. [VID-M2020: Session 10 @ 00:06:17–00:07:24]
- Base externa que EM citaba: literatura de microestructura (Stanford/EBS, Farmer, Oomen, BoC) — tercera pata del marco junto a PTC/Lori y observación propia (q16). [IMG-TWIT: Screenshot_2,3,8,13]
