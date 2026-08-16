# Extracto — PriceSwing_08

## 1. Ficha de fuente

- **Fuente:** `00_fuentes/videos/PriceSwing_08.mp4`.
- **Duración:** 00:31:15.
- **Apoyo:** transcripción/SRT/JSON completos y 22/22 frames indexados inspeccionados; el vídeo se contrastó en los pasajes con shelf, SWE, stop-out y referencias deícticas.
- **Jerarquía:** `M2020 > Price Swing > PDFs`.
- **Naturaleza:** lección legacy sobre shelf top/bottom, shelf wash extension, first-touch y retest posterior. Incluye una mención a un short real detenido, pero no un trade documentable de principio a fin.

## 2. Estructura real

1. Shelf como inventory, apex retest y posible stop-out (00:00:00–00:06:50).
2. Shelf top/bottom, distancia al apex y selección de respuestas (00:06:51–00:15:11).
3. SWE, first touch y retest tras consumo/invalidation (00:15:12–00:20:34).
4. Shelf lejano, pain trade y contexto superior (00:20:49–00:25:09).
5. Counterflow, gestión por respuesta y structured exercising (00:25:10–00:31:12).

## 3. Shelf top/bottom retests

- El shelf es el inventory que sostiene el run; puede estar próximo al apex o mucho más lejos. La parte unfilled —top, middle o bottom— importa más que el rectángulo indiscriminado. [VID-PS: PriceSwing_08 @ 00:00:15–00:00:50] [VID-PS: PriceSwing_08 @ 00:08:04–00:09:18] `CONFIRMADO/CONSERVADO EN M2020`.
- **Respuesta counterflow en shelf:** EM busca una extensión ineficiente hacia la parte unfilled del shelf. Si el shelf es HTF debe evaluarse si existe espacio/respuesta suficiente en esa escala. Si price se sienta sobre el nivel y sellers siguen presionando, no hay una respuesta favorable aunque el shelf sea grande. [VID-PS: PriceSwing_08 @ 00:08:04–00:09:18] [VID-PS: PriceSwing_08 @ 00:20:49–00:21:28]
- **Retest tras shift:** un apex-base/shelf retest gana calidad cuando previamente se recoge un nivel H1/H4/daily, la llegada es muy débil/extended y el shelf queda completamente consumido o, mejor, invalidado. El retorno se busca en la parte todavía unfilled del apex base/liquidity base, que puede coincidir con point of release. [VID-PS: PriceSwing_08 @ 00:16:29–00:18:27] [VID-PS: PriceSwing_08 @ 00:18:41–00:20:25]
- Un shelf cercano facilita conectar invalidation y apex-base retest. Con shelf lejano, la respuesta counterflow desde top/bottom puede existir, pero la entrega debe debilitarse; buildup/clustering sobre el shelf señala fuerza contra el trade. [VID-PS: PriceSwing_08 @ 00:19:15–00:20:34] [VID-PS: PriceSwing_08 @ 00:28:41–00:29:45]
- El flip del shelf cambia el estado: las respuestas residuales posteriores pueden seguir siendo tradeables localmente, pero no restablecen el inventory consumido. [VID-PS: PriceSwing_08 @ 00:03:13–00:04:27] [VID-PS: PriceSwing_08 @ 00:06:51–00:08:02] `PRECURSOR REFINADO EN M2020`.

## 4. First touch y retest son operaciones distintas

### 4.1 First-touch fade

- **QUÉ:** fade de una extensión muy débil/thin hacia un nivel H1/H4 suficientemente grueso, después de que el sell/buy inventory del shelf haya sido consumido. Un SWE añade confluencia, pero no sustituye nivel y llegada. [VID-PS: PriceSwing_08 @ 00:15:12–00:17:28]
- **CUÁNDO/ENTRADA:** first touch del nivel HTF después de una extensión progresivamente más fina. Precio exacto/orden: `NO ESPECIFICADO EN FUENTES`.
- **INVALIDACIÓN:** el extremo de la hipótesis debe sostener en la capa legacy general; hard stop/distancia específica en este ejemplo: `NO ESPECIFICADO EN FUENTES`.
- **TARGET:** `run it past that shelf wash extension` — atravesar el shelf ya drenado. [VID-PS: PriceSwing_08 @ 00:15:43–00:16:20]
- **GESTIÓN:** retirar parte de la equity durante la respuesta; EM permite volver a tomar el trade si reaparece la oportunidad. Cantidad, BE y reglas de reentrada: `NO ESPECIFICADO EN FUENTES`. [VID-PS: PriceSwing_08 @ 00:16:12–00:16:29]

### 4.2 Retest posterior de apex base/shelf

- **QUÉ:** tras la respuesta inicial y el consumo/invalidation del shelf, retorno a apex base, liquidity-base top/middle/bottom o PoR aún unfilled. [VID-PS: PriceSwing_08 @ 00:16:29–00:18:27]
- **CUÁNDO/ENTRADA:** nivel HTF recogido + arrival débil + shelf totalmente consumido o poked/invalidated; entrada en la parte unfilled del retest. Borde y orden exactos: `NO ESPECIFICADO EN FUENTES`.
- **INVALIDACIÓN:** el high/low concreto puede invalidar esa entrada, pero no necesariamente la tesis de que el inventory superior se está drenando. Hard stop/tolerancia universal: `NO ESPECIFICADO EN FUENTES`.
- **GESTIÓN/TARGET:** expectativa de continuar a través del lado débil; parciales y target exacto: `NO ESPECIFICADO EN FUENTES`.

No se mezclan: el first touch opera el nivel de llegada; el retest opera el inventory/accumulation después del shift.

## 5. Shelf Wash Extension

