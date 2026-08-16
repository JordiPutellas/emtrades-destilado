# Extracto — M2020 Session 1: estructura OTC frente a exchange

> Fuente primaria: `Session 1.mp4` (28:18; metadata de creación 14-feb-2020). Navegación: transcripción `.md/.srt/.json`. Revisados los 3 frames indexados y fotogramas adicionales del vídeo en 00:02:50, 00:05:53, 00:10:24, 00:14:14, 00:16:43, 00:20:39, 00:22:39, 00:24:30 y 00:26:12. Citas corregidas conservadoramente: Deutsche Bank, principal, retail FX, execution size, FXCM, SNB, LMAX, ECN, aggregator, Currenex y cTrader.

## Propósito y alcance

- EM define OTC/exchange como las reglas o costumbres bajo las que se negocian activos; cualquier producto puede negociarse OTC, mientras los activos exchange-based siguen otro conjunto de reglas. [VID-M2020: Session 1 @ 00:00:14–00:00:53]
- Es una lección de organización y ejecución de mercado. **No presenta setup, trigger, invalidación, gestión ni reglas de price action.** Los ejemplos numéricos son pedagógicos; no se validan ni completan con conocimiento externo.

## OTC: bilateral, dealer/principal y riesgo

- Analogía literal: comprar al shopkeeper; la transacción ocurre entre cliente y proveedor. EM lo denomina **bilateral trading**, entre dos partes. [VID-M2020: Session 1 @ 00:00:55–00:01:52]
- En FX interbank el cliente pide quotes a un dealer. La operación se celebra directamente con él: si el cliente compra EUR/vende USD a Deutsche Bank, DB compra esos USD. Después el dealer decide si mantiene el riesgo, lo casa con otro cliente interno o se cubre en el mercado más amplio; esa decisión es independiente de la transacción bilateral original. [VID-M2020: Session 1 @ 00:01:54–00:03:19]
- El **counterparty risk** OTC recae en la contraparte directa. Para retail suele ser el broker: aunque se presente como ECN/no-dealing-desk, EM dice que actúa como **principal** —el cliente compra y el broker vende— y luego decide si cubre. [VID-M2020: Session 1 @ 00:03:34–00:04:35]
- Sobre retail FX: por el tamaño pequeño del flujo, el broker suele sentarse sobre él/internalizarlo; como mejor caso lo casa con otro cliente. Si no quiere asumir el neto, puede agregar muchas órdenes pequeñas y cubrir el agregado porque el LP bancario no acepta tickets diminutos (EM usa “beneath a million” como ejemplo). [VID-M2020: Session 1 @ 00:04:36–00:05:34]

## Exchange: multilateralidad, matching y CCP

- Exchange = **multilateral**. Una compra de 5M puede casarse contra un único vendedor o contra miles de órdenes pequeñas; a diferencia de OTC, no se negocia todo directamente con un único dealer/principal. [VID-M2020: Session 1 @ 00:05:34–00:06:59]
- La **central counterparty (CCP)** actúa como referee/intermediario: evita que el participante deba liquidar bilateralmente con cada contraparte, aplica reglas comunes y supervisa las transacciones. EM asocia este diseño con mayor seguridad y transparencia, especialmente de precio y equity disponible. [VID-M2020: Session 1 @ 00:07:07–00:08:16]
- Según EM, la CCP liquida la operación pero no toma la posición direccional como dealer; el riesgo de settlement/counterparty queda concentrado frente a ella. La analogía eBay: comprador y vendedor entregan dinero/bien al intermediario, que completa ambos lados. [VID-M2020: Session 1 @ 00:08:18–00:09:59]

## Formación y observación de precios

- **Exchange:** un solo order book para participantes del venue. Una limit visible se sienta en ese libro, cualquiera puede verla y acceder a ella; EM lo llama **order-driven pricing**. Los precios muestran dónde se encuentran oferta y demanda —el “equilibrium point”, en el punto más fino de liquidez— y cada tick/transacción queda registrado. [VID-M2020: Session 1 @ 00:10:01–00:12:17]
- **OTC:** **quote-driven**. El dealer elige y puede cambiar sus quotes; no son órdenes garantizadas. Puede rechazar/re-cotizar (last look), o la liquidez puede haber sido tomada antes de que llegue la orden y producir slippage. [VID-M2020: Session 1 @ 00:11:09–00:11:58] [VID-M2020: Session 1 @ 00:14:14–00:14:53]
- Resumen de EM: exchange = multilateral, single book, order-driven y más transparente; OTC = bilateral y quote-driven. En exchange puede haber slippage, pero no re-quote del dealer sobre una indicación bilateral. [VID-M2020: Session 1 @ 00:14:14–00:15:47]
- Los datos de exchange son valiosos porque EM los considera transparentes y respaldados por órdenes; la CCP/venue vende el acceso. Un CFD del broker replica el precio de un contrato subyacente, pero sus precios pueden ser indicativos y ligeramente distintos. [VID-M2020: Session 1 @ 00:12:17–00:14:12]

## Counterparty risk y settlement OTC

