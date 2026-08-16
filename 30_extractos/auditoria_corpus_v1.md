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
