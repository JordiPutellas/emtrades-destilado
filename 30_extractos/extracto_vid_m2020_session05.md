# Extracto — M2020 Session 5: dislocación, ciclo operativo y selección de niveles

> Fuente primaria: `session 5-006.mp4` (02:19:30; pantalla fechada 1-oct-2020). Navegación: transcripción `.md/.srt/.json`. Revisados íntegramente transcripción/SRT, los 33 frames indexados y el vídeo en los pasajes visuales de charts, esquemas y trades. Las cifras, fechas y descripciones institucionales se conservan como claims de EM. Correcciones conservadoras de Whisper: buy/sell liquidity, GBPUSD, EBS, HFT, Deutsche Bank, Currenex, prime brokerage y `bearish deal flow`.

## 1. Event-driven: retirada de contraparte, no volumen necesariamente extraordinario

- EM abre con un sell-off GBPUSD de segundos tras una headline Brexit. Antes y al llegar nueva información, sistemas rápidos retiran quotes para evitar adverse selection; “**the liquidity just evaporates**”. El salto puede producirse con el mismo volumen ordinario si desaparece la limit liquidity que antes lo absorbía. [VID-M2020: Session 5 @ 00:00:01–00:05:18]
- La firma visual que propone observar es conjunta: tick frequency, distancia por tick/pip y volatilidad cambian de forma reconocible alrededor del evento. La atribución concreta de cada spike a una headline es a veces explícita y a veces supuesto de EM; no convertir los casos inciertos en hechos. [VID-M2020: Session 5 @ 00:05:29–00:06:30]
- El mismo mecanismo existe con menor intensidad fuera de noticias: al cruzar un threshold, quotes que parecían gruesas se retiran y el estado pasa de estabilidad bilateral a `midflow`, que aquí define provisionalmente como **one-sided liquidity**. El automatismo de LP/dealer evita quedar short contra una orden grande troceada. [VID-M2020: Session 5 @ 00:06:39–00:09:33]

## 2. Alcance de “the whole move is inefficient”

- La ineficiencia no es solo la vela más larga: si los sellers encuentran poca buy liquidity durante todo el recorrido, los fills quedan fragmentados/estirados y el **run entero**, a esa escala, puede ser thinly traded. `Low volume` significa poca transacción casada, aunque el sell market volume que intenta ejecutar sea intenso. [VID-M2020: Session 5 @ 00:10:33–00:12:26] [VID-M2020: Session 5 @ 00:15:35–00:16:19]
- Al secarse el flujo agresivo, la asimetría se invierte: buy liquidity gruesa frente a offers dispersos permite volver al rango con menos buying. EM pide expresamente intentar invalidar esta conclusión con observación propia. [VID-M2020: Session 5 @ 00:12:28–00:15:11]
- No significa que cada tick carezca de contraparte ni que cualquier movimiento direccional deba rellenarse inmediatamente. Es una comparación relativa entre la profundidad/transacción del origin y la del recorrido.

## 3. Solo lo nuevo del bloque institucional

