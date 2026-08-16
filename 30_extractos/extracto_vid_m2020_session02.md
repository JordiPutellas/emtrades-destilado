# Extracto — M2020 Session 2: proceso dinámico, order book y comportamiento dealer

> Fuente primaria: `Session 2.mp4` (01:37:55; pantalla fechada 10-sep-2020). Navegación: transcripción `.md/.srt/.json`. Revisados íntegramente la transcripción, los 15 frames indexados y el vídeo en los pasajes deícticos/ambiguos. Se aislaron y comprobaron por audio las menciones a `FTR` de 00:12–00:16. Correcciones conservadoras de Whisper en las citas/paráfrasis: market price, Quasimodo, bid/ask, market-to-limit-order ratio, inventory y Fiat Punto. Los números del order book y de las simulaciones son ejemplos pedagógicos, no parámetros operativos.

## 1. Apertura: análisis anticipatorio y trade incompleto

- En GBPUSD H1, EM repasa la semana desde el jueves: el lunes empezó la venta sin pullback; el martes volvió a vender y perdió **0,2%**; el miércoles llegó el movimiento que esperaba. A medida que la presión vendedora perdía momentum/tapered off, el precio rebotó contra la venta previa; EM lo presenta como la primera oportunidad significativa de swing de la semana. [VID-M2020: Session 2 @ 00:00:03–00:00:59]
- Su expectativa era un fill hacia **1.2750** porque el precio había extendido por encima de un swing high mayor. Formula el claim: “**It almost always fills**”. Es una afirmación contextual de EM pendiente de validación, no una regla universal. [VID-M2020: Session 2 @ 00:00:59–00:01:36]
- Considera tardío esperar al break/retest convencional de market structure: quiere evaluar la fuerza/debilidad **dentro del movimiento y antes de que se forme el high**. Habla de una “certain sequence of events”, pero en esta sesión no enumera sus componentes; promete desarrollarlos cuando introduzca las estructuras. [VID-M2020: Session 2 @ 00:01:39–00:02:38] [VID-M2020: Session 2 @ 00:17:40–00:18:37]
- La ventaja anticipatoria se explica como **informational asymmetry**: detectar información que aún no está reflejada en precio. En mercados electrónicos, las noticias se incorporan casi instantáneamente y el retail no tiene la velocidad para explotar el headline; su alternativa es un framework visual que evalúe el movimiento mientras se desarrolla, antes de que llegue la confirmación visible para otros traders. [VID-M2020: Session 2 @ 00:02:45–00:06:36]
- EM recalca que ni la lectura anticipatoria ni el market structure break garantizan el resultado; las probabilidades pueden cambiar con información nueva. [VID-M2020: Session 2 @ 00:06:41–00:07:04]

### ¿Merece un TE nuevo?

- **Contexto:** GBPUSD, lunes-miércoles, venta que pierde momentum y extensión por encima de un swing high. **Dirección/expectativa:** short/fill hacia 1.2750. **Pérdida conocida:** 0,2% el martes, sin vínculo inequívoco con la posición mostrada. [VID-M2020: Session 2 @ 00:00:03–00:01:36]
- **Entrada:** NO ESPECIFICADA. **Invalidación/stop:** NO ESPECIFICADOS. **Gestión:** NO ESPECIFICADA. **Resolución:** no se documenta que 1.2750 sea alcanzado ni el resultado de una ejecución concreta.
- Conclusión: **no crear TE** en `05_trade_examples.md`. Es análisis retrospectivo/expectativa de apertura con campos operativos esenciales ausentes.

## 2. Setup aislado frente a proceso dinámico

