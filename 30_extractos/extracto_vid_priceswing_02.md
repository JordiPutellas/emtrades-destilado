# Extracto — PriceSwing_02

## 1. Ficha de fuente

- **Fuente:** `00_fuentes/videos/Price Swing series/PriceSwing_02.mp4`
- **Duración:** 00:18:37.
- **Época/jerarquía:** Price Swing, anterior a M2020; `M2020 > Price Swing > PDFs`.
- **Revisión:** transcripción y SRT completas; 13/13 frames indexados; vídeo comprobado en el esquema y ejemplos GBPUSD H1/D1.

## 2. Estructura real del vídeo

1. Define core liquidity base y point of release dentro del diagrama CPS.
2. Explica contracción, buildup/consumo del lado de salida y skinny leg.
3. Propone top/middle/bottom, PoR y clean breaking point como candidatos de retest, no como entradas automáticas.
4. Desarrolla timeframe/refinamiento y enseña ejemplos GBPUSD.
5. Cierra con exercising: seleccionar parámetros propios y validar antes de convertirlos en reglas.

## 3. Vocabulario nuevo o temprano

### Core liquidity base

- Zona donde se han cruzado transacciones/volumen; normalmente es una `tight contraction`, un rango de precio relativamente estable con top definible, aunque no siempre limpio. [VID-PS: PriceSwing_02 @ 00:00:10–00:01:20]
- La fuente no sabe de antemano por qué lado romperá sin contexto adicional. **Aspecto chartista:** consolidación/rango del origen del run. **Función:** concentra la liquidity relativa que inicia el drive y puede responder cuando el precio regresa. [VID-PS: PriceSwing_02 @ 00:00:47–00:01:09] [VID-PS: PriceSwing_02 @ 00:02:57–00:04:15]
- **Estatus:** `CONFIRMADO/CONSERVADO EN M2020`, aunque M2020 reemplaza `volume point`/`psychological attachment` como causalidad suficiente por estado de liquidity y ejecución.

### Point of release, contracción y buildup

- Antes de release, la acción se aquieta: caen bodies/volumen, se seca liquidity y encoge volatilidad; después el precio construye presión cada vez más profunda contra las offers del borde y sale. [VID-PS: PriceSwing_02 @ 00:01:20–00:02:31]
- En data-driven release aparece típicamente skinny leg/shot; en condiciones normales puede volver a recoger core/PoR/top antes de continuar. [VID-PS: PriceSwing_02 @ 00:02:27–00:02:57]
- **Aspecto chartista:** último borde/miniacumulación desde el que parte la expansión. **Función:** punto refinado potencial para el retest de la base. **Estatus:** `PRECURSOR REFINADO EN M2020`; el PoR se conserva, pero la explicación posterior prioriza parte unpicked y release point refinado HTF→LTF.

### Skinny leg y clean breaking point

- Skinny leg es la salida fina del core tras superar la liquidity del borde; las pequeñas acumulaciones que quedan en esa pierna suelen ser residuales frente al core. [VID-PS: PriceSwing_02 @ 00:02:27–00:03:16]
- Clean breaking point es un nivel no testeado dentro de la salida que puede responder antes de alcanzar PoR/core; para EM eso puede significar simplemente **no trade** si su modelo exige PoR. [VID-PS: PriceSwing_02 @ 00:04:40–00:05:24] [VID-PS: PriceSwing_02 @ 00:08:43–00:09:37]
- **Estatus:** `CONFIRMADO/CONSERVADO EN M2020` morfológicamente; la preferencia exacta por PoR es personal/sample-dependent.

### Tres partes/fractales de la base

- EM trabaja top, middle y bottom: si top fue picked puede buscar middle/feeding fractal o bottom; el retorno más profundo puede producir respuesta mayor. No establece que cada contacto responda ni que exista orden obligatorio. [VID-PS: PriceSwing_02 @ 00:03:49–00:04:39]
- En el chart dice `there's three fractals to a base`, pero el cierre resume `three parts to a liquidity base`; visualmente refina múltiples subbases/fractales dentro del rango. [VID-PS: PriceSwing_02 @ 00:07:57–00:08:43] [VID-PS: PriceSwing_02 @ 00:18:12–00:18:31]
- **Estatus:** `PRECURSOR REFINADO EN M2020`: M2020 formaliza top/middle/bottom y considera drenada la base entera al alcanzar bottom.

## 4. Reglas y expectativas literales