- EM repite EBS/pre-trade credit, single book, information leakage y prime brokerage ya destilados. El matiz útil es el **contrato de fill** del dealer: (1) toma el lado contrario con su inventory/risk; (2) casa la market order con limit orders/client flow interno, incluso esperando el lado opuesto para capturar spread; o (3) cubre en otro dealer/venue y externaliza la información. Las dos primeras son internalización; la tercera externalización. [VID-M2020: Session 5 @ 00:44:50–00:51:48]
- Si externalizar repetidamente a un cliente mueve el mercado contra el dealer, puede clasificar su flow como aggressive/toxic y ampliar spread. Es explicación de EM sobre customer profiling, no regla universal ni señal observable por el retail. [VID-M2020: Session 5 @ 00:51:48–00:54:08]
- Counterparty risk importa en un mercado bilateral: si la contraparte quiebra, el cliente puede no cobrar. EM usa FXCM/SNB 2015 para explicar por qué los banks endurecieron prime brokerage; cifras, requisitos y causalidad quedan como relato de EM. [VID-M2020: Session 5 @ 00:30:42–00:32:25] [VID-M2020: Session 5 @ 00:55:14–00:59:39]
- La fragmentación genera dos interfaces: **single-dealer platform**, relación directa y disclosed con un bank; **multi-dealer platform**, tercero que agrega varios dealers, compite por best bid/offer y supervisa execution como “referee”. EM dice que la mayoría del flow no price-sensitive seguía prefiriendo relaciones single-dealer; no declara un ganador universal. [VID-M2020: Session 5 @ 01:14:29–01:21:36]
- Prime-of-prime/aggregator puede construir un private liquidity pool, elegir LPs y aportar pricing/trading/risk engines que deciden internalizar o externalizar automáticamente. Esto explica por qué un broker puede mostrar precios agregados sin que cada retail order llegue al interbank. [VID-M2020: Session 5 @ 01:06:28–01:14:04]
- `Wash trading` se usa de forma idiosincrática para una cascada donde algos se venden/compran entre sí, persiguen la poca liquidez y activan stops durante un flash crash. No es `washed inventory`, SWE ni una definición jurídica universal de wash trading. [VID-M2020: Session 5 @ 01:35:36–01:38:31]

## 4. Price-chasing en books internalizados

- Una orden cliente grande no se llena en un clip: el dealer la divide y la casa con inventory y sell limits internos. Tras el primer fill, sube el ask para buscar más contraparte sin asumir todo el short. [VID-M2020: Session 5 @ 01:42:44–01:47:47]
- El quote de ese dealer es información para los demás. Para no quedar desalineados y ser arbitrados, sus pricing engines actualizan también; si tenían sell limits internas en precios inferiores, pueden **internalizarlas/tomar el lado contrario** en vez de ofrecerlas, preservando el repricing común. Así la liquidez real existe, pero no llega al cliente en ese precio. [VID-M2020: Session 5 @ 01:47:48–01:55:46]
- EM llama ineficiencia a esa negación temporal de contraparte: menos liquidity disponible que la existente → el precio viaja más, aumenta volatilidad y el buy flow termina **persiguiendo** asks que se retiran/reprecian, en vez de ser la única causa que los empuja. [VID-M2020: Session 5 @ 01:55:46–01:59:38]
- El run termina cuando la orden se pausa/cancela por límites de ejecución, se completa por slices o alcanza sell liquidity suficiente; entonces sellers absorben el remanente, queda el recorrido fino y el precio puede dibujar de vuelta hacia la buy liquidity/origin. [VID-M2020: Session 5 @ 01:59:38–02:01:14]
- Límite: si la buy liquidity real acepta precios superiores y acompaña, el precio puede estabilizar arriba. El drawback no nace de la forma del chart sola, sino de que el deseo/liquidez real haya quedado atrás mientras los dealers estiraban el quote. [VID-M2020: Session 5 @ 02:01:14–02:03:12]

## 5. Un run HTF es una composición de ciclos, no un único impulso

- EM nombra la transición alrededor del extremo: **sideways/parabolic phase → apex → shelf flip → bearish deal flow → shift in the state of liquidity**. Después se repite en sentido contrario. El diagrama escrito confirma `deal flow`, que Whisper deforma como `filled flow`. [VID-M2020: Session 5 @ 02:06:03–02:06:42]
- Esto **no** es el template de cuatro variaciones de apex ni gestión dentro de apex. Es una narración causal general que conecta componentes ya existentes del price swing.
- Un micro-run puede ser una sola volume shot en decenas de segundos, con casi nada de opposite liquidity. Un move de 30–70 pips/H1 suele contener múltiples ciclos: **stability → surge/pop → dry-off/drawback → stability**, y cada pop activa brevemente el price-chasing/protection mechanism. [VID-M2020: Session 5 @ 02:06:46–02:10:53]
- Aun con muchos fills en el recorrido, el movimiento HTF sigue siendo relativamente thin frente a la mayor concentración del origin. Ineficiencia es un grado relativo, no un binario “trade/no trade”. [VID-M2020: Session 5 @ 02:10:53–02:11:27]

