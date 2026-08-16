# Auditoría del corpus — previa al congelado "EMTrades reconstruido v1"

> Sesión 17 (2026-08-16). Tanda 1: taxonomía epistémica, índice y trade examples.

## Bloque 1 — Normalización de taxonomía epistémica

Sistema declarado en CLAUDE.md, sección "Estados epistémicos" (cinco etiquetas). Conversión aplicada sobre `40_destilado/*.md`, estrictamente etiqueta→etiqueta:

| Etiqueta ad-hoc (eliminada) | Etiqueta declarada (nueva) | Ocurrencias |
|---|---|---|
| `` `PRECURSOR REFINADO EN M2020` `` | `[PRECURSOR: PS → refinado en M2020]` | 15 |
| `` `VOCABULARIO TEMPRANO CORREGIDO` `` | `[PRECURSOR: PS → refinado en M2020]` | 2 |
| `` `SOLO PRICE SWING — NO CONFIRMADO DESPUÉS` `` | `[SOLO-PS: no confirmado después]` | 5 |
| `` `CONFIRMADO/CONSERVADO EN M2020` `` | `[CONFIRMADO]` | 15 |
| `` `[INFERENCIA FUERTE]` `` (backticks) | `[INFERENCIA-FUERTE]` | 1 |

Nota sobre las dos conversiones no literales:
- `VOCABULARIO TEMPRANO CORREGIDO` → PRECURSOR: ambos casos (01_principios.md:98, 91_contradicciones.md:12) marcan el misnomer "transfer of liquidity" corregido en M2020 S10 — es exactamente "formulación temprana superada"; el detalle de que fue una corrección de vocabulario permanece en el texto del propio bullet.
- `CONFIRMADO/CONSERVADO EN M2020` → `[CONFIRMADO]`: marcaba afirmaciones de época Price Swing que M2020 conserva; el matiz cross-época queda en las fuentes citadas en cada bullet.

Sistemas paralelos NO tocados (deliberadamente, son otra cosa):
- `NO ESPECIFICADO EN FUENTES` — marcador de campo vacío en setups (CLAUDE.md regla 4).
- RESUELTA / PARCIALMENTE RESUELTA / DESARROLLADA / RESUELTA OPERATIVAMENTE / CERRADA-IRRECUPERABLE — ciclo de vida de preguntas en `90_preguntas_abiertas.md`.
- "Estado: confirmado / por confirmar" en entradas de glosario — CLAUDE.md regla 5.

## Tanda 2 (Sesión 18) — cierre de la taxonomía

- **Corrección de recuento:** la tabla de la tanda 1 decía 15 conversiones de `CONFIRMADO/CONSERVADO EN M2020`; el diff real de cbdd3bf contiene **18** (02_conceptos ×9, 04_proceso ×7, 03_setups ×2).
- **Regresión revertida:** los 18 casos reetiquetados `[CONFIRMADO]` → `[CONFIRMADO: PS→M2020]` (supervivencia cross-época, eje para filtrar en validación). Estado declarado en CLAUDE.md.
- **Caso 1 (04_proceso.md:39)** — RESUELTO: `**AVANCE, NO CIERRE**` convertido a prosa sin negrita ("es un avance, no un cierre").
- **Caso 2 (90_preguntas_abiertas.md:30)** — RESUELTO en el bloque 2 de la sesión 18 con el sistema de estados de pregunta ([IRRECUPERABLE] para el artefacto + nota de lo reconstruido).
- **Caso 3 (02_conceptos.md:31)** — RESUELTO: nuevo estado `[NO-LOCALIZADO]` declarado en CLAUDE.md y aplicado. Taxonomía de afirmaciones cerrada en 7 estados.

## Tanda 2 — estados de pregunta (bloque 2)

Normalización de `90_preguntas_abiertas.md` a los seis estados declarados en CLAUDE.md. Reparto resultante (con estados duales contados en ambos): [RESUELTA] ×6 · [RESUELTA-PARCIAL] ×10 · [NO-LOCALIZADA] ×10 · [IRRECUPERABLE] ×2 · [VALIDACIÓN] ×6 · [PENDIENTE-USUARIO] ×4.

Juicio añadido (único caso sin marcador previo): **"Mapeo lección↔vídeo"** (antigua abierta 10) no llevaba estado; se le asignó [NO-LOCALIZADA] [PENDIENTE-USUARIO] — los vídeos referenciados no están en el corpus y Jordi podría recordar la correspondencia. Revisar si se prefiere otro estado.

## Tanda 2 — muestreo de integración extracto → maestro (bloque 3)

Muestreo dirigido a los tres puntos de menor ratio citas/líneas: PS01 (7/76L), PS09 (6/70L), S15 (10/60L). Clasificación: (a) omitido por jerarquía · (b) omitido por redundancia · (c) pérdida real.

