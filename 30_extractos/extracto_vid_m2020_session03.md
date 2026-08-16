# Extracto — M2020 Session 3: price reflects liquidity, estructura FX y price discovery

> Fuente primaria: `Session 3.mp4` (01:44:50; pantalla fechada 24-sep-2020). Navegación: transcripción `.md/.srt/.json`. Revisados íntegramente la transcripción, los 18 frames indexados y el vídeo/audio en los pasajes deícticos o ambiguos. Las explicaciones institucionales e históricas se registran como afirmaciones de EM, no como hechos verificados externamente; los importes, spreads, márgenes, leverage y ATR son ejemplos/lecturas pedagógicas. Correcciones conservadoras de Whisper: buy liquidity, tier-one bank, Bank for International Settlements, Deutsche Bank, Roel Oomen, inventory, EBS, Reuters FX Spot Matching, GBPUSD/EURUSD, Virtu y FXCM.

## 1. `Price reflects the state of liquidity`

- El alumno Zain recuerda el market-to-limit-order ratio. EM precisa que, cuando la market order iguala o supera la limit liquidity disponible, consume el nivel; si queda volumen por ejecutar, busca la siguiente contrapartida y cambia el best price. [VID-M2020: Session 3 @ 00:00:00–00:02:12]
- EM formula el alcance directo: “**it's only market orders that move the market**” y “**it's impossible for a limit order to move the market**”. La limit no puede ejecutarse a peor precio que el fijado: es price-making, liquidez y fricción; la market es la orden que cruza/consume y desplaza mecánicamente el precio ejecutado. [VID-M2020: Session 3 @ 00:02:12–00:03:30]
- **Matiz de alcance dentro de la propia sesión:** esa formulación se refiere a la ejecución directa. EM también contempla que sell limits se retiren, reduzcan o repricien; eso modifica el book y la distancia que recorrerá la siguiente market order, aunque la limit no sea la orden que cruza el spread. No hay contradicción: market order = desplazamiento mecánico; quote withdrawal/repricing = cambio previo de fricción y efecto indirecto sobre distancia/volatilidad. [VID-M2020: Session 3 @ 00:14:01–00:15:44] [VID-M2020: Session 3 @ 00:27:02–00:29:40] [VID-M2020: Session 3 @ 00:30:30–00:31:23]
- **`Skewed liquidity` no es flujo direccional:** describe dónde descansan las limits y su profundidad relativa. Si los bids son mucho más gruesos que los offers, el book está sesgado a favor del buy side: hace falta más venta agresiva para bajar que compra agresiva para subir. Es una asimetría de fricción/probabilidad, no contar market buys frente a market sells. [VID-M2020: Session 3 @ 00:04:05–00:06:09]
- El market maker/dealer posee ventaja informativa por su función: ve gran cantidad de customer order flow y, además, su propia vista de liquidez/quotes. “Bank” por sí solo no basta; la ventaja que EM describe nace de **hacer mercado** y ser contraparte de clientes, no de una etiqueta institucional genérica. Los importes de cientos de miles de millones/trillones son ejemplos extremos. [VID-M2020: Session 3 @ 00:06:36–00:13:17]
- Ejemplo causal: ante un comprador muy grande, el LP no quiere quedar short, refuerza/acompaña bids y reduce sell liquidity. El flujo original justifica una subida; la reacción del dealer reduce la fricción y obliga al remanente a viajar más para hallar sellers, por lo que el run recorre más distancia de la que explicaría por sí solo el volumen inicial. EM separa así **impulso original** de **amplificación dealer-driven**. [VID-M2020: Session 3 @ 00:13:17–00:16:26]
- Una foto microsegundo a microsegundo del book puede mostrar buy liquidity muy estirada/fina tras el run; después las quotes pueden reaparecer, retirarse o cambiar de lado. La instantánea explica el estado en ese instante, no el desarrollo futuro completo. Incluso sin un aumento de sellers, una sell liquidity que sigue fina puede bastar para que el precio caiga si el buy side quedó aún más débil. [VID-M2020: Session 3 @ 00:16:26–00:18:16]
- Formulación exacta de EM: “**Basically, there's a principle, another principle, that price reflects state of liquidity.**” Imbalance y exhaustion dejan estructuras visuales, ritmo/tick rate y distancia recorrida diferentes. Heatmap/bookmap podría mostrarlos directamente, pero EM afirma que el mismo estado puede inferirse en price action con el framework adecuado, sin necesitar order book. [VID-M2020: Session 3 @ 00:18:28–00:21:24]
- Límite epistemológico: en esta fase no enseña todavía las estructuras visuales ni promete certeza ex ante. El ratio permite explicar después del hecho que tuvo que existir imbalance; aprender a reconocerlo durante el desarrollo exige observar muy de cerca la secuencia miles de veces y actualizarse con cada nueva información. [VID-M2020: Session 3 @ 00:21:39–00:26:42]