## 6. Selección de nivel y calidad del approach

- Tras el retorno, EM distingue **core/origin** —bulk de liquidez, bids/offers “reales”, mayor responsiveness— de middle/residual areas, menos favorables. Regla personal: “**I only trade at core areas**”, salvo que el movimiento sea HTF (por ejemplo H1), donde admite trades dentro del middle. [VID-M2020: Session 5 @ 02:13:12–02:13:54] [VID-M2020: Session 5 @ 02:17:26–02:17:49]
- El trade/live call que usa para ilustrarlo combina core validado con un approach fino cuyo ticking mostraba sellers débiles. Su síntesis: “**Level selection is 50% the equation**”; el trade fue “**a combination of a good level plus a weak move**”. Price movement es la otra mitad; nunca es solo level-based. [VID-M2020: Session 5 @ 02:13:54–02:15:18] [VID-M2020: Session 5 @ 02:19:00–02:19:25]
- Regla personal inequívoca: “**I am not allowed to take trade ahead of the level**”. La sesión anuncia para después cómo winners aparentemente buenos cambian sutilmente de probabilidad y cómo responder; no entrega todavía esa gestión. [VID-M2020: Session 5 @ 02:17:57–02:18:43]
- Variable Volume Flow queda anunciado para Session 6 como explicación de por qué el flujo no persiste y por qué un mercado líquido en el tiempo puede tener liquidez casi inexistente en un segundo. [VID-M2020: Session 5 @ 02:15:28–02:17:20]

## 7. Trades, setups y límites

- El supuesto trade de ~00:46 es una **oportunidad no tomada** por estar en la llamada: EM dibuja un stop de 2 pips y calcula 4R/8 pips después del movimiento; no es ejecución real y no crea TE. [VID-M2020: Session 5 @ 00:46:00–00:46:52]
- Menciona un long real con stop amplio y +13 pips flotantes, después lo vincula al regreso por el vacuum, pero no deja precio de entrada, invalidación exacta, gestión ni cierre inequívocos. El trade del core/high of day se resume como unos 4 pips sin contrato completo. **No crear TE**. [VID-M2020: Session 5 @ 01:05:13–01:05:59] [VID-M2020: Session 5 @ 02:13:01–02:14:25] [VID-M2020: Session 5 @ 02:17:57–02:18:10]
- No se crea setup ni se modifica S-01–S-09: `good level + weak move`, core-first y no anticipar son filtros de proceso; faltan invalidación y gestión específicas por modelo.
- La caza transversal solo encuentra `apex` como componente del ciclo general. CPS, SWE/washed, Washed IV/CPL, cuatro variaciones/gestión de apex, OP, responsive levels, YO/WO/MO, momentum trade, fractal pushing y HOTW no aparecen. El detalle se consolida al cerrar S6.
- `transfer of liquidity` no aparece. C-001 avanza a nueve sesiones M2020 (~13h04) sin el término. [VID-M2020: Session 5 — revisión completa 00:00:00–02:19:30]
- C-002 no se reabre: single/multi-dealer, internalización y fragmentación amplían el alcance ya compatible; no hay equivalencia explícita entre displayed book y total liquidity.

## 8. Integración

- `01_principios.md`: price-chasing en múltiples books y composición fractal del run.
- `02_conceptos.md`: price-chasing mechanism y single-/multi-dealer platforms.
- `04_proceso.md`: core-first, excepción HTF, no anticipar y `good level + weak move`.
- `90_preguntas_abiertas.md`: avance real de tradeable PI y timing/fill; el ciclo con apex no cierra el template.
- `91_contradicciones.md`: C-001 ampliada a nueve sesiones; C-002 sigue cerrada.
- `03_setups.md`, `05_trade_examples.md` y `92_ideas_btc.md`: sin cambios por ausencia de contrato completo, TE reconstruible o diferencia cross-asset nueva.
