# Principios (EMTrades — destilado)

> Marco causal del método. Convenciones de fuentes en CLAUDE.md.

## Los 9 liquidity principles (lista canónica)

Del documento "Liquidity Principles" [PDF: Liquidity Principles]:

1. La volatilidad es una función de la liquidez disponible.
2. El precio va hacia el lado más débil / menos líquido.
3. El precio deja liquidez residual; la liquidez se transfiere a medida que el precio avanza. *(Ver C-001 en 91_contradicciones.md: [USUARIO] cuestiona "transfer of liquidity" como mecanismo.)*
4. Una base de liquidez tiene 3 lados: techo, medio y suelo.
5. Las bases de HTF acumulan más liquidez que las de LTF (liquidez = fricción).
6. El precio simplemente busca, encuentra y consume liquidez.
7. Las extensiones se rellenan — cuanto más lejos viaja el precio de forma ineficiente, más débil se vuelve.
8. Los price runs y swings son fractales: todas las escalas, todo el día.
9. La entrega eficiente de precio es muy fuerte... hasta que deja de serlo.

## Desarrollo (por módulo procesado)

### Volatilidad = f(liquidez disponible)

- "Liquidity (passive & active) is not a constant, volume is variable. Price goes to the weaker, less liquid side. Due to this price can move against the broader sentiment/trend even if it isn't a move with conviction." [PDF: The Price Run p.2]
- "If there's a void of offers above price and bids are coming in thicker (even slightly thicker), price will move through that weak area. Vice versa." [PDF: The Price Run p.4]
- Sentimiento ≠ volumen: en un chop de 9 días con sentimiento bajista estable (GBPUSD jul-2019), cada run alcista fue función de sell liquidity débil, no de cambio de sentimiento. [PDF: The Price Run p.4]

### Mecanismo institucional del price run (por qué existe la ineficiencia)

- Un LP institucional mueve sus quotes ante flujo entrante → respuesta en cadena de todos los LPs (protección anti-arbitraje: ensanchan spreads y sus pricing engines suben los precios) → los flujos "persiguen" las quotes → movimiento fino e ineficiente que **sobrepasa** (overshoot) y deja un **vacío de liquidez** detrás. [PDF: The Price Run p.1, p.8]
- Los LPs trocean órdenes grandes para casarlas sin mover el mercado; su trabajo termina cuando el inventario se llena — después el precio queda sin soporte y rebalancea por el vacío buscando liquidez. [PDF: The Price Run p.6, p.8]
- El disparador del run es **relativo**: "the 'increase' is relative, doesn't have to be massive, just more than the volume keeping price stable" — por eso muchos spikes se secan rápido y vuelven a la base. [PDF: The Price Run p.7, p.9]

### Ciclo canónico del price run

Estabilidad de volumen (low liquid state) → surge relativo en un lado → run fino/ineficiente → agotamiento (top "jumpy", bids exhausted) → shift de liquidez → rebalance a través del vacío → respuesta en la core liquidity base. [PDF: The Price Run p.5–p.10] [IMG: The Price Run p.10]

- "Contraction leads to expansion" explicado vía liquidez: el precio entra casi siempre en áreas de volumen bajo y estable (LLS, en todos los timeframes) que quedan expuestas a un shot de volumen en un lado. [PDF: The Price Run p.5]

### Fractalidad

- Todo swing contiene swings menores; el swing HTF es el contenedor de los fractales LTF. [IMG: Price Swing Basics video p.3–p.5]
- Los apexes fractales son auto-similares "regardless of scale or pip distance". [IMG: Price Swings Continued p.13]
- Los shelves son relativos a su timeframe: un shelf de 5min no afecta a un swing H1+; los shelves menores son el inventario de los swings fractales internos. [PDF: Price Swings Continued p.8]
- Mayor escala = más liquidez acumulada: "bigger shelf flips = bigger shifts in momentum, but bigger shelfs hold more liquidity — more work, more time". [PDF: Price Swings Continued p.10]

### Estados y shifts de liquidez

- El swing avanza alimentándose del shelf más cercano hasta que este no puede sostener el run; superar un shelf tras consumir la liquidez opuesta produce un **shift in the state of liquidity**: el otro lado toma el control. [PDF: Price Swings Continued p.8]
- Apex + shelf flip típicamente preceden shift y midflow. [PDF: Price Swings Continued p.8]
- Los **shifting points** son "decision points or momentum shifting, chain reaction effecting points — highly responsive areas". [IMG: Price Swings Continued p.4]
- Tras el shift, el precio corre por liquidez residual débil cuyas respuestas se absorben → midflow (continuación). [IMG: Price Swings Continued p.6]