- Una probabilidad validada pertenece al sample set, no al siguiente trade. Los resultados se distribuyen aleatoriamente: un setup con expectancy positiva puede encadenar pérdidas y los parámetros “perfectos” no garantizan el resultado individual. Los porcentajes 60/40, 70% y 99% son ejemplos didácticos, no estadísticas aportadas por EM. [VID-M2020: Session 2 @ 00:07:04–00:13:15]
- Además, la probabilidad de mercado **cambia durante el trade** al entrar información nueva. De ahí el problema de un setup estático: puede ser favorable al entrar y dejar de serlo mientras se desarrolla. [VID-M2020: Session 2 @ 00:11:04–00:11:44]
- La solución que propone EM es **trade management + evaluación en tiempo real** mediante un proceso apropiado para probabilidades cambiantes. Variables: anatomía visual/estructural de ganadores y perdedores, punto y secuencia donde suelen fallar, variaciones de fallo/éxito, y transición de favorable a desfavorable. [VID-M2020: Session 2 @ 00:13:17–00:16:42]
- La regla de proceso es explícita: trackear precio constantemente y revisar incoming information; ver las características esperadas de reversión no basta. Cuando la idea se vuelve inválida y existe oportunidad de salir, no tiene sentido seguir esperando más allá de la invalidación. [VID-M2020: Session 2 @ 00:17:40–00:18:11] [VID-M2020: Session 2 @ 00:21:24–00:21:40]
- Para refutar un comportamiento exige sample set suficientemente grande: dos o tres fallos consecutivos no invalidan por sí solos una relación probabilística. A la vez, afirma que en los fallos suele haber tiempo/espacio para ver que la idea se deteriora y aplicar una countermeasure; no propone “cerrar los ojos” y dejar que el porcentaje histórico opere mecánicamente. [VID-M2020: Session 2 @ 00:18:38–00:21:13]
- Crítica adicional: los modelos mean-reversion/indicadores sobreoptimizados para un entorno dejan de funcionar cuando cambia la volatilidad; los breakouts convencionales también pierden frecuencia en mercados más eficientes. [VID-M2020: Session 2 @ 00:42:29–00:43:18]

### FTR — verificación y procedencia

- El audio dice repetidamente **FTR**: “your Quasimodo or your FTR pattern”, “FTR setup”, “variations of FTR”. La pantalla no muestra una expansión de la sigla y EM tampoco la expande verbalmente. [VID-M2020: Session 2 @ 00:12:04–00:13:15] [VID-M2020: Session 2 @ 00:15:05–00:16:20]
- En esta sesión FTR es un **ejemplo hipotético de setup/patrón ya conocido por el alumno**, colocado junto a Quasimodo para explicar distribución de resultados y gestión. No se atribuye a EM, no se define su anatomía y no se ofrecen trigger, invalidación ni gestión propios. Por tanto, no se incorpora a `03_setups.md`.

## 3. Market-to-limit-order ratio y lado menos líquido

- En un exchange, best bid = buy order más alta y best offer/ask = sell order más baja: los dos precios más competitivos del libro. [VID-M2020: Session 2 @ 00:21:42–00:23:10]
- **Limit order:** price-sensitive, pasiva y price-making; aporta liquidez. **Market order:** time-sensitive/urgente, agresiva y price-taking; consume la liquidez disponible levantando el offer o golpeando el bid. [VID-M2020: Session 2 @ 00:23:14–00:24:44]
- El coste de la market order es aceptar el fill disponible y barrer niveles peores si no existe suficiente profundidad; el coste de la limit es el riesgo de no ejecución. [VID-M2020: Session 2 @ 00:31:23–00:32:56]
- EM formula el **market-to-limit-order ratio**: cuando las market orders superan las limits disponibles en una dirección, consumen esos niveles y desplazan el best price. Lo llama su primer principio presentado en esta sesión y mecanismo de price discovery. [VID-M2020: Session 2 @ 00:26:04–00:30:21] [VID-M2020: Session 2 @ 00:33:13–00:33:35]
- Su esquema central separa **volumen transaccionado** de **profundidad disponible**. Un vendedor ejecuta mucho más volumen contra un bid profundo sin moverlo; simultáneamente, un comprador pequeño barre un ask fino y mueve el precio al alza. Por tanto, puede haber más volumen vendedor que comprador y aun así subir el precio. [VID-M2020: Session 2 @ 00:33:35–00:38:11]
- El lado débil/fino es el de menor depth de limit orders. Es más fácil que allí el market-to-limit ratio supere uno; por eso “**price goes to the less liquid side**”. EM dice que la probabilidad queda asimétricamente sesgada hacia ese lado, aunque reconoce que identificarlo no es fácil y que el estado más sesgado dura poco porque requiere muy poco volumen para desplazarse. [VID-M2020: Session 2 @ 00:38:11–00:45:17] [VID-M2020: Session 2 @ 01:01:24–01:03:09]
- **Liquidez no equivale a volumen:** la primera es profundidad/fricción disponible; el segundo es lo que efectivamente transacciona. Una gran limit bloquea el paso mientras permanezca: para atravesarla hay que consumirla o que sea retirada. [VID-M2020: Session 2 @ 00:35:02–00:38:11] [VID-M2020: Session 2 @ 01:04:31–01:06:30]
- Horizonte temporal: en FX el volumen potencial a largo plazo es prácticamente ilimitado y suele existir actividad multidireccional, pero en cualquier segundo puede secarse. La oportunidad nace de la sequedad/asimetría puntual, no de asumir que entrará permanentemente más volumen direccional. [VID-M2020: Session 2 @ 00:46:28–00:48:10]
- Frente a análisis técnico arbitrario, muestra un chart de 40.000 coin tosses que admite trendlines y “break of midflow”. Su criterio de edge no es que una forma sea visible, sino que la asimetría proceda de las reglas transaccionales limit-vs-market y sobreviva a muestras amplias. [VID-M2020: Session 2 @ 00:48:29–00:54:47]

