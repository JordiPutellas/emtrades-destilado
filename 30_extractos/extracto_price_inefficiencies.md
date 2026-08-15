# EMTrades — Documento Maestro (MUESTRA)
## Módulo: Price Inefficiencies (PIs) / Liquidity Gaps

> **Estado:** Prueba de concepto. Fuentes: 3 PDFs del módulo "Price Inefficiencies" + 2 PDFs de contexto ("Liquidity Principles", "Deeper Look into Price Swing Basics") + 4 capturas anotadas.
> **Convención:** [PDF] = extraído de texto de PDF. [IMG] = extraído de anotaciones en capturas de gráficos. [INFERENCIA] = interpretación mía a validar contigo.

---

## 1. Principios fundacionales (marco general del método)

Del documento "Liquidity Principles" — los 9 pilares sobre los que se construye todo [PDF]:

1. La volatilidad es una función de la liquidez disponible
2. El precio va hacia el lado más débil / menos líquido
3. El precio deja liquidez residual; la liquidez se transfiere a medida que el precio avanza
4. Una base de liquidez tiene 3 lados: techo, medio y suelo
5. Las bases de HTF (timeframes altos) acumulan más liquidez que las de LTF (liquidez = fricción)
6. El precio simplemente busca, encuentra y consume liquidez
7. Las extensiones se rellenan — cuanto más lejos viaja el precio de forma ineficiente, más débil se vuelve
8. Los price runs y swings son fractales: ocurren todo el día, a todas las escalas (de pocos pips a swings HTF de 1000+ pips)
9. La entrega eficiente de precio es muy fuerte... hasta que deja de serlo

---

## 2. Concepto central: la ineficiencia de precio (PI)

**Definición operativa** [PDF]: segmento de precio donde hubo un cambio extremo en el estado de liquidez y el precio se entregó en un "run" fino resultante de liquidez escasa en un lado del libro. Los términos *price inefficiency*, *gap* y *liquidity gap* se usan indistintamente.

**Mecanismo** [PDF]:
- Debilidad en un lado del mercado + algo de fuerza en el otro → el precio "sale corriendo" de forma ineficiente (dislocación).
- El movimiento fino deja un **vacío de liquidez** dentro del tramo.
- Cuanto más continúa el run ineficiente, mayor la probabilidad de que el precio vuelva a **rebalancear** hacia eficiencia en vez de seguir repricing agresivamente.
- Los liquidity providers despliegan mecanismos que agravan la dislocación; cuando el volumen que empuja el run se seca, el movimiento natural es "sangrar" de vuelta a través del vacío por agotamiento.
- Los micro-gaps existen siempre que un lado del libro entra más pesado, aunque solo son visibles en charts de 1-5 ticks.

**Contexto que favorece PIs** [PDF]: eventos/datos, sorpresas, central bank speak, geopolítica, fin de mes/día, horas de baja liquidez. Cada divisa del par tiene su propio perfil de liquidez y vulnerabilidad a formar PIs.

---

## 3. Anatomía visual: eficiente vs ineficiente

### Entrega INEFICIENTE — características [IMG: Inefficiency Schematic]
- El precio despega moviéndose de forma "fina" (thin)
- Falta de mechas al final de las velas; velas de extremos romos (blunt ended)
- El precio suele estirarse a medida que el run continúa
- A escala menor, el run va dejando bolsillos fractales de liquidez residual
- Esos bolsillos **no** se recogen como en precios eficientes → el precio queda "en deuda": tendrá que volver a tratar con esos compradores/vendedores residuales a la vuelta (por eso a menudo sangra hacia abajo tras un run ineficiente al alza)
- Matiz importante: no siempre sangra de vuelta — es más probable si la ida dejó bolsillos y la vuelta va sobre flujos naturales, no event-driven

### Entrega EFICIENTE — características [IMG: Efficient Price Delivery Schematic]
- El precio rellena continuamente las piernas ineficientes, rebalanceando el mercado
- Aspecto más "blocky", más lateral aunque tenga inclinación direccional
- Los runs tardan más en desarrollarse porque van rellenando constantemente
- El precio va recogiendo liquidez a medida que la pierna se desarrolla → **queda menos liquidez residual** cuando el precio se gira y vuelve a atravesar la zona
- La eficiencia es un **espectro**: de altamente ineficiente a altamente eficiente, con todo el rango intermedio. Hay que entrenar el ojo para diferenciar grados.