**PS01 — LIMPIO.** Integrados: CPS framework/feature (02:28, 04:61), core vs residual (02:364), precursor legacy S-08 (03:79). Omitidos: "trading on the principles" y fractalidad (b — principios cubiertos por PDFs/M2020); "extensions get filled" PS01 (b — claim ya registrado con S2 + genealogía PS02, estatus PRECURSOR); "never definitive" del CLB retest (b — equivale al "response ≠ hold ≠ reversal" M2020); uso temprano de "washed up" (b — criterio top+bottom picked ya en SWE/washed vía PS04). La baja ratio se explica por jerarquía, no por prisa.

**PS09 — LIMPIO.** Integrados: síntesis/mapa relacional (02:29, 02:159, 04:125, 91:33). Omitidos: definición legacy de shelf "last core area of inventory that needs to hold" (b — coincide con la definición M2020 "the last inventory that pushed price to new lows" ya en 02:shelf); "last inventory dinámico" (cubierto funcionalmente por 02:159); metáfora battle/tug-of-war (a — pedagogía superada por M2020); apexes "highly responsive" como adjetivo común (b — negativo de caza ya registrado en cierre_price_swing). **Atención PS04/PS08:** el material wash/shift de PS09 no revela huecos en la morfología SWE integrada — sin anotaciones.

**S15 — 3 PÉRDIDAS REALES (c), integradas:**
1. Mecanismo completo de "HTF pulls more liquidity" (vela diaria = 24–48h de volumen; granularidad LTF como artefacto de cotización a 5 decimales) → añadido a 01_principios § Jerarquía de timeframes. [VID-M2020: Session 15 @ 00:07:01–00:10:57]
2. Detección del viraje de régimen HTF + gestión de fades fallidos ("runs, doesn't fill — first sign"; "extension beneath Asia range = HTF inefficiency characteristic"; "my high becomes the invalidation") → añadido como regla 14b en 03_setups. [VID-M2020: Session 15 @ 01:00:00–01:06:07]
3. Autodefinición del edge ("probabilistic anticipatory approach trading the properties of price behaviors which are a result of market mechanisms"; modelos lagging; edge death sin aviso de los ladder traders) → añadido a 04_proceso. [VID-M2020: Session 15 @ 00:27:41–00:32:23]
Redundantes correctos en S15 (b): repaso microestructura (S2/S12), "trading the volatility" (S12 + regla 11), countermeasures, workspace, niveles-sensor, FX conduit — todos ya integrados.

**Veredicto del criterio de ampliación:** resultado MIXTO — los dos Price Swing salen limpios (la baja integración ES jerarquía), pero S15 tenía 3 pérdidas puntuales, ya reparadas. Ni "los tres limpios" ni "los tres sucios": no se amplía el muestreo por cuenta propia; queda a decisión humana si se muestrea algún otro M2020 denso (candidatos por densidad: S13, S11.2).

## Tanda 3 (Sesión 19) — correcciones de fuente (capturas CLP en alta resolución)

- **Error factual corregido:** [IMG: CLP/EEBe34cXoAEhKWw.png] es XAUUSD **t30 = 30 TICKS**, no "30s" (visible en el selector de TF: barra T5/T25/T30/T40, T30 activo). Corregido en extracto_capturas_CLP.md, 02_conceptos y 03_setups. Cambia el significado: es el extremo LTF de la serie.
- **Sospecha derivada — RESUELTA (sesión 20):** [IMG: CLP/EEBgtXpXUAAoEmR.png] reverificado en alta resolución: es **t5 = gráfico de 5 TICKS** (selector "t5" en cabecera, T5 activo en la barra lateral), no 5 segundos. Corregido en extracto_capturas_CLP.md (sección y línea de serie "t30→t5") y en 02_conceptos § CPL.
- **IV = inventory elevado a [CONFIRMADO]** con la anotación "Bids dry off, red inventory pushes price back down through the rip area" [IMG: CLP/ED6JtkLXsAEu4X4.png]. Expansión literal de las letras: sigue sin escribir.
- **ANOMALÍA INTERNA DE LA FUENTE (registrada, no resuelta):** EM rotula "CPL - consumption response leg", pero esas palabras darían CRL, no CPL. Hipótesis posibles (palabra omitida; "Consumption Price Leg" glosado de memoria) — NO se infiere cuál. Anotada también en 02_conceptos.
- **Dato de R verificado** en EEBe34cXoAEhKWw.png: SL rotulado "Pips: -58" (1515.46 vs entrada ~1514.88), beneficio abierto rotulado "Pips: 222.0" → **≈3.8R corriendo**, números legibles con claridad. Se mantiene la salvedad: la captura no acredita autoría ni cierre.

## Tanda 3 — preguntas en la misma situación que q18 (propuesta, NO aplicada)

q18 se reclasificó a [VALIDACIÓN] [NO-LOCALIZADA] porque la morfología está completa y los parámetros fueron retenidos deliberadamente por la fuente. Dos preguntas más comparten el patrón "morfología completa + parámetros remitidos por EM a samples/engagement, nunca publicados" y son candidatas a añadir [VALIDACIÓN] como segundo estado — **se listan para decisión humana, sin aplicar**:

