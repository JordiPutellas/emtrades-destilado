# EMTrades reconstruido — v1 (SNAPSHOT CONGELADO)

**Fecha de congelado:** 2026-08-16.
**Commit de referencia del estado congelado:** `fe35256` (fin de la auditoría, tandas 1-3 + higiene; el commit que introduce esta carpeta es el inmediatamente posterior).

## Corpus que sustenta este snapshot (cerrado, procesado al 100%)

- **17/17 PDFs** (módulos: Liquidity Principles, Price Swings, Price Delivery, Fractals, Process, Trade Example...).
- **26/26 vídeos** transcritos y destilados (27,4 h; 693 frames): Mentoría 2020 completa (16/16, ~23 h 48 min) + serie Price Swing completa (10/10).
- **237/237 capturas** procesadas (incluye Discord 129/129, CLP 12/12, EM Twits, MIET, sueltas).
- Cierres transversales: `30_extractos/cierre_m2020.md`, `30_extractos/cierre_price_swing.md`. Auditoría: `30_extractos/auditoria_corpus_v1.md`.

## Qué ES v1

Un snapshot versionado y auditable de **lo que el corpus EMTrades documenta**: doctrina reconstruida con trazabilidad total (etiquetas de fuente + estados epistémicos de CLAUDE.md), ontología de niveles, máquina de estados del price swing, inventario de comportamientos/modelos con sus huecos marcados, y claims falsables extraídos con cita.

## Qué NO es

- **NO es una especificación de sistema de trading.** Los campos NO ESPECIFICADO EN FUENTES siguen vacíos; nada se ha completado por inferencia.
- **NO es evidencia de edge.** Nada del corpus ha sido validado estadísticamente (la base empírica de gestión son 5 TEs — especificación de comportamiento, no evidencia).
- **NO autoriza a operar nada**, ni en FX ni en BTC. La adaptación a BTC sigue aparcada (92_ideas_btc.md) y la validación es la fase 2, no iniciada.

## Regla de modificación

v1 es **inmutable salvo por error factual demostrable**. Toda corrección exige entrada de changelog aquí abajo (fecha, fichero, qué decía, qué dice, evidencia). Cualquier evolución doctrinal, reinterpretación o adición va a los maestros vivos de `40_destilado/` y, en su día, a v2 — nunca a esta carpeta.

### Changelog de v1

El registro canónico está en [`CHANGELOG_v1.md`](CHANGELOG_v1.md) (creado 2026-08-16, sesión de higiene; las cabeceras ❄️ de los ficheros apuntan a él). Sin correcciones factuales a fecha de hoy.

## Las tres capas, separadas por construcción

1. **Doctrina EM** — lo que las fuentes documentan, con etiqueta de fuente ([PDF:], [IMG:], [VID-M2020:], [VID-PS:], [DISCORD:], [IMG-TWIT:], [IMG-MIET:]) y estado epistémico ([CONFIRMADO], [CONFIRMADO: PS→M2020], [PRECURSOR: PS → refinado en M2020], [SOLO-PS: no confirmado después], [NO-LOCALIZADO]).
2. **Inferencias del proyecto** — [INFERENCIA] / [INFERENCIA-FUERTE]: deducciones nuestras, nunca presentadas como material original.
3. **Contexto [USUARIO]** — aportaciones de Jordi (93_contexto_usuario.md y marcas [USUARIO] puntuales): calibra plausibilidad y genera hipótesis; NUNCA es especificación del sistema ni rellena huecos de fuente.

## Contenido de la carpeta

| Fichero | Qué es |
|---|---|
| `00_README_v1.md` | Este documento. |
| `10_ontologia.md` | Ontología de niveles + máquina de estados + capa de microestructura. |
| `20_inventario.md` | Inventario A/B/C de comportamientos y modelos, con huecos motivados. |
| `30_claims_validables.md` | Claims falsables extraídos del corpus, con cita y qué medir. |
| `40_test_comprension.md` | Test ciego de comprensión (10 preguntas, sin respuestas). |
| `01_principios.md` … `93_contexto_usuario.md` | Copia congelada de los maestros a fecha de snapshot. |
