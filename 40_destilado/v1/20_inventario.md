# v1 · Inventario de comportamientos y modelos

> Parte del snapshot v1. Clasifica TODO lo tradeable del corpus en tres categorías, sin promover nada. Detalle completo con fuentes: `03_setups.md` (copiado en esta carpeta). Marcas de motivo del hueco:
> - **[RETENIDO]** = RETENIDO POR LA FUENTE: EM declara tener el parámetro y no publicarlo → en fase 2 se CONSTRUYE.
> - **[NUNCA-FORMULADO]** = el corpus no lo aborda → puede que ni existiera como regla; algunos casos están doctrinalmente remitidos por EM a sample building propio (se señala), lo que es diseño pedagógico, no descuido de destilación.

---

## A. Comportamientos descriptivos (el corpus dice que ocurren; sin contrato de trade)

1. **Gaps & rebalances** — "una de las mejores" conductas por consistencia. [PDF: módulo Price Inefficiencies]
2. **Respuesta en core liquidity base** — máxima respuesta contraria tras el ciclo completo del run. [IMG: Price Swings Continued p.3] [IMG: The Price Run p.10]
3. **Shelf retest de continuación** — tras romper shelf con core/bases débiles: retest y continuación hacia midflow; no confundir con el fade de exhaustion. [VID-M2020: Session 11 part 2 @ 01:25:58–01:27:55]
4. **Template de variaciones de low** (precursor Twitter del template de 4 apexes) — "2 or 3 other predominant variations for lows... inside the accumulation at the low there's at least 5 trades". [IMG-TWIT: Reversal, Reversal 2]
5. **Poor highs/lows (unfinished auction)** — "more times than not it'll trade through it"; sin garantía de liquidez fresca detrás. [DISCORD: Disc 73, 77]
6. **Balanced liquidity / equilibrium** — condición de NO-trade direccional ("you'll get chopped up"); el edge exige distorsión activa. [DISCORD: Disc 80, 85–88]
7. **Dealing ranges + regla direccional** — "until we form a dealing range ABOVE the previous one I'd be v v cautious holding longs". [IMG-TWIT: Dealing Ranges]
8. **BA como nivel de reacción** — "BA is quite responsive", comprobar si washed; reglas de entrada [NUNCA-FORMULADO]. [VID-M2020: Session 12]
9. **Low volume nodes preservados como niveles** — "the market preserves history of low volume nodes as levels". [DISCORD: disc 28]
10. **VVF (large inefficient extension → exhaustion → extension fill)** — comportamiento nombrado, no setup autónomo. [VID-M2020: Session 7 @ 00:40:47–00:41:12]
11. **Trending extension fill** — fill en tendencia ≠ reversal ("no reversal, just rebalance to find sellers"). [IMG: Liquidity Void p.15]
12. **Drift de Asia y su fill** — "directional moves through Asia usually weak... often get filled"; "first run out of Asia is usually really weak and dries off". Ejecuciones reales en TE-05. [IMG-MIET: Asia trade 1-2, First Run out of Asia]

Menú declarado por el propio EM (mapea sobre lo anterior y los modelos): "Extensions, ABR, Shelf flips, Midflow, Swing Retest of CLB, Residual Liquidity Base responses... Void Fills". [IMG: Fractals _ Scaling p.8]

---

## B. Modelos incompletos (hay QUÉ y algo de CUÁNDO; faltan campos)

**S-01 · Midflow trading**
- QUÉ: continuación stair-step post-shift; respuestas contrarias absorbidas. ✓
- CUÁNDO: "wait for price to rebalance down to local liquidity base"; escala mínima H1. Trigger concreto: [NUNCA-FORMULADO].
- DÓNDE: [NUNCA-FORMULADO] (pista: midflow es expectativa — si no aparece, reevaluar).
- CÓMO: [NUNCA-FORMULADO] (solo "duración variable").

**S-02 · Counter flow trading**
- QUÉ: fade de pierna expuesta hacia base/inventario más cercano. ✓
- CUÁNDO: first touch de la exhaustion/thinnest point, midflow gobernante estable, llegada débil + VVF exhaustion. Trigger de vela: [NUNCA-FORMULADO].
- DÓNDE: hard stop [NUNCA-FORMULADO]; deterioro probabilístico descrito (cortar antes del stop si la liquidez esperada no está). ✓parcial
- CÓMO: regla de expectativa/target real (solo rebalance salvo bounce-preshift débil; target = último base; short holding times). ✓

**S-03 · Fade de PI dentro de fractal**
- QUÉ: fade de ineficiencia en área core dentro del fractal. ✓
- CUÁNDO / DÓNDE / CÓMO: [NUNCA-FORMULADO] ×3 (el clasificador tradeable vs non-tradeable es proceso empírico por modelo, no tabla universal — q2).

**S-04 · Trades dentro de apex HTF**
- QUÉ: swings LTF dentro del apex HTF mientras el big shelf flipa. ✓
- CUÁNDO / DÓNDE / CÓMO: [NUNCA-FORMULADO] ×3 (clave declarada sin parámetros: dónde/cuándo se seca el run HTF).