- La conducta es fractal en cualquier chart; el HTF importa porque `these are going to pull more liquidity` relativamente. EM prefiere una base H1, baja a 5/15m para localizar PoR y usa la llegada ineficiente LTF. [VID-PS: PriceSwing_02 @ 00:05:27–00:06:51] [VID-PS: PriceSwing_02 @ 00:07:57–00:08:18]
- No impone ancho numérico: puede usar base H1 completa, PoR o bottom según tamaño y sample. [VID-PS: PriceSwing_02 @ 00:05:31–00:06:51]
- Variables que exige parametrizar: calidad de llegada, timeframe, partes ya picked, PoR/bottom, CBP untested y clusters de bases. [VID-PS: PriceSwing_02 @ 00:04:40–00:05:31] [VID-PS: PriceSwing_02 @ 00:16:58–00:17:28]
- Si el precio ofrece respuesta débil y vuelve por encima del entry point en un short ilustrativo, EM lo llama invalidación e infiere insufficient bid-side liquidity. Es un ejemplo visual, no distancia universal de stop. [VID-PS: PriceSwing_02 @ 00:13:20–00:13:41]

## 5. Comparación con M2020

- **Conservado:** core > residual; timeframe superior suele contener más liquidity; refinar al release; top/middle/bottom; llegada ineficiente como filtro.
- **Refinado:** PS02 trata PoR, bottom o CBP como selección personal derivada de muestras; M2020 S14 fija el nivel vigente como parte unpicked y el borde en release point, sin hacer obligatorio operar todos los contactos.
- **Refinado:** `psychological attachment` al origen [00:18:12] es explicación legacy no usada como mecanismo canónico M2020.
- **Sin contradicción:** EM rechaza reglas prestadas sin test: `until you actually have tested them ... they're just some random rules`. [VID-PS: PriceSwing_02 @ 00:17:24–00:17:45]

## 6. Setup/trade potencial

### Legacy swing retest of CLB

- **QUÉ:** regreso al core/origen del price run; entrada más favorable cuando un leg LTF fino/gap-slip atraviesa residual y alcanza core. [VID-PS: PriceSwing_02 @ 00:06:42–00:07:28]
- **CUÁNDO entra:** el vídeo propone decidir de antemano entre PoR, bottom, base completa o CBP según sample; no ofrece un trigger único. `NO ESPECIFICADO EN FUENTES` como contrato general.
- **DÓNDE invalida:** atravesar el entry point/área elegida aparece como invalidación en un ejemplo; distancia de stop `NO ESPECIFICADA EN FUENTES`. [VID-PS: PriceSwing_02 @ 00:13:20–00:13:41]
- **CÓMO gestiona:** respuesta esperada mayor desde core que desde residual, pero parciales/targets/BE `NO ESPECIFICADOS EN FUENTES`.
- **Estatus:** `SOLO PRICE SWING — NO CONFIRMADO DESPUÉS` como contrato legacy; sus filtros conceptuales sí fueron conservados/refinados. No se crea setup nuevo.

## 7. Evolución o contradicciones

- No hay contradicción material. El claim `high chance of a response` en top/middle/bottom no lleva tasa y queda subordinado por el propio EM a parts picked, timeframe, llegada y sample. [VID-PS: PriceSwing_02 @ 00:03:49–00:05:31]
- La explicación de que la base deja `psychological attachment` es vocabulario causal temprano no confirmado después; se registra como `SOLO PRICE SWING — NO CONFIRMADO DESPUÉS`, no como principio.

## 8. Resultado de la caza

- **Tradeable PI:** avance: core HTF + llegada LTF fina/gap-slip + selección PoR/bottom/CBP; sin taxonomía universal.
- **Extensión suficiente:** `further away` y leg cada vez más fino sustancian la idea, pero no hay distancia/tiempo mínimo. [VID-PS: PriceSwing_02 @ 00:06:51–00:07:28]
- **Washed:** `washing this fractal away` al recoger bottom después de top; antecedente de consumo, no SWE ni criterio completo. [VID-PS: PriceSwing_02 @ 00:11:27–00:11:37]
- **First touch/retest:** se estudian partes picked/untested y respuestas sucesivas, pero no se enuncia una regla universal de first touch.
- Resto de caza transversal: sin respuesta cerrada en PS02; consolidación única al final de PS05.

## 9. Erratas verificadas

- Whisper repite `call/equity base`; el audio-contexto, el slide `Liquidity Base` y las referencias posteriores permiten corregir a **core liquidity base**.
- `three parts to a equity base` se corrige a **three parts to a liquidity base**; no se infiere que `three fractals` sea una taxonomía distinta de top/middle/bottom.