1. **Resueltas #2 (SWE)** — [RESUELTA-PARCIAL]: PS04/PS08 dan morfología y target, pero "EM remite los parámetros a samples y no fija hard stop, distancia, breakdown trigger ni reglas de reentrada". Mismo patrón: no se encontrarán leyendo; se construyen en fase 2.
2. **Abiertas #15 (criterios de "washed")** — [RESUELTA-PARCIAL]: cualitativo resuelto, threshold cuantitativo inexistente en fuente (PS08: "sus parámetros deben desarrollarse mediante engagement"). Mismo patrón.

## Tanda 3 — cierre del muestreo de integración (bloque 5)

**Última pasada: S13 y S11.2** (los dos candidatos por densidad anotados en la tanda 2).

- **S13** — integración excelente pese a ser la sesión más densa (midflow, jerarquía TF, 3 lados, entornos, TE-02, cadencias: todo con reflejo). **1 pérdida (c)**: el cluster de lectura del primer break ("it looks like an apex anyway" / el primer break típicamente golpea residual / el tipo de nivel que creó el extremo pondera si aguanta) → integrado en 02_conceptos § Apex. [VID-M2020: Session 13 @ 01:26:45–01:29:49]
- **S11.2** — **2 pérdidas (c)**, ambas de gestión/comportamiento, confirmando el patrón de S15 (las pérdidas se concentran en gestión, no en principios/conceptos): (1) **shelf retest de continuación** (comportamiento de continuación contextual, distinto del fade de exhaustion) → 03_setups § Comportamientos de referencia [@ 01:25:58–01:27:55]; (2) **riesgo del cushion ausente** (sin initial response no hay countermeasures → full loss/gap-through posible; 2–5 pips es ejemplo, no mínimo) → S-08 CÓMO gestiona [@ 01:47:21–01:51:19]. Redundantes correctos: reach vs buildup/swipes, drain criteria, Bayes post-entry, small shelf, timeframe-microscopio, modelo de 5 pasos (todo ya en S-08/04_proceso con cites de S11.2).

**MUESTREO DE INTEGRACIÓN: CERRADO.** Balance final: **5 extractos muestreados** (PS01, PS09, S15, S13, S11.2) de 26 vídeos; **6 pérdidas (c) integradas en total** (3 en S15, 1 en S13, 2 en S11.2), cero en los extractos Price Swing. Patrón confirmado: la integración de principios/conceptos es sólida; las pérdidas se concentraron en material de GESTIÓN y selección fina de sesiones M2020 densas — todas reparadas. La integración del corpus se da por buena para el congelado v1.

**Recuento final de estados de pregunta (tras sesión 19):** [RESUELTA] ×7 · [RESUELTA-PARCIAL] ×12 · [NO-LOCALIZADA] ×7 · [VALIDACIÓN] ×7 · [IRRECUPERABLE] ×2 · [PENDIENTE-USUARIO] ×0 (duales contados en ambos; la leyenda del encabezado del fichero no cuenta). Cambios de la sesión: q1 → RESUELTA (CPS≠CPL); q14 y q17 → RESUELTA-PARCIAL; q18 → VALIDACIÓN+NO-LOCALIZADA; q10 pierde PENDIENTE-USUARIO (prioridad baja); q9 cerrada como NO-LOCALIZADA definitiva.

## Casos sin clasificar — requieren decisión humana

Marcadores que no encajan limpiamente en las cinco etiquetas. NO convertidos; texto actual intacto:

1. **04_proceso.md:39** — `**AVANCE, NO CIERRE**`
   Texto: "S9 no entrega una lista operativa cerrada de winner/loser ni umbral universal para cortar antes del stop: **AVANCE, NO CIERRE**."
   Problema: es un veredicto sobre el grado de cierre de una pregunta (q-tracking), no un estado epistémico de una afirmación de EM. Candidatos: dejarlo como prosa sin negrita, o moverlo como nota a 90_preguntas_abiertas.

2. **90_preguntas_abiertas.md:30** — `**ARTEFACTO NO LOCALIZADO; MECÁNICA PARCIALMENTE RECONSTRUIDA**`
   Texto: "5. **\"Second level information\" como lección — ARTEFACTO NO LOCALIZADO; MECÁNICA PARCIALMENTE RECONSTRUIDA:** ..."
   Problema: mezcla estado de un artefacto perdido (fuente) con estado de reconstrucción (contenido). No es ninguno de los cinco estados; funcionalmente es un estado de ciclo de vida de pregunta ad-hoc. Candidato: normalizar el vocabulario de estados de PREGUNTA (sistema paralelo) en una tanda posterior.

3. **02_conceptos.md:31** — `**NO SE HA LOCALIZADO EN EL CORPUS CONSERVADO**`
   Texto: "[USUARIO] recuerda además un setup concreto llamado CPS, pero **NO SE HA LOCALIZADO EN EL CORPUS CONSERVADO** (M2020 16/16 + Price Swing 10/10 + PDFs + capturas)."
   Problema: estado de búsqueda exhaustiva negativa — ni [SOLO-PS] (no es material temprano) ni [INFERENCIA] (no es deducción). Es información valiosa tal cual; candidato: admitir un sexto estado `[NO-LOCALIZADO]` o dejarlo como prosa.