## 2. Estabilidad, absorción, secado y práctica personal de riesgo

- Tras un sell-off agresivo, EM espera que market volume se seque, aumentando la probabilidad de que el precio vuelva a rango; aclara que ese secado es **a veces** tradeable, no siempre. El día anterior perdió aproximadamente 0,2% y por eso estuvo dispuesto a operar de noche el drawback/range posterior. [VID-M2020: Session 3 @ 00:32:18–00:33:09]
- En el entorno mostrado (GBPUSD, rango aproximado de 50–65 pips), las buy limits absorben market sellers en el low y las sell limits absorben market buyers en el high. Esa suficiencia bilateral de limit liquidity mantiene estabilidad y baja agresividad relativa. [VID-M2020: Session 3 @ 00:33:09–00:35:46]
- EM rechaza reducirlo a `range` o `bearish trend`: quiere leer tempo/rhythm. Un descenso puede alternar desplazamientos breves con largos tramos estables y tener implicaciones operativas distintas de un sell-off continuo aunque ambos se llamen tendencia bajista. [VID-M2020: Session 3 @ 00:34:23–00:37:50]
- [INFERENCIA] La explicación desarrolla **volume stability / balanced liquidity** y es compatible con LLS, pero EM no usa aquí `LLS`; no se reetiqueta automáticamente el rango como tal. [VID-M2020: Session 3 @ 00:33:09–00:35:46]
- EM dice que reconoce ese entorno estable y lo “milks”: enumera haber capturado dos lows y un retest, pero no aporta entradas, stops, gestión ni resultado por operación. En un entorno agresivo prefiere early morning/late day; en el estable está dispuesto a operar durante más franjas. [VID-M2020: Session 3 @ 00:37:50–00:39:57]
- Audio confirmado: “**Like I said to you, I don't really risk more than 0.2% on the trade.**” Es una política personal real de EM en el contexto de su operativa de esa fecha (24-sep-2020); no identifica cuenta concreta, no la convierte en consejo y no prescribe ese porcentaje al alumno. Es compatible con la pérdida diaria aproximada de 0,2% mencionada en Sessions 2–3; no contradice otra regla de riesgo del corpus. [VID-M2020: Session 3 @ 00:38:27–00:38:46]

## 3. Mapa institucional de FX según EM

- EM separa bancos domésticos/comerciales de bancos globales tier-one. Describe depósito, préstamo, liquidez interbancaria, regulación/reservas y relación con banco central/BIS solo para llegar a su punto: los tier-one tienen relaciones de crédito entre sí y son los principales proveedores de liquidez que le interesan. Su explicación de banca, dinero y regulación es pedagógica y simplificada. [VID-M2020: Session 3 @ 00:40:03–00:48:32]
- Dentro de un tier-one distingue wealth management, banca doméstica, corporate treasury e investment banking. Para FX importan treasury services, lending, sales y liquidity provision; pone IPO/M&A como contexto de servicios, no como mecánica de precio. [VID-M2020: Session 3 @ 00:48:32–00:52:41]
- Una corporación multinacional mantiene ingresos/costes en varias monedas y necesita convertir o cubrir currency risk. El banco asume/facilita esa transacción; puede ser enorme sin intención especulativa. [VID-M2020: Session 3 @ 00:52:41–00:54:39]
- FX no es solo spot: EM enumera spot, forwards y swaps; las cifras de volumen y las definiciones rápidas son claims pedagógicos no verificados. Los bancos pueden especializarse por producto/cliente/ejecución electrónica. [VID-M2020: Session 3 @ 00:55:32–00:57:38]
- La fuente de ingresos que enfatiza es transaccional/de servicio y basada en relaciones con clientes, no apostar contra stops retail. El banco vende acceso, ejecución y liquidez y busca conservar customer flow. [VID-M2020: Session 3 @ 00:57:38–00:59:16]
- Metáfora central: FX es un **conduit/plumbing** para acceder a monedas, activos, comercio y cobertura entre países, no principalmente un risk asset que todos compran para especular. Por eso el flujo es heterogéneo y gran parte puede ser operativo o de hedge: corporates, asset managers/hedge funds, pension funds y governments. [VID-M2020: Session 3 @ 00:59:16–01:04:13]
- Definición funcional: **sell side** vende/provee el servicio de liquidez; **buy side** lo compra/consume, incluso cuando la firma está vendiendo una divisa. Incluye corporates, funds, governments y clientes de prime brokerage; excluye al retail sin relación directa con bancos. [VID-M2020: Session 3 @ 01:00:39–01:01:52]