### Relación con los nueve liquidity principles

- **Principio 1 (volatilidad = f de liquidez):** desarrollado por el secado/retirada de un lado del libro y el aumento posterior de volatilidad dealer-driven. [VID-M2020: Session 2 @ 01:21:45–01:25:28]
- **Principio 2 (precio al lado menos líquido):** formulación directa y explicación causal mediante market-to-limit ratio. [VID-M2020: Session 2 @ 00:40:45–00:45:17]
- **Principio 6 (buscar/encontrar/consumir liquidez):** limits = fricción; markets = consumo. [VID-M2020: Session 2 @ 01:04:31–01:06:30]
- **Principio 7 (extensions fill):** reiterado como “almost always fills”, pero sin cuantificación ni condiciones suficientes; queda como claim a validar. [VID-M2020: Session 2 @ 00:01:27–00:01:36]
- No modifica los otros cinco principios ni usa “transfer of liquidity”.

## 4. Dealers, inventario, last look e information leakage

- Exchange: single venue/book y best prices order-driven. OTC: múltiples dealers con sus propios books/quotes; un agregador puede presentar los mejores quotes como un libro compuesto, pero no los convierte en un único book central. [VID-M2020: Session 2 @ 01:06:56–01:07:40] [VID-M2020: Session 2 @ 01:13:13–01:14:10]
- Cada dealer fija bid/ask, compra para construir inventory, vende para descargarlo y busca capturar el spread. La competencia hace que un dealer fuera de precio no reciba el otro lado y quede atrapado con inventario. [VID-M2020: Session 2 @ 01:08:02–01:12:56]
- Los quotes OTC no son bona fide limits equivalentes a las del exchange: el contrato puede conceder **last look**, con el que el dealer rechaza o re-cotiza un trade si detecta que su precio quedó desfasado/adverso. Esto mitiga pricing errors, pero no elimina inventory risk posterior. [VID-M2020: Session 2 @ 01:13:49–01:17:08]
- **Toxic inventory / inventory risk:** si el dealer compra y el mercado cae antes de encontrar comprador, queda largo a un precio demasiado alto. Puede terminar vendiendo agresivamente y aceptar pérdida para descargar inventario. [VID-M2020: Session 2 @ 01:17:12–01:20:34] [VID-M2020: Session 2 @ 01:26:37–01:28:07]
- **Hot potato trading e information leakage:** la descarga urgente de un dealer revela información a competidores; estos también venden el inventario y retiran/asimetrizan bids. Venta agresiva + bid side seco genera price run y más volatilidad. EM aclara que el hot potato clásico ya no era dominante en 2020, aunque persistía algún elemento. [VID-M2020: Session 2 @ 01:20:34–01:25:28]
- Estado más favorable para un dealer: flujo comprador y vendedor simultáneo y equilibrado, que permite casar ambos lados y capturar el spread repetidamente sin acumular inventario direccional. [VID-M2020: Session 2 @ 01:25:55–01:27:14]
- En exchange también existe un juego informativo: una nueva limit grande cambia la conducta ajena, pero puede ser layering/spoofing y retirarse antes de ejecución. La información visible es observable, no necesariamente intención firme ni mapa completo de liquidez. [VID-M2020: Session 2 @ 01:30:19–01:34:55]

