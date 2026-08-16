# Cierre transversal — corpus Price Swing

## 1. Propósito y autoridad

**Cobertura:** 10/10 vídeos destilados, con transcripciones/SRT completas y 175/175 frames indexados revisados. Los charts, deícticos, ejemplos, entradas y errores relevantes se contrastaron con vídeo/audio.

Price Swing es la capa temprana del método. Su valor es genealógico: fija la morfología original, muestra precursores de los modelos posteriores y revela vocabulario corregido o abandonado. Jerarquía obligatoria: `M2020 > Price Swing > PDFs`.

## 2. Anatomía y vocabulario temprano

La secuencia legacy queda reconstruida como:

`core liquidity base → point of release → skinny leg → price pause → continuation leg → shelf/SWE → consolidation apex → apex base/retest → shelf flip/shift → midflow → fill/rebalance`

- **Core liquidity base:** origen con liquidity relativamente gruesa que inicia el drive; no confundir con pequeños residual levels del recorrido. [VID-PS: PriceSwing_02 @ 00:02:27–00:03:16]
- **Point of release:** borde desde el que el precio sale tras contracción/buildup; top, middle, bottom y clean breaking point son refinamientos candidatos cuya validez depende del sample. [VID-PS: PriceSwing_02 @ 00:01:20–00:02:57] [VID-PS: PriceSwing_02 @ 00:08:43–00:09:46]
- **Skinny leg / price pause / continuation:** delivery fina; estabilización en residual liquidity; nuevo buildup/absorción y extensión. La pause puede dar fill local sin reversal. [VID-PS: PriceSwing_03 @ 00:08:10–00:12:31]
- **Shelf / inventory:** base que sostiene el flow; top, middle y bottom pueden consumirse. Shelves anidados pertenecen a escalas distintas y limitan la expectativa. [VID-PS: PriceSwing_06 @ 00:04:28–00:07:33]
- **SWE:** shelf consumido en top + middle/bottom seguido de extension ineficiente. La fuente da anatomía y target de atravesar el washed shelf, no contrato completo. [VID-PS: PriceSwing_04 @ 00:04:53–00:05:45] [VID-PS: PriceSwing_08 @ 00:15:12–00:17:28]
- **Consolidation apex / apex base:** pausa terminal, release/parabolic final, breakdown y posible retest de la accumulation/base que produjo el break. [VID-PS: PriceSwing_05 @ 00:00:48–00:05:09]
- **Pickup, feeding fractal, absorption, residual liquidity, midflow y CBP:** describen qué nivel fue recogido, cuál alimenta el movimiento, dónde se absorbe respuesta, qué pocket queda dentro del run, qué bases sostienen el flow y qué borde rompe limpiamente. M2020 conserva la lógica, pero refina alcance y jerarquía.

## 3. CPS: secuencia, función y límite

Price Swing confirma CPS como `Characteristics of a Price Swing`: un mapa relacional de features para localizar el precio y conectar anatomía con liquidity principles. Los principios explican **por qué**; CPS describe **cómo** se organiza y permite navegar. [VID-PS: PriceSwing_01 @ 00:00:14–00:06:03] [VID-PS: PriceSwing_10 @ 00:06:35–00:07:39]

PS09 recompone el ciclo completo y después ofrece fade, apex retest y breakout como comportamientos alternativos. PS10 vuelve a exigir escoger un feature, repetirlo y desarrollar **su** trade model. Por tanto, el corpus no contiene un setup operativo único llamado CPS, aunque [USUARIO] recuerda que existía uno. [VID-PS: PriceSwing_09 @ 00:10:33–00:12:48] [VID-PS: PriceSwing_10 @ 00:19:53–00:21:40]

## 4. Setups legacy y precursores

