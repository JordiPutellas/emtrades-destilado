# EMTrades — Mapa del método (Price Swing 10/10; cierre global en preparación)

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

- **LLS** (estado por defecto, ~80% del tiempo; fractal; por horario, pre-datos o macro): [01_principios](01_principios.md), concepto [LLS](02_conceptos.md).
- **Run** y su mecanismo institucional (troceo de órdenes, price-chasing, overshoot; corroboración parcial [PAPER]): [01_principios](01_principios.md).
- **Void / chain reaction** y dónde esperarlos (distinct levels: past shelf, H/L diario-semanal-mensual, rangos LLS): [01_principios](01_principios.md), [02_conceptos](02_conceptos.md).
- **Apex → shelf flip → shift → midflow** (midflow es una EXPECTATIVA: si no aparece, reevaluar): [02_conceptos](02_conceptos.md).
- **Rebalance** y diagnóstico **LIC** (¿exhaustion o presión? decide target y gestión): [01_principios](01_principios.md), [02_conceptos](02_conceptos.md).

## El esquema que ordena todo: CPS (13 componentes)

"Characteristics of a Price Swing" — expansión de CPS confirmada por el PDF y las dos capturas sueltas; la plantilla procede de Chris Lori / Pro Traders Club y fue adoptada por EM [IMG: Tracking Unfilled Liquidity p.4; IMG: sueltas]:

`1 Liquidity Base → 2 Point of Release → 3 Skinny Leg → 4 Price Pause (Shelf Bottom) → 5 Continuation Leg → 6 Consolidation Apex → 7 Retest H/L → 8 Apex Base (break) Retest → 9 Shelf Top/Bottom Retest → 10 Gap Slip → 11 Clean Breaking Point → 12 PoR (vuelta) → 13 Liquidity Base Bottom`

Uso: "Identify liquidity, use CPS to navigate through price & manage the trade." Glosario completo con índice: [02_conceptos](02_conceptos.md).

## Qué se opera (estado actual)

Setups S-01…S-09 —incluido Washed IV/CPL— + catálogo de EM (ABRs, shelf flips, swing retests de CLBs, void fills, midflow) + response areas de alta probabilidad + reglas de gestión del trade real de 2019 (stop 10 pips, shelf como primer target, "paying for the trade", stop a invalidación, compounds): [03_setups](03_setups.md) y [05_trade_examples](05_trade_examples.md).

Calibración clave: la MISMA zona es alta probabilidad con entrega ineficiente hacia ella (mejor aún tras SWE) y baja probabilidad con entrega eficiente.

## Cómo se aprende/ejecuta (proceso)

Itinerario de 3 pasos formalizado en M2020 S15: (1) aprender a ver swings, (2) aplicar el marco a precio vivo —trackear/explicar, añadir contexto y buscar respuestas— y (3) derivar cómo operar cada entorno/setup. Process building por componente (sample sets de 10/día) y tracking de unfilled liquidity a doble vía: [04_proceso](04_proceso.md).

## Estado de la destilación

- ✅ 17/17 PDFs procesados (extractos en `30_extractos/`).
- ✅ 26/26 vídeos transcritos y destilados (27,4 h; 693 frames). Corpus M2020 completo: 16/16 vídeos (~23 h 48 min). Price Swing completo: 10/10.
- ✅ Corpus visual completo: 237/237 capturas procesadas (incluye Discord 129/129 y CLP 12/12).
- El vídeo final Price Swing 10 no recupera los artefactos prometidos/recordados que faltaban; el cierre transversal separará dependencias perdidas, aclaraciones del usuario y claims para validación.
- Cierre y mapa de navegación del corpus: [cierre_m2020](../30_extractos/cierre_m2020.md).
- Dudas vivas: [90_preguntas_abiertas](90_preguntas_abiertas.md) · Conflictos: [91_contradicciones](91_contradicciones.md) · Ideas BTC (aparcadas): [92_ideas_btc](92_ideas_btc.md).