## 4. Voice broker → EBS/Reuters → price discovery

- En el interbank voice-brokered, un banco que quería descargar inventario debía buscar contrapartida por teléfono y comprobar relaciones de crédito; EM lo describe como lento y arriesgado mientras el precio podía moverse. Es una reconstrucción histórica de EM, no verificación externa. [VID-M2020: Session 3 @ 01:04:21–01:08:03]
- Según EM, EBS (Electronic Broking Services) y Reuters FX Spot Matching aparecieron a comienzos de los 90 como plataformas electrónicas interdealer: single order book, matching automático y **pre-trade credit**. Permitían descargar inventory risk más rápido y mejoraron la distribución de precios. [VID-M2020: Session 3 @ 01:08:03–01:10:49]
- Asignación que hace EM: EURUSD principalmente en EBS y GBPUSD en Reuters FX Spot Matching; menciona USDJPY/USDCHF como repartidos entre una u otra sin mapping inequívoco. Tratar pares/fechas como claim histórico de EM. [VID-M2020: Session 3 @ 01:10:49–01:11:47]
- Los banks miraban cambios de best bid/offer en EBS y actualizaban los quotes distribuidos a clientes. Cuando gran parte del volumen interdealer estaba allí, EM sitúa allí el **price discovery**: información entra, cambia primero el precio interdealer y después se redistribuye al tier cliente. El participante más cercano al punto de formación recibe antes la información. [VID-M2020: Session 3 @ 01:11:47–01:15:15] [VID-M2020: Session 3 @ 01:18:40–01:20:38]
- “**all the liquidity is posted here**” es una simplificación del esquema; segundos después EM dice “**90% or 70%**”. Su alcance es concentración de una gran parte del interdealer visible/ejecutable, no totalidad de la liquidez latente, futura o irrevocable. C-002 no se reabre. [VID-M2020: Session 3 @ 01:12:28–01:13:23]
- Mecanismo de leakage: si un bank cubre en EBS un buy de cliente, otros dealers reciben/venden inventario, responden/hacen hot potato y el precio sube contra el cliente mientras completa el ticket. La orden original se hace visible por su impacto, aumenta slippage/execution cost y, según EM, contribuye a mayor volatilidad. [VID-M2020: Session 3 @ 01:15:15–01:17:13]
- Alternativa: el bank internaliza/warehousea el riesgo sin enviar la operación a EBS; competidores no conocen cliente, tamaño ni dirección, hay menos information leakage y potencialmente menos slippage. No implica que el riesgo desaparezca: solo se gestiona fuera del book interdealer visible. [VID-M2020: Session 3 @ 01:17:13–01:18:40]

## 5. Prime brokerage y distribución retail

- Un cliente que quiere los mejores quotes de varios banks necesitaría relaciones de crédito/margen con cada uno, multiplicando counterparty exposure. Prime brokerage permite usar una sola relación/nombre de bank para acceder a quotes de otros dealers; el PB intermedia crédito y cobra comisiones/servicio. Los importes de margen y comisión son ejemplos. [VID-M2020: Session 3 @ 01:21:03–01:26:43]
- Con la expansión retail por internet, brokers compran liquidez/quotes a bancos y la revenden. Mediante PB/agregación pueden formar el best bid/best offer de bancos distintos, añadir spread al cliente y capturar la diferencia. El broker puede cubrir inmediatamente al mejor quote o decidir conservar/internalizar el riesgo. Los cálculos de 0,6/5 pips son pedagógicos. [VID-M2020: Session 3 @ 01:26:43–01:33:27]
- El PB también concede leverage contra margin; EM usa 50:1 y $100m→$5bn solo como ejemplo, no como estándar de mercado. [VID-M2020: Session 3 @ 01:33:27–01:35:38]
- Session 4 queda anunciada para: ocultación de identidad del cliente mediante PB; fallos/riesgo de prime brokers y banks; co-location/HFT; y continuación de la evolución de estructura FX. Como antecedente cita el episodio CHF/SNB de 2015 y la deuda de FXCM con su PB; cifra y relato quedan como claims históricos de EM. [VID-M2020: Session 3 @ 01:35:38–01:36:45] [VID-M2020: Session 3 @ 01:39:54–01:40:25]

## 6. HFT, co-location y cambio histórico de volatilidad