- **Swing retest of CLB:** retorno al core/PoR con llegada fina; contrato legacy incompleto. `SOLO PRICE SWING — NO CONFIRMADO DESPUÉS` como setup autónomo.
- **Counterflow / SWE fade:** extension ineficiente hacia opposing HTF liquidity, first touch y recorrido hacia inventory/core. `PRECURSOR REFINADO EN M2020` dentro de S-02/S-08.
- **Consolidation-apex fade:** last/second-last release, high/low que debe sostener y weaker rallies antes del breakdown. `PRECURSOR REFINADO EN M2020`; no es trigger canónico.
- **Apex-base retest / shelf-flip retest:** buen nivel previo + weak arrival + break + retorno a BA/apex base. La escala del break limita el target. `PRECURSOR REFINADO EN M2020`.
- **Pain trade:** buildup que absorbe el extremo y amenaza otra pocket; diagnóstico de deterioro, no setup.
- **SWE:** añade confluencia y expectativa de atravesar el washed area; faltan hard stop, threshold y reglas cerradas de reentrada.

No se creó setup nuevo: ninguna novedad Price Swing supera la capa M2020 con un contrato más completo. Tampoco se creó TE; los trades incompletos, stop-out de PS08 y ejercicios de PS10 no unen inequívocamente contexto, fill, invalidación, gestión y desenlace.

## 5. Qué sobrevivió en M2020

- Core frente a residual y `response ≠ hold ≠ reversal`.
- Price swing como estados encadenados, no patrón estático.
- Midflow sostenido por bases/inventory y debilitado cuando dejan de sostener.
- First touch como máxima asimetría local; retest como distribución distinta.
- Importancia del delivery hacia el nivel, escala gobernante y espacio disponible.
- Tracking post-entry de absorption, stair-step, winner/loser development y probabilities shifting.
- Framework → historical sample → live observation → modelo validado por comportamiento.

Estatus: `CONFIRMADO/CONSERVADO EN M2020`.

## 6. Qué fue refinado

- Shelf/inventory pasó de equivalencia visual amplia a equivalencia funcional acotada por el base que creó el extremo.
- La SWE temprana se descompone en M2020 como drain por repeated/deep tests, residual weakness, parabolic/exhaustion y gestión dinámica; M2020 ya no necesita la etiqueta.
- Apex temprano mezclaba fade, break y retest; M2020 separa exhaustion, technical break, shelf flip, BA y retest.
- Entry/stop legacy se convierte en tres capas: invalidación estructural, deterioro probabilístico y stop de emergencia.
- `Manageable response` deja de implicar winner: solo crea cushion para observar nueva información.
- Las reglas de top/middle/bottom, PoR o CBP quedan subordinadas a nivel, llegada, timeframe y sample.

Estatus: `PRECURSOR REFINADO EN M2020`.

## 7. Qué fue corregido

La corrección explícita central es `transfer of liquidity`. PS03 documenta el lenguaje temprano —`transferred down`, `transfer of liquidity`—; M2020 S10 lo llama misnomer: `Liquidity doesn't get transferred. Liquidity follows.` El comportamiento visual permanece, pero la explicación vigente usa order splitting, execution algos, inventory que follows/chases price, withdrawal/repricing, exhaustion y drain. [VID-PS: PriceSwing_03 @ 00:07:42–00:09:49] [VID-M2020: Session 10 @ 00:06:17–00:07:24]

También se corrigen por alcance los absolutos legacy sobre fills, extensions y respeto del framework: son hipótesis contextuales, no leyes ni tasas calibradas.

Estatus: `VOCABULARIO TEMPRANO CORREGIDO`.

## 8. Qué desapareció o no fue reutilizado

- SWE como nombre formal y CBP como pieza central pierden protagonismo en M2020.
- `Last/second-last release` no sobrevive como trigger canónico.
- El ladder CPS de 13 componentes sigue siendo mapa, pero M2020 enseña estados y decisiones con mayor granularidad.
- Shelf flip, apex base y pickup sí sobreviven; no deben clasificarse como abandonados.
- El template cerrado de cuatro apexes, CPS-setup, momentum trade y parámetros Washed IV/CPL no aparecen en Price Swing: no son “abandonados” demostrados, sino `POSIBLE MATERIAL PERDIDO`.