- EM explica settlement FX con T+2: la operación no implica entrega física instantánea. Entre trade y settlement la contraparte puede deteriorarse hasta no poder pagar; por eso el riesgo bilateral es real. [VID-M2020: Session 1 @ 00:16:34–00:18:18]
- Ejemplos de EM: el shock CHF/SNB de 2015 dejó a FXCM con un agujero aproximado de $300M y clientes ganadores que el broker no podía pagar sin financiación; incluso bancos grandes pueden quebrar (Lehman). La lección es riesgo de contraparte, no un setup ni una regla de precio. [VID-M2020: Session 1 @ 00:18:21–00:20:08]

## Por qué persiste OTC

- Ventajas que EM atribuye a OTC: costumbre histórica, anonimato de la transacción bilateral y flexibilidad para crear soluciones específicas para participantes no necesariamente especulativos (multinacionales, gestores, necesidades comerciales). Exchange registra operaciones y exige reglas uniformes orientadas al trading competitivo. [VID-M2020: Session 1 @ 00:20:20–00:22:28]
- Trade-off final: OTC es flexible/anónimo pero más difícil de regular y permite prácticas dudosas; los dealers tier-one siguen el FX Global Code, aunque EM dice que resulta difícil hacerlo cumplir. [VID-M2020: Session 1 @ 00:27:39–00:28:09]

## Estructuras intermedias dentro de FX

- **LMAX / MTF:** EM lo presenta como modelo exchange-like dentro de FX: bancos y clientes introducen limits en un single order book, precio order-driven; LMAX se interpone como contraparte y el riesgo del cliente queda frente a LMAX, no directamente frente al banco que aporta la limit. [VID-M2020: Session 1 @ 00:22:34–00:24:22]
- **ECNs (Hotspot, FXall, Currenex):** agregan liquidez de bancos conectados/credit lines y facilitan anonymous order routing; EM dice que el agregador no toma el riesgo principal, sino que facilita. [VID-M2020: Session 1 @ 00:24:30–00:25:42]
- **Retail:** el broker sigue llenando al cliente y elige asumir, casar internamente o cubrir el riesgo. En MT4, según EM, el broker toma quotes de proveedores y controla cómo se reflejan en el backend; cTrader muestra directamente los quotes de los agregadores integrados. Aun con cTrader, el fill llega al servidor del broker, que puede cubrir o internalizar; EM lo llama “slightly more transparent”, no completamente transparente. [VID-M2020: Session 1 @ 00:25:29–00:27:25]

## Consecuencias para interpretar precio, liquidez y ejecución

1. **Identificar la organización antes de interpretar los datos.** En OTC se observan quotes bilaterales/fragmentadas; en exchange, órdenes mostradas y trades de un libro común. No tratar ambos feeds como el mismo objeto. [VID-M2020: Session 1 @ 00:10:01–00:12:17]
2. **El flujo del cliente no implica impacto en el mercado amplio.** Un dealer/broker puede internalizarlo, casarlo o cubrir solo el neto agregado. [VID-M2020: Session 1 @ 00:02:38–00:03:19] [VID-M2020: Session 1 @ 00:04:36–00:05:34]
3. **Quote visible no equivale a ejecución garantizada en OTC.** Re-quote, last look, slippage y cambio del quote son parte de la estructura descrita. [VID-M2020: Session 1 @ 00:11:32–00:11:58] [VID-M2020: Session 1 @ 00:14:29–00:14:53]
4. **La transparencia de exchange es relativa al libro mostrado y al registro.** Esta sesión no afirma que toda la liquidez futura/latente sea visible; fuentes posteriores dicen explícitamente que gran parte está oculta incluso en futuros. Se registra el matiz en C-002. [VID-M2020: Session 1 @ 00:10:01–00:12:17] [DISCORD: answers] [DISCORD: Disc 64–65]
5. **No deriva una regla gráfica.** La consecuencia es epistemológica/ejecutiva: saber qué representa el precio observado y quién es la contraparte, no convertir OTC-vs-exchange en señal de entrada.

## Caza secundaria y C-001

- **Ausentes:** CPS/CPS-setup, SWE, washed/Washed IV, apex/variaciones, OP/pickup, responsive vs market-state-dependent, YO/WO/MO, momentum trade/trade models.
- **“Transfer of liquidity” y variantes:** no aparecen en 28:18. C-001 permanece cerrada como evolución; evidencia M2020 acumulada: S1 + S12–S15 (~6h22) sin el término.
- La única “transferencia” tratada es settlement/entrega entre contrapartes; no es el mecanismo temprano llamado `transfer of liquidity`.

## Integración

- `01_principios.md`: organización OTC/exchange, internalización, observabilidad y ejecución.
- `02_conceptos.md`: OTC/bilateral, exchange/multilateral, dealer/principal, CCP, MTF y ECN.
- `04_proceso.md`: filtro previo por venue y límites de lo observable.
- `91_contradicciones.md`: C-001 actualizada y C-002 para transparencia mostrada vs liquidez latente.
- `92_ideas_btc.md`: solo antecedente estructural; cualquier enlace con Hyperliquid queda como `[INFERENCIA]`.
