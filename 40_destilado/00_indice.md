> 📝 DOCUMENTO VIVO. Se edita libremente.
> La versión congelada al cierre de la destilación está en
> v1/00_indice.md

# EMTrades — Mapa del método (corpus conservado completo)

> Documento de orientación vivo (2026-08). Todo lo afirmado aquí tiene fuente detallada en los maestros enlazados. Los vídeos M2020, más refinados, prevalecen sobre el material anterior en caso de conflicto.

## La idea en tres frases

El precio es una función de la liquidez disponible: la volatilidad sube donde la liquidez falta, y el precio va siempre al lado más débil ([01_principios](01_principios.md)). Cuando un run se entrega de forma ineficiente deja un vacío detrás y queda "en deuda": al secarse el flujo, rebalancea por ese vacío hasta el último punto de liquidez. Todo esto es fractal — la misma anatomía a todas las escalas, solo cambian distancia, tiempo y volatilidad — y se opera de forma **anticipatoria, sin confirmación**, leyendo la fase del swing y el estado de la liquidez.

## El ciclo canónico (fases y dónde está cada una)

```
   LLS ──▶ surge relativo ──▶ PRICE RUN ──▶ void / chain reaction ──▶ APEX
    ▲      (un lado pesa      (skinny leg,    (se estira "como          (top: consolidation
    │       más que el         price pause,    chicle", compound         apex, AB, ABR)
    │       volumen del        continuation    past shelf/H-L)               │
    │       rango)             leg/parabólica)                               ▼
    │                                                             SHELF FLIP + SHIFT
    │                                                             (el otro lado toma
    │                                                              control; shifting
    │                                                              point = decision pt)
    │                                                                        │
    └─── nuevo LLS ◀── respuesta en CLB ◀── REBALANCE (gap slip) ◀── MIDFLOW (stair-step,
         (el ciclo se        (core liquidity     por el vacío a           extension-fill-
          repite en           base del run       last point of            new range; las
          todos los TF)       original)          liquidity                respuestas contra
                                                                          flujo se absorben)
```

- **LLS** (estado por defecto; fractal; por horario, pre-datos o macro): [01_principios](01_principios.md), concepto [LLS](02_conceptos.md). ⚠️ El "~80% del tiempo" es un claim **NO VALIDADO** en el corpus — posible lore de Lori/PTC: jarredroyce lo cita como enseñanza de Lori ("80%") en [DISCORD: Inefficiency conversation]; ver [90_preguntas_abiertas q12](90_preguntas_abiertas.md).
- **Run** y su mecanismo institucional (troceo de órdenes, price-chasing, overshoot; corroboración parcial [PAPER]): [01_principios](01_principios.md).
- **Void / chain reaction** y dónde esperarlos (distinct levels: past shelf, H/L diario-semanal-mensual, rangos LLS): [01_principios](01_principios.md), [02_conceptos](02_conceptos.md).
- **Apex → shelf flip → shift → midflow** (midflow es una EXPECTATIVA: si no aparece, reevaluar): [02_conceptos](02_conceptos.md).
- **Rebalance** y diagnóstico **LIC** (¿exhaustion o presión? decide target y gestión): [01_principios](01_principios.md), [02_conceptos](02_conceptos.md).

## El esquema que ordena todo: CPS (13 componentes)

"Characteristics of a Price Swing" — expansión de CPS confirmada por el PDF y las dos capturas sueltas; la plantilla procede de Chris Lori / Pro Traders Club y fue adoptada por EM [IMG: Tracking Unfilled Liquidity p.4; IMG: sueltas]:

`1 Liquidity Base → 2 Point of Release → 3 Skinny Leg → 4 Price Pause (Shelf Bottom) → 5 Continuation Leg → 6 Consolidation Apex → 7 Retest H/L → 8 Apex Base (break) Retest → 9 Shelf Top/Bottom Retest → 10 Gap Slip → 11 Clean Breaking Point → 12 PoR (vuelta) → 13 Liquidity Base Bottom`

Uso: "Identify liquidity, use CPS to navigate through price & manage the trade." Glosario completo con índice: [02_conceptos](02_conceptos.md).

## Jerarquía de niveles (qué responde, qué se drena)