## 9. Mapa PTC/Chris Lori → Price Swing → M2020

| Capa | Evidencia | Estado |
|---|---|---|
| PTC/Chris Lori | Esquema CPS con marca Pro Traders Club/ChrisLori; fractals, pickup, absorption y dealing; EM atribuye `shifting points` a Lori | Herencia directa acreditada |
| Price Swing | EM organiza esa anatomía en shelves, SWE, apex, midflow, core/residual y ejercicios de respuesta | Desarrollo temprano; autoría término-a-término no demostrada |
| M2020 | Microestructura, VVF, estados, exhaustion, escala, first-touch/retest y Bayes post-entry | Capa refinada y canónica |
| Literatura/mercado | Papers de microestructura y observación propia citados por EM | Tercera pata; no reducir el método a PTC |

La doctrina void→base y cifras tipo 80% aparecen atribuidas a Lori por un alumno; no se convierten en estadística propia de EM sin fuente primaria.

## 10. Preguntas cerradas o avanzadas

- **SWE:** anatomía shelf-specific y target cerrados cualitativamente; contrato aún incompleto.
- **Washed/drained:** top/middle/bottom consumidos y repeated/deep tests conectados genealógicamente, sin equivalencia universal ni threshold.
- **CPS:** confirmado definitivamente como framework en el corpus; setup recordado no localizado.
- **Tradeable PI:** proceso nivel + llegada + estado + escala + resultado fuertemente reconstruido; no existe clasificador universal.
- **Apex management:** escala, absorption, reentry y pain-trade avanzan; template de cuatro casos no aparece.
- **Second-level information:** mecánica de adquisición parcialmente reconstruida por PS10, no la lección prometida.
- **C-001:** genealogía temprana completa y corrección M2020 preservada.

## 11. Material buscado y no localizado

- Setup CPS concreto.
- Template formal de cuatro variaciones de apex y gestión por variante.
- Poke past low del OP y su efecto formal sobre probabilidades.
- `Fractal pushing`.
- HOTW y reglas YO/WO/MO.
- Taxonomía responsive vs market-state-dependent.
- Momentum trade como setup.
- Parámetros completos de Washed IV/CPL.
- Threshold/timing universal de extension/fill.

Estas ausencias corresponden al corpus conservado completo, no solo a Price Swing.

## 12. Dependencias probablemente perdidas

- `Process video` y `exercise video`, no conservados según [USUARIO].
- Lección de `second-level information` y archivo/plantilla de cuatro apexes.
- Continuación prometida sobre OP.
- Modelos privados o posteriores: Washed IV/CPL, momentum trade y posible CPS setup.
- Material que formalizara YO/WO/MO, responsive/state-dependent o fractal pushing, si existió.

PS10 reconstruye indirectamente el itinerario de exercising, pero no acredita ser ninguno de los archivos perdidos.

## 13. Claims que pasan a validación empírica

- Tasa/tamaño de response desde first touch y degradación del retest.
- Efecto de deep tests sobre un shelf y threshold de washed/drained.
- Fill de voids/extensions: frecuencia, distancia, timing y distinción entre fill, core return y reversal.
- Technical break + parabolic como filtro incremental del fade.
- Llegada eficiente/ineficiente a core por estado, timeframe e instrumento.
- Winner/loser characteristics y corte antes del hard stop.
- Retórica cuantitativa (`80/20`, `99 to 1`, `always`, `guaranteed`).
- Traslado a BTC perps/Hyperliquid, que no queda validado por este corpus FX histórico.

El corpus fuente conservado queda procesado por completo. El siguiente trabajo ya no es destilación: requiere aclaración de Jordi, recuperación externa opcional o validación empírica.