- Definición corroborada: antes de alcanzar el nivel, bottom, middle y top del shelf han sido picked; la extensión posterior deja el área `drained in sell-side liquidity`. Si no quedan sellers/buyers, el precio debería atravesarla con menos fricción. [VID-PS: PriceSwing_08 @ 00:15:12–00:15:59] `PRECURSOR REFINADO EN M2020` por drain cualitativo.
- PS08 añade uso operativo: en el first-touch fade, el target se coloca más allá del SWE; se puede retirar equity durante el recorrido. [VID-PS: PriceSwing_08 @ 00:15:53–00:16:24]
- EM dice que el operador desarrollará sus propios `parameters for a shelf wash extension`; expresa preferencia por una extensión `right past the shelf`, especialmente si existe un fractal, pero no fija distancia mínima, trigger formal, hard stop ni estadística. [VID-PS: PriceSwing_08 @ 00:16:04–00:16:20]
- El retest posterior no se activa por el nombre SWE solo: exige good/thick HTF level, arrival muy débil y shelf consumido o invalidado. [VID-PS: PriceSwing_08 @ 00:16:45–00:18:08]
- Por tanto, PS08 **avanza fuertemente pero no completa** el contrato SWE. Cierra target estructural y una pauta de gestión; trigger exacto, hard stop y parámetros de reentrada siguen `NO ESPECIFICADO EN FUENTES`.

## 6. Stop-out real y pain trade

- EM afirma sobre un short en apex retest: `I took a short there actually that day ... I did get stopped out`, al extender price por encima del high. Añade que la idea amplia permanecía válida porque la extensión seguía drenando buy-side liquidity y después el mercado cayó durante trece días. [VID-PS: PriceSwing_08 @ 00:06:16–00:06:41]
- Lo único inequívoco es: short real, stop por invalidación del high y continuación bajista posterior. No se muestran entrada exacta, stop ejecutado, gestión, reentrada ni resolución atribuible a una misma orden. **No se crea TE**.
- Distinción: el high invalida esa entrada; no prueba por sí solo que el shelf/inventory amplio se haya fortalecido. El `pain trade` forma parte del pre-trade planning: anticipar qué hará EM si price toma el stop, llega a un nivel mejor y luego desarrolla la hipótesis original. [VID-PS: PriceSwing_08 @ 00:21:33–00:22:40] `PRECURSOR REFINADO EN M2020` por invalidación estructural vs deterioro probabilístico.

## 7. Gestión y proceso

- Counterflow contra el estado gobernante: tomar equity rápido. Si price no sale del nivel y `clustering and clustering`, EM cerraría el trade; la anatomía de la respuesta distingue winner/loser. [VID-PS: PriceSwing_08 @ 00:28:41–00:29:45]
- El ejercicio debe definir feature, setup, dirección con/contra flow y timeframe; también estudiar trades negativos para internalizar qué no arriesgar. EM desaconseja usar dinero real durante esa fase porque el objetivo pasa de aprender a ganar y daña el feedback psicológico. [VID-PS: PriceSwing_08 @ 00:25:10–00:26:24] [VID-PS: PriceSwing_08 @ 00:29:50–00:30:54] `CONFIRMADO/CONSERVADO EN M2020`.
- Claims como `more times than it doesn't` o el response de 30 pips son pedagógicos/anecdóticos, no medición de expectancy. [VID-PS: PriceSwing_08 @ 00:26:33–00:28:02]

## 8. Comparación y evolución

- M2020 conserva nivel + arrival + state + first touch, formaliza probabilities shifting y distingue mejor technical break/parabolic/exhaustion. La capa M2020 gobierna S-08.
- La morfología shelf picked/consumed se conserva como drained inventory, pero M2020 no reutiliza `SWE` como nombre formal. `PRECURSOR REFINADO EN M2020`.
- PS08 es más tajante al sugerir que un área drenada se atravesará; M2020 S14 añade la excepción contextual de que una zona washed puede responder según cómo llega price. No es contradicción directa: la versión posterior limita el alcance y es canónica.

## 9. Resultado de la caza

| Ítem | Resultado PS08 |
|---|---|
| CPS como setup | Ausente. |
| SWE completo | Target y gestión parcial añadidos; hard stop y parámetros exactos ausentes. |
| 4 apexes / gestión por variante | Variaciones contextuales, no catálogo de cuatro. |
| Poke past low del OP | Pokes de shelf/high; OP no identificado. |
| Fractal pushing | Ausente. |
| HOTW | Ausente. |
| YO/WO/MO | Ausente. |
| Responsive vs market-state-dependent | `response/responsive` solo en sentido común; taxonomía ausente. |
| Momentum trade | Ausente como setup. |
| Washed IV/CPL | Ausente; SWE no se equipara. |
| Tradeable vs non-tradeable PI | Nivel grueso + weak arrival + parte unfilled + desarrollo de respuesta; fuerte avance, no clasificador universal. |
| Extensión suficiente/timing | `thin/extended`, right past shelf y espacio según timeframe; sin umbral/timing universal. |
| PTC/Lori vs EM | La slide CPS reaparece sin atribución verbal; el vídeo no separa autorías. |
| Transfer of liquidity | Ausente. |

## 10. Erratas verificadas y límites

- Whisper `shell` = **shelf**; `state of equity` = **state of liquidity**; `infantry` = **inventory**; `unflow` = **unfilled**.
- El frame inicial vuelve a mostrar la slide `Characteristics of a Price Swing`; no acredita por sí solo la autoría verbal de los añadidos dibujados por EM.
- Los numerosos `trade there` son ejemplos de selección histórica. Sin entry/stop/gestión/resultado unidos no se convierten en TE.