**S-05 · Fade de void spike / extensión más allá de H-L**
- QUÉ: spike ineficiente contra void → rebalance al last point of liquidity. ✓
- CUÁNDO: restricción explícita ("not all are tradeable"); trigger: [NUNCA-FORMULADO].
- DÓNDE: criterio condicional sobre el shelf del rebalance; stop: [NUNCA-FORMULADO].
- CÓMO: target implícito + diagnóstico LIC obligatorio + protocolo event-driven (Discord). ✓parcial

**S-06 · Operar alrededor del LLS**
- QUÉ: LLS como oportunidad antes/durante/después del break. ✓
- CUÁNDO: dos plantillas (anticipación / fade de la extensión) — la fuente avisa "this isn't explaining HOW". Triggers: [NUNCA-FORMULADO].
- DÓNDE / CÓMO: [NUNCA-FORMULADO] ×2.

**S-07 · Tres entradas sobre un nivel (plantilla general)**
- QUÉ: fade hacia el nivel / retest del apex tras breakdown / shelf flip trade. ✓
- CUÁNDO: parámetros por variante [NUNCA-FORMULADO] — **remitidos doctrinalmente por EM a exercising** ("over time you will come to know which entry is best").
- DÓNDE: zonas que "define our risk" en los legacy PS05-PS08; stops exactos [NUNCA-FORMULADO].
- CÓMO: seguimiento del espectro favourable/unfavourable; cuantitativo [NUNCA-FORMULADO].

**S-09 · Fade de Washed IV / CPL**
- QUÉ: morfología COMPLETA (consumo del inventario, CPL simétrica, fade atravesando la zona consumida; fractal en 4 escalas documentadas). ✓
- CUÁNDO: "once price runs off the consumption in the CPL im looking to fade" — trigger exacto y tipo de nivel: **[RETENIDO]** ("Of course i have developed trade parameters for when I'll step in, where, nature of the level I'll step in at etc" [IMG: CLP/ED6JtkLXsAEu4X4.png]).
- DÓNDE: **[RETENIDO]**.
- CÓMO: target declarado ("past the consumed inventory"); parciales/BE/trailing: **[RETENIDO]**.
- Consecuencia registrada en S-09: estos huecos no se pueden completar leyendo más material — nunca se publicó (q18 → [VALIDACIÓN]).

---

## C. Modelos operativos (los cuatro campos con contenido real)

**S-08 · Fade de agotamiento en nivel bueno (plantilla de 3 componentes)** — el único que califica, con un sub-hueco:
- QUÉ: fade simétrico de midflow debilitado — "extension into core liquidity, in the parabolic phase or after a break of midflow, of a H1 price swing". ✓ [VID-M2020: Session 13 @ 01:14:18–01:14:54]
- CUÁNDO: invariantes + 3 variantes de activación reconciliadas (break+parabólica+first touch / sideways-pop sin break / break temprano=contexto); ejecución con buy/sell limit en el nivel. ✓
- DÓNDE: stop detrás del nivel; el nivel/OP debe aguantar (TE-02: 2.6 pips). **Distancia universal: [NUNCA-FORMULADO]** (los ejemplos reales usan 1.8–10 pips). ✓con-hueco
- CÓMO: el bloque más rico del corpus — cushion/manageable response, tracking bayesiano winner/loser, cortar/descargar si rompe midflow en contra, target mínimo (atravesar washed) y extendido (core), ponderación por hora del día, riesgo del cushion ausente. ✓
- Condiciones de evitación documentadas + distinción crítica de expectancy (nivel golpeado ES el parámetro). ✓

Base empírica: 5 TEs (2019-2020, GBPUSD) — especificación de comportamiento, NO evidencia de edge (ver 05_trade_examples.md).

---

## Tabla resumen (mapa de trabajo de la fase 2)

| Categoría | Nº | Entradas |
|---|---|---|
| A. Comportamientos descriptivos | 12 | lista arriba |
| B. Modelos incompletos | 8 | S-01…S-07, S-09 |
| C. Modelos operativos | 1 | S-08 (con 1 sub-hueco) |

| Motivo del hueco | Campos vacíos | Dónde |
|---|---|---|
| **RETENIDO POR LA FUENTE** | 3 | S-09: trigger/nivel, invalidación, gestión intermedia |
| **NUNCA FORMULADO** | 21 | S-01 ×3 · S-02 ×2 · S-03 ×3 · S-04 ×3 · S-05 ×2 · S-06 ×3 · S-07 ×3 · S-08 ×1 · A-8 (entrada BA) ×1 |

Lectura operativa: lo RETENIDO tiene morfología completa y se construye en fase 2 desde ella; lo NUNCA FORMULADO exige primero decidir si el comportamiento merece un contrato (y varios están doctrinalmente remitidos a sample building del propio trader — el método de EM QUIERE que esos parámetros salgan de samples, no de reglas publicadas: [VID-PS: PriceSwing_10] [PDF: Process Over Profits p.5]).
