# Proyecto: Destilación del método EMTrades

## Objetivo

Convertir el material acumulado de EMTrades (vídeos, PDFs, capturas anotadas, conversaciones de Discord) en un sistema de trading documentado, trazable y falsable, como paso previo a validar si el edge existe y adaptarlo a BTC perps (Hyperliquid).

## Contexto

- EMTrades operaba GBPUSD spot FX. Método: price action puro basado en dinámica de liquidez (price moves to the less liquid side, volatility = f(liquidez), PIs/gaps y rebalances, fractalidad).
- El usuario fue rentable 2 años con este método (3k→60k) antes de dejar el trading por burnout. Hoy opera ocasionalmente BTC en Hyperliquid.
- La adaptación a BTC es HIPÓTESIS a validar, no un hecho. No mezclar destilación (qué decía EMTrades) con adaptación (qué haremos en BTC).

## Estructura del repo

- `00_fuentes/` — material bruto. NUNCA modificar.
- `10_transcripciones/` — salida de whisper por vídeo (.md con timestamps, .srt, .json).
- `20_frames/` — fotogramas extraídos en momentos visuales clave de los vídeos.
- `30_extractos/` — un .md por fuente procesada con lo relevante extraído.
- `40_destilado/` — documentos maestros. Son el PRODUCTO. Se actualizan incrementalmente.
- `scripts/` — herramientas de transcripción y extracción de frames.

## Reglas de destilación (OBLIGATORIAS)

1. **Trazabilidad total.** Toda afirmación en `40_destilado/` lleva etiqueta de fuente:
   - `[PDF: nombre]` — texto extraído de PDF
   - `[IMG: nombre]` — anotación leída en captura/gráfico
   - `[VID: nombre @ HH:MM:SS]` — dicho en vídeo (timestamp obligatorio)
   - `[DISCORD: lote/captura]` — de conversaciones de Discord
   - `[INFERENCIA]` — interpretación nuestra, pendiente de validar con el usuario
     Nunca presentar una inferencia como si fuera material original.

2. **Destilación incremental.** Al procesar cada fuente, en la MISMA sesión:
   - crear/actualizar su extracto en `30_extractos/`
   - integrar lo nuevo en los maestros de `40_destilado/`
   - actualizar `90_preguntas_abiertas.md` (resolver las que se resuelvan, añadir nuevas)
   - registrar conflictos en `91_contradicciones.md`

3. **Contradicciones son señal.** Si una fuente contradice algo ya destilado, NO sobreescribir: registrar ambas versiones en `91_contradicciones.md` con fuentes y fechas si se conocen. El método pudo evolucionar.

4. **Separar descripción de regla operativa.** En `03_setups.md` distinguir siempre:
   - QUÉ describe EMTrades (comportamiento del precio)
   - CUÁNDO entra (trigger concreto si lo hay)
   - DÓNDE invalida (si lo especifica)
   - CÓMO gestiona (parciales, BE, targets)
     Si algún campo no está en el material, escribir "NO ESPECIFICADO EN FUENTES" — no rellenar con suposiciones.

5. **Glosario vivo.** Todo término propio (PI, CPS, SWE, BA, shelf, apex, LLS, gap slip, midflow, fractal pushing...) va a `02_conceptos.md` con definición, fuente y estado (confirmado / por confirmar).

6. **Vocabulario del transcriptor.** Whisper falla con jerga. Al revisar transcripciones, corregir sistemáticamente: liquidity, inefficiency, GBPUSD/cable, bids/offers, fade, shelf, apex, fractal, rebalance, void, LLS, CPS, SWE, BA, midflow, pip. Mantener lista de erratas frecuentes en `10_transcripciones/_erratas.md`.

7. **Frames = contexto visual.** Los vídeos son screencasts de gráficos: lo que señala en pantalla vale tanto como lo que dice. El script de frames extrae fotogramas en pasajes con lenguaje deíctico ("look here", "this candle", "this level", "right there", "as you can see"). Al destilar un vídeo, revisar los frames de sus momentos clave, no solo el texto.

8. **No evaluar el edge durante la destilación.** Primero reconstruir fielmente el método completo. La crítica y validación estadística es una fase posterior y separada. Escepticismo sí, pero en `90_preguntas_abiertas.md`, no censurando el material.

## Flujo de trabajo por sesión

1. Elegir fuente(s) pendiente(s) — ver `30_extractos/_pendientes.md`
2. Procesar (leer/transcribir/ver frames)
3. Extraer → `30_extractos/`
4. Integrar → `40_destilado/`
5. Actualizar pendientes, preguntas abiertas y contradicciones
6. Commit con mensaje descriptivo: `destila: <fuente> — <qué añade>`

## Orden de procesamiento recomendado

1. PDFs restantes (base conceptual: Price Swing Basics → Price Delivery → Fractals → Process)
2. Vídeos (transcribir todos primero en batch, destilar después por orden temático)
3. Capturas de trades y Discord por lotes de 20-30 (contienen la ejecución real)
4. Trades propios del usuario (reconstrucción estadística — fase de validación)

## Qué NO hacer

- No dar consejo financiero ni recomendaciones de inversión; esto es documentación y análisis.
- No inventar reglas que el material no contiene para "completar" el sistema.
- No adaptar a BTC sobre la marcha; anotar ideas de adaptación en `92_ideas_btc.md` y seguir.

## Jerarquía de fuentes y fiabilidad

Las fuentes tienen épocas y fiabilidad distinta. Etiquetar época en vídeos:

- [VID-M2020: sesión @ ts] — Mentoría 2020. Fuente MÁS refinada y autoritativa.
- [VID-PS: vídeo @ ts] — Serie Price Swing (anterior). Útil para anatomía de
  swings, pero contiene conceptos que EM refinó o abandonó después.
  En conflicto entre épocas: prevalece M2020, y el conflicto se registra en
  91_contradicciones.md como "evolución del método".

## Estados epistémicos

Además de la etiqueta de fuente, las afirmaciones de `40_destilado/` llevan
(cuando aplica) una etiqueta de estado epistémico. Solo existen estas cinco,
siempre entre corchetes:

- `[CONFIRMADO]` — definido explícitamente por EM.
- `[PRECURSOR: PS → refinado en M2020]` — formulación temprana superada.
- `[SOLO-PS: no confirmado después]` — solo aparece en material temprano; no reutilizado.
- `[INFERENCIA]` / `[INFERENCIA-FUERTE]` — deducción del proyecto, con grado.
- `[USUARIO]` — aportación o corrección de Jordi (ver sección siguiente).

"NO ESPECIFICADO EN FUENTES" se mantiene tal cual como marcador de campo
vacío en setups (regla 4); no es un estado epistémico. Los marcadores de
ciclo de vida de `90_preguntas_abiertas.md` (RESUELTA, PARCIALMENTE
RESUELTA, CERRADA-IRRECUPERABLE...) son un sistema aparte y no se tocan.

## Etiqueta [USUARIO]

Correcciones o desacuerdos del usuario con el material original (p.ej.
"transfer of liquidity no es un mecanismo real") se registran con etiqueta
[USUARIO] junto a la afirmación original — NUNCA se borra ni se corrige
silenciosamente lo que decía EM. La destilación captura el método tal como
era; la crítica es una capa separada.