### Principio bisagra [PDF]: "Efficient price delivery is very strong until it isn't"
- Cuando el precio se mueve eficientemente es muy difícil pararlo: representa intención del mercado. No se pueden sostener fades contra la eficiencia.
- Pero tras el giro, queda poca liquidez en la zona entregada eficientemente (el precio ya consumió todos los niveles al desarrollarse).
- La entrega eficiente aparece en ciertas fases del swing (midflow, rangos, trapped liquidity), no siempre.

---

## 4. Implicaciones operativas (lo que se traduce a trading)

**Setups mencionados explícitamente:**
- **Fade de PI dentro de fractal** [IMG: GBPUSD 1min]: "El tipo de ineficiencias que nos gusta hacer fade y ponernos delante — fade altamente probabilístico. Short dentro del fractal, normalmente en un área core de liquidez." El precio es succionado de vuelta cuando los bids se secan y queda gap dentro de la pierna.
- **PIs relativos dentro de eficiencia** [PDF]: si aparecen ineficiencias dentro de un estado más amplio de eficiencia → oportunidades altamente asimétricas y unilaterales. (Señalado como uno de los mejores escenarios.)
- **Gaps & rebalances** [PDF]: calificado como "una de las mejores" conductas por consistencia.
- **Continuación por transferencia de liquidez** [PDF, Price Spike]: cuando el inventario/momentum sostiene y empuja transfiriendo liquidez → señal de intención presente; esperar que el precio se estire / golpee un void y "se abra". Patrón de continuación.

**Reglas de contexto (críticas):**
- **Escala relativa siempre** [PDF]: una PI de 1min no significa nada frente a un run de H4. La PI se evalúa relativa a su propio marco.
- **Ubicación y fase del swing** [PDF]: determinan si la PI se rellena de inmediato o más tarde. En zonas eficientes se rellenan rápido; el precio NO está obligado a rellenar de inmediato.
- **Timing de entrada** [PDF, Price Spike]: el precio suele dar solo una o dos buenas oportunidades de entrada aunque el estado de baja liquidez se prolongue (p.ej. en el low de un rango LLS para longs).
- **Gestión de posición** [IMG: GBPUSD 5min]: "el CÓMO se mueve el precio determina cómo gestionar el trade y las expectativas". Si el precio avanza de forma ineficiente hacia liquidez opuesta, habrá respuestas y rebalanceos de gap *independientemente* de la dirección final — hay que integrarlo en la gestión en vez de esperar línea recta al target.
- **Los fractales que rompen resistencia son los que aguantan al retorno** [PDF, Price Spike].

**Vocabulario propio detectado** (para glosario): PI, gap slip, shelf, shelf invalidation, apex / apex retest, fase parabólica, BA (¿base area? — por confirmar), CPS (¿core price swing? — por confirmar), LLS (Low Liquidity State), SWE (por confirmar), price run, price spike, midflow, HTF/LTF, residual levels, core area of liquidity, fractal pushing.

---

## 5. Preguntas abiertas / lagunas a resolver con más material

1. **BA, CPS, SWE** — siglas usadas sin definir en este módulo. Presumiblemente definidas en otros PDFs (Price Swing Basics, Process) o en los vídeos.
2. **Criterio de "tradeable vs non-tradeable PI"** — el material insiste en diferenciar, pero los criterios concretos parecen estar en los vídeos/ejemplos, no en el texto. Clave para sistematizar.
3. **"3 lados de una base de liquidez"** (principio 4) — mencionado pero no desarrollado en este módulo.
4. **Reglas de invalidación** — cuándo un fade de PI está mal y se corta. Solo hay pistas ("cannot hold fades against efficiency").
5. **Traslado a BTC/perps**: todo el material es FX spot (GBPUSD/EURUSD) con dealers y LPs bancarios. En BTC perps la microestructura difiere (funding, liquidaciones en cascada, liquidez fragmentada entre venues). La *lógica* (precio→lado fino, gaps→rebalance) es plausible que se conserve; las *huellas visuales* y los horarios de liquidez, no necesariamente. → A validar empíricamente, no asumir.

---

*Siguiente paso: procesar módulos "Price Swing Basics" y "Price Delivery" (definen CPS, price run, liquidity void, LLS) para completar la base conceptual antes de entrar en "Process" (que parece contener la ejecución: tracking unfilled liquidity, trade management).*