## 5. Riesgo, suerte y tolerancia psicológica

- Las simulaciones muestran que estrategias con la misma probabilidad/expectancy pueden producir recorridos de equity muy distintos por distribución aleatoria; un resultado extraordinario no prueba por sí solo habilidad y uno mediocre no implica parámetros distintos. [VID-M2020: Session 2 @ 00:56:11–01:01:18]
- El tramo final usa una anécdota sobre un trader extremo para separar skill, suerte y exposición: riesgo extraordinario puede producir un outlier ganador o uno ruinoso. Los comentarios biográficos/coloquiales no constituyen doctrina ni una recomendación de sizing. [VID-M2020: Session 2 @ 01:31:19–01:37:11]
- Conclusión directa de EM: la mayoría tiene un límite monetario de pérdida/ganancia a partir del cual se deteriora su estado psicológico en el corto plazo. No formula aquí un porcentaje ni una regla universal de riesgo. [VID-M2020: Session 2 @ 01:37:12–01:37:49]

## 6. Caza prioritaria

1. **CPS como setup:** AUSENTE.
2. **SWE / washed shelf-specific:** AUSENTE.
3. **Parámetros Washed IV/CPL:** AUSENTES.
4. **Cuatro apexes / gestión dentro de apex:** AUSENTES.
5. **Poke past low del OP:** AUSENTE.
6. **Responsive vs market-state-dependent:** AUSENTE.
7. **YO/WO/MO:** `MO` aparece como etiqueta visual en el chart inicial, pero no se explica ni se dan reglas; solo EJEMPLO COMPATIBLE.
8. **Momentum trade / trade models:** habla de strength/momentum y tapering, pero no del setup “momentum trade” ni de trade models; AUSENTE como respuesta.
9. **Tradeable vs non-tradeable PI:** AUSENTE.
10. **Extensión suficiente para counter-trend:** el fill de extensión se afirma, pero no ofrece criterio de suficiencia ni separa rebalance de reversal; AVANCE NULO para la pregunta concreta.
11. **Transfer of liquidity:** AUSENTE en 01:37:55 y sin variante conceptual equivalente; el mecanismo usado es market-to-limit ratio, depth, inventory y withdrawal.
12. **Triggers/invalidación/gestión para S-01–S-09:** ninguna ampliación específica. Solo regla transversal: reevaluar en tiempo real y salir cuando la idea se invalida.
13. **Mapa lección↔vídeo:** anuncia que las estructuras y la secuencia de strength/weakness llegarán después; al cierre dice que la siguiente sesión continuará con estructura FX/OTC y preguntas sobre best bid/offer, dealers e information leakage. [VID-M2020: Session 2 @ 00:17:40–00:18:37] [VID-M2020: Session 2 @ 01:28:07–01:28:49]

## 7. C-001 y C-002

- **C-001:** “transfer of liquidity” no aparece. Acumulado M2020: S1, S2 y S12–S15 = seis sesiones, ~7h59, sin el término.
- **C-002:** Session 2 desarrolla la resolución existente, no la contradice: exchange tiene un book común observable, mientras OTC agrega quotes revocables de dealers; además, book visible no significa información exhaustiva ni intención garantizada porque pueden existir layering/spoofing/cancelación. [VID-M2020: Session 2 @ 01:13:13–01:17:08] [VID-M2020: Session 2 @ 01:30:19–01:34:55]

## 8. Integración

- `01_principios.md`: ratio market-to-limit, profundidad vs volumen y mecanismo dealer/inventory.
- `02_conceptos.md`: FTR sin expansión, best bid/offer, market-to-limit ratio, dealer inventory/hot potato.
- `04_proceso.md`: probabilidades dinámicas, tracking en real time, invalidación y sample sets.
- `90_preguntas_abiertas.md`: claims nuevos y Session 2 retirada de candidatos agotados.
- `91_contradicciones.md`: C-001 acumulada y evidencia compatible añadida a C-002.
- `05_trade_examples.md` y `03_setups.md`: sin cambios; no hay trade completo ni setup nuevo atribuible a EM.