- La cercanía al punto de price discovery crea ventaja cuando EBS cambia antes que el quote redistribuido. Con tecnología sub-second, clientes/HFT pueden explotar ese retraso; EM anuncia co-location como forma de recibir antes los updates. No lo convierte en señal accesible al trader retail. [VID-M2020: Session 3 @ 01:37:15–01:40:25]
- Claim/anécdota sin validar: EM muestra una búsqueda sobre **Virtu** y afirma un solo losing day en 1.238 días. Sirve para ilustrar el edge tecnológico sub-second, no como evidencia estadística del método. [VID-M2020: Session 3 @ 01:38:45–01:39:50]
- Hipótesis histórica de EM: evolución tecnológica, competencia y cambios en liquidity provision alteraron el price action y redujeron la volatilidad respecto a épocas previas. En gráficos D1 con ATR(14), lee aproximadamente GBPUSD 59–166 pips/día en etapas recientes, picos de ~400 durante GFC y medianas antiguas ~140–150; para EURUSD muestra largos periodos de ~50 pips/día frente a ~100–110 antes. Son lecturas aproximadas de pantalla, no una serie validada. [VID-M2020: Session 3 @ 01:40:31–01:44:47]
- Atribuye la volatilidad relativa de GBP en ese periodo al contexto Brexit. Es explicación contextual de EM, no una regla causal general. [VID-M2020: Session 3 @ 01:42:32–01:43:03]

## 7. Caza prioritaria

1. **CPS como setup:** AUSENTE.
2. **SWE / washed shelf-specific:** AUSENTES.
3. **Parámetros Washed IV/CPL:** AUSENTES.
4. **Cuatro apexes / gestión dentro de apex:** AUSENTES.
5. **Poke past low del OP:** AUSENTE.
6. **Responsive vs market-state-dependent:** AUSENTE.
7. **YO/WO/MO:** `YO`, `WO` y `MO` son visibles como etiquetas en charts, pero EM no las comenta ni da reglas; solo EJEMPLO VISUAL COMPATIBLE.
8. **Momentum trade / trade models:** AUSENTES.
9. **Tradeable vs non-tradeable PI:** AUSENTE. Solo dice que el secado de market volume es “sometimes tradable”, sin criterio PI.
10. **Extensión suficiente para counter-trend:** AUSENTE.
11. **Transfer of liquidity:** AUSENTE en 01:44:50 y sin variante conceptual equivalente; usa consumption, friction, withdrawal/repricing, dealer amplification, inventory e information leakage.
12. **Triggers/invalidación/gestión S-01–S-09:** AUSENTES. La política personal de 0,2% no es un trigger ni management estructural de setup.
13. **Referencias posteriores:** Session 4 cubrirá identidad/prime brokerage, fallos de PB, co-location/HFT y evolución de estructura FX. [VID-M2020: Session 3 @ 01:35:38–01:36:45] [VID-M2020: Session 3 @ 01:39:54–01:40:25]

## 8. Trades, setups y estado de contradicciones

- EM señala haber capturado dos lows y un retest en el entorno estable, y menciona cerrar la mayoría/runner como estilo posible, pero faltan entrada, invalidación, gestión por operación y resolución documentada. **No crear TE** en `05_trade_examples.md`. [VID-M2020: Session 3 @ 00:37:50–00:39:31]
- No hay setup nuevo: las explicaciones de imbalance, price discovery, estabilidad y microestructura no contienen contrato QUÉ/CUÁNDO/DÓNDE/CÓMO. [VID-M2020: Session 3 — revisión completa 00:00:00–01:44:50]
- **C-001:** `transfer of liquidity` no aparece. Acumulado M2020: S1–S3 y S12–S15 = siete sesiones, ~9h44, sin el término; permanece cerrada como evolución. [VID-M2020: Session 3 — revisión completa 00:00:00–01:44:50]
- **C-002:** no se reabre. “All liquidity” queda acotado por la rectificación inmediata a 70–90% y por el contraste visible book vs latent/hidden/cancelable liquidity ya documentado. [VID-M2020: Session 3 @ 01:12:28–01:13:23]

## 9. Integración

- `01_principios.md`: formulación y alcance de `price reflects the state of liquidity`, skew/dealer amplification, estabilidad y evolución de venue/volatilidad.
- `02_conceptos.md`: skewed liquidity, sell/buy side, EBS/Reuters, price discovery, information leakage y prime brokerage.
- `04_proceso.md`: lectura del tempo frente a etiquetas trend/range, observación secuencial y práctica personal de riesgo 0,2%.
- `90_preguntas_abiertas.md`: Session 3 retirada de candidatos agotados y nuevos claims de validación.
- `91_contradicciones.md`: C-001 acumulada a siete sesiones y C-002 acotada.
- `03_setups.md`, `05_trade_examples.md` y `92_ideas_btc.md`: sin cambios; no hay setup/trade completo ni diferencia OTC-vs-exchange nueva que justifique duplicar notas BTC.