Todos los niveles son liquidity bases, pero no equivalentes: **core** (base de origen del run; máxima respuesta al retorno; "every single apex is classed as core liquidity relative to the timeframe of the price run") frente a **residual** (pockets débiles cuyo criterio es densidad relativa; sus respuestas se absorben en midflow), más los tipos por ubicación: **OP, feeder, BA, shelf/inventory y shifting point**. El drain es funcional, no binario: repeated grabs, deep tests y feeds que empujan cada vez menos consumen el inventario hasta el break; tras él, los intentos residuales se secan rápido. Definiciones y reglas de drain: [02_conceptos](02_conceptos.md).

## Capa de microestructura (por qué el mecanismo es ese)

Debajo del marco hay una capa de mercado real: FX es OTC quote-driven (last look, internalización, liquidez fragmentada/phantom) frente a exchange order-driven; el único absoluto operativo es el **market-to-limit-order ratio** (el precio puede subir habiendo más vendedores que compradores); y la mayor parte de la liquidez es **latente/oculta**, con un **conversion rate** que decide si un nivel absorbe el movimiento o queda open book (M2020 S1–S3, S12 + Discord). [01_principios](01_principios.md) · [02_conceptos](02_conceptos.md).

Eje transversal de ejecución no dibujado arriba: **inventory / technical break / first touch vs retest** (S8–S11) — es el eje sobre el que pivota S-08 hoy ([03_setups](03_setups.md)).

## Qué se opera (estado actual)

Setups S-01…S-09 —incluido Washed IV/CPL— + catálogo de EM (ABRs, shelf flips, swing retests de CLBs, void fills, midflow) + response areas de alta probabilidad + reglas de gestión del trade real de 2019 (stop 10 pips, shelf como primer target, "paying for the trade", stop a invalidación, compounds): [03_setups](03_setups.md) y [05_trade_examples](05_trade_examples.md).

Calibración clave: la MISMA zona es alta probabilidad con entrega ineficiente hacia ella (mejor aún tras SWE) y baja probabilidad con entrega eficiente.

## Cómo se aprende/ejecuta (proceso)

Itinerario de 3 pasos formalizado en M2020 S15: (1) aprender a ver swings, (2) aplicar el marco a precio vivo —trackear/explicar, añadir contexto y buscar respuestas— y (3) derivar cómo operar cada entorno/setup. Process building por componente (sample sets de 10/día) y tracking de unfilled liquidity a doble vía: [04_proceso](04_proceso.md).

## Snapshot congelado: EMTrades reconstruido v1

**El corpus está congelado como [v1/](v1/00_README_v1.md)** (2026-08-16): ontología de niveles y máquina de estados ([10_ontologia](v1/10_ontologia.md)), inventario A/B/C de comportamientos y modelos ([20_inventario](v1/20_inventario.md)), 38 claims falsables ([30_claims_validables](v1/30_claims_validables.md)) y test ciego de comprensión ([40_test_comprension](v1/40_test_comprension.md)), junto a la copia congelada de todos los maestros. **Relación:** los ficheros de este directorio (00-93) siguen siendo los documentos VIVOS y pueden evolucionar; `v1/` es inmutable salvo error factual demostrable (con changelog en su README) y es la referencia citable para la fase 2. Toda evolución doctrinal irá a los maestros vivos y, en su día, a v2.

## Estado de la destilación

- ✅ 17/17 PDFs procesados (extractos en `30_extractos/`).
- ✅ 26/26 vídeos transcritos y destilados (27,4 h; 693 frames). Corpus M2020 completo: 16/16 vídeos (~23 h 48 min). Price Swing completo: 10/10.
- ✅ Corpus visual completo: 237/237 capturas procesadas (incluye Discord 129/129 y CLP 12/12).
- ✅ Corpus fuente conservado procesado íntegramente. No quedan PDFs, vídeos ni capturas pendientes de destilar.
- Cierres transversales: [M2020](../30_extractos/cierre_m2020.md) · [Price Swing](../30_extractos/cierre_price_swing.md).
- Próximas fases posibles —todavía no iniciadas—: aclaraciones de Jordi, recuperación/genealogía externa opcional o validación empírica. La clasificación canónica está en [_pendientes](../30_extractos/_pendientes.md).
- Dudas vivas: [90_preguntas_abiertas](90_preguntas_abiertas.md) · Conflictos: [91_contradicciones](91_contradicciones.md) · Ideas BTC (aparcadas): [92_ideas_btc](92_ideas_btc.md) · Contexto de usuario, no doctrina: [93_contexto_usuario](93_contexto_usuario.md).
