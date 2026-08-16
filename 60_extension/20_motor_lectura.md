# El motor de lectura: de observable a estado de liquidez

> **Capa de extensión — material de trabajo, NO doctrina nueva.** Reúne la inferencia visual que el corpus tiene dispersa: cómo EM deducía el estado de la liquidez mirando SOLO gráficos de precio — sin tape, sin libro, sin volumen. Todo con cita; v1 no se toca; sin implementación ni traducción a cripto.
>
> **REGLA DE ORO del documento:** solo entra lo observable en un gráfico de precio. Lo que requiere libro/tape/volumen se anota en §1.9 como fuera del alcance de la lectura visual.
>
> Autor: proyecto (sesión 23 revisada). Fecha: 2026-08-16.
>
> Base doctrinal del motor: "**you don't need volume data to see what's going on — it's present in the price. Liquidity turns up in the same places; price movement shows where there was little volume transacted — it's observable**... with the right framework it's possible to see it in prices too." [DISCORD: Disc 24] Y el axioma que lo hace posible: "price is always reflecting state of liquidity and its never a constant" [DISCORD: Disc 6] — imbalance y exhaustion "dejan estructura, ritmo/tick rate y distancia observables" [VID-M2020: Session 3 @ 00:18:28–00:21:24].

---

## 1. Catálogo de observables

Formato: **cómo se ve · qué se infiere · fiabilidad declarada por EM** (fuerte / sugerente / ambigua — y si EM avisa de que puede engañar).

### 1.1 Tempo y entrega

**Ob-01 · Tick rate / tempo de impresión.** Se ve: frecuencia y continuidad con que imprimen los ticks — la parabólica hace "flash, flash, flash", es "crazy fast", frente a ticks espaciados/irregulares. NO es una forma de vela: "la vela agregada puede ocultar esta diferencia". [VID-M2020: Session 4 @ 00:00:00–00:01:31] Infiere: fase parabólica = último inventario drenándose agresivamente = máxima probabilidad de exhaustion [VID-M2020: Session 9 @ 01:17:48–01:20:25]. Fiabilidad: **fuerte** (definitoria de la fase) — con la advertencia explícita de que la silueta de la vela engaña.

**Ob-02 · Finura de la pierna (thin/skinny delivery).** Se ve: tramo entregado fino, sin dealing. Infiere: escasez de liquidez en un lado; ineficiencia. [PDF: Introduction Price Inefficiencies] Fiabilidad: **fuerte pero relativa** — dos correcciones del propio EM: (a) la ineficiencia es propiedad del MOVIMIENTO/ESTADO completo, "the whole move is inefficient, not just some 3 pip skinny leg from 143 hours ago" [IMG-MIET: InNeFFiciencY]; (b) puede haber volumen enorme y ser ineficiente — lo no-transaccionado en medio es la ineficiencia [DISCORD: Disc 55, 56]. No clasificar por vela grande aislada [VID-M2020: Session 6 @ 00:31:17–00:37:07].

**Ob-03 · Densidad de pockets residuales dentro de la pierna.** Se ve: cuántas y qué micro-acumulaciones deja el leg por dentro. Infiere: grado RELATIVO de ineficiencia — entre dos legs finas, la que deja menos/más débiles pockets residuales es más ineficiente. [VID-M2020: Session 6 @ 00:34:22–00:37:07] Fiabilidad: **fuerte** como comparador (es el criterio que EM da en vez del tamaño de vela).

**Ob-04 · Drift vs spike (el carácter del movimiento).** Se ve: el mismo desplazamiento puede ser "drifted more than spiked" — avance sostenido sin volatilidad — o un run/spike. [DISCORD: Disc 47–51] Infiere lecturas OPUESTAS: spike ineficiente → candidato a rebalance; drift persistente → metaorden/autocorrelación llenándose todo el día ("they've been filling one big fuckoff order all day... autocorrelation in flows is often one big order") → "**A move like this doesn't have to [fill]**" — es el movimiento con el que "people burn a 50% hole in their account". [DISCORD: Disc 47–51] El camino también actualiza la lectura aunque el destino sea el mismo: "drifted, worked its way through" vs "just ran ran ran"; y "congested" puede ser una lectura ERRÓNEA del nivel cuando el precio atraviesa una thin leg de forma drifty. [DISCORD: Disc 94.1] Fiabilidad: **fuerte como advertencia**; EM documenta explícitamente el error de lectura (faders diciendo "it's gonna fill" desde las 7am). ⚠️ Context-dependent por naturaleza.

**Ob-05 · Stair-step (extension–fill–new range).** Se ve: escalera de extensiones con fills cortos y rangos nuevos. Infiere: midflow/imbalance con inventario sosteniendo [PDF: Price Swings Continued p.7]; también compatible con execution algorithm en estilo neutral [VID-M2020: Session 6 @ 00:57:34–01:04:44]. Fiabilidad: **fuerte** como firma de midflow; ambigua respecto a la causa exacta (flujo vs algo).

**Ob-06 · Gap slip.** Se ve: el precio "gaps through on the way down" — atraviesa un tramo de golpe. [IMG: Price Swings Continued p.3] Infiere: vacío dejado por los bids retirados/consumidos (el canal del rebalance). Fiabilidad: el corpus lo usa como **etiqueta descriptiva** — ver §6 (observables sin inferencia articulada).

**Ob-07 · Ranges above ranges / dealing ranges apilados.** Se ve: rangos formándose cada uno por encima del anterior. Infiere: one-sided liquidity — "limit buys accepting higher prices alongside market buyers pushing, in a broadly weak area of offers" [IMG-TWIT: EMTRADES]; "seamless drift higher with ranges above ranges even on light volume" [IMG-TWIT: Emergency Cut]. Regla direccional: "until we form a dealing range ABOVE the previous one I'd be v v cautious holding longs" [IMG-TWIT: Dealing Ranges]. Fiabilidad: **fuerte** en contexto de catalizador; con el matiz de que la one-sided liquidity "often tapers off" [IMG-TWIT: EMTRADES].

**Ob-08 · Sideways → pop.** Se ve: lateral tras la primera ruptura, luego expulsión. Infiere: el sideways drena inventario y precede la parabólica — "after the sideways comes the pop"; "sideways pop into parabolic phase = often precedes highs". [VID-M2020: Session 13 @ 00:18:55–00:19:57] [IMG: Fractals _ Scaling p.8] Fiabilidad: **sugerente** ("often").

**Ob-09 · Presencia/ausencia de fase parabólica en un run largo.** Se ve: si el run ha tenido ya su tramo acelerado. Infiere: los runs largos "typically end in parabolic phase — haven't had that yet" → la AUSENCIA de parabólica se lee como run inacabado (usado en real para mantener). [IMG-MIET: GBP April] Fiabilidad: **sugerente** ("typically"); es una lectura por ausencia.

### 1.2 Interacción con niveles

**Ob-10 · Cómo LLEGA el precio al nivel (eficiente vs ineficiente).** Se ve: la calidad de la entrega en el tramo de aproximación. Infiere: probabilidad de respuesta — es el filtro central de selección: "eficiente hacia el nivel = no trade; ineficiente = interesante" [VID-M2020: Session 14 @ 00:16:29–00:17:07]; EM lo cuantifica como el "50%" de la decisión (nivel bueno Y movimiento débil hacia él) [VID-M2020: Session 5 @ 02:15:15–02:16:15]; calibración del PDF: ALTA probabilidad "price runs inefficiently into it extending past highs after a SWE", BAJA "price moves efficiently into a sell liquidity base" [PDF: Trade Example p.8]. Y es RELATIVO: "you can have a relatively weak level and an **even weaker move into it — generating response**" [DISCORD: Disc 6]. Fiabilidad: **fuerte** — posiblemente el observable más importante del método; hasta invierte la lectura de un área washed (ver Ob-17).

**Ob-11 · Dónde se detuvo el precio y dónde NO.** Se ve: el mapa histórico de respuestas. Infiere: dónde hay/hubo liquidez — "price holding in a base... it's because there's liquidity there — **it's the only thing holding price**" [DISCORD: Disc 13]; "liquidity turns up in the same places; price movement shows where there was little volume transacted" [DISCORD: Disc 24]; "the market preserves history of low volume nodes as levels — can find it on a lower tick timeframe" [DISCORD: disc 28]. Fiabilidad: **fuerte** (es la base del trazado de niveles).

**Ob-12 · Repetición de tests sobre la misma zona.** Se ve: el precio vuelve una y otra vez al mismo nivel. Infiere: drain — "The more we test the level, the weaker it gets — the liquidity is being drained (finite, quantitative)" [VID-M2020: Session 13 @ 01:03:29–01:05:24]; "grabbed it, grabbed it, grabbed it → falta de liquidez: you shouldn't really have any problems to get through" [VID-M2020: Session 14 @ 00:12:40, 00:27:27]. Fiabilidad: **fuerte** (formulada como mecánica finita).

**Ob-13 · Penetración profunda vs toque superficial.** Se ve: cuánto entra el precio en la base. Infiere: profundidad del consumo — deep tests drenan [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50]; regla extrema: si alcanza el **bottom**, TODA la liquidez de la base se da por consumida, solo queda la del último pickup (débil) [VID-M2020: Session 13 @ 01:03:29–01:05:24]. Fiabilidad: **fuerte**.

**Ob-14 · Poke más allá de un extremo.** Se ve: penetración sutil pasado un high/low u OP. Infiere — DOBLE LECTURA según de quién es el nivel: (a) poke del OP de MI trade → "shifts the probabilities significantly" (degradación del apex) [VID-M2020: Session 12 @ 00:30:17–00:32:26]; (b) poke past de un inventario CONTRARIO → drain deseable: "Goes deep into it, **better yet it pokes past it**" (debilita el área que después se quiere atravesar) [IMG: CLP/ED6JtkLXsAEu4X4.png]. Fiabilidad: **fuerte** en ambas direcciones. ⚠️ Mismo observable, lecturas opuestas por rol del nivel.

**Ob-15 · Clustering sobre el nivel vs salida rápida.** Se ve: el precio se sienta/acumula sobre el nivel, o sale disparado de él. Infiere: la liquidez esperada no está / sí está — "si price se sienta/clusterea sobre el nivel, cortar" [VID-PS: PriceSwing_08 @ 00:28:41–00:29:45]; "en counterflow, una salida rápida del nivel es favorable; `clustering and clustering` justifica cerrar" [VID-PS: PriceSwing_08 @ 00:25:10–00:26:24]. Fiabilidad: **fuerte** operativa (criterio de corte).

**Ob-16 · Respuesta menguante (cada feed empuja menos).** Se ve: cada rebote desde el inventario alcanza menos distancia o necesita penetrar más el base; los feeds fallan en alcanzar el core del fractal. Infiere: inventario perdiendo capacidad — "la debilidad existe antes de que el lower high/higher low la haga visible". [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50, 01:12:26–01:13:55] Fiabilidad: **fuerte** (es el diagnóstico funcional de drain).

**Ob-17 · Aspecto de una zona washed.** Se ve: top Y bottom/middle del shelf picked antes de la extensión (anatomía binaria dibujada, sin threshold cuantitativo) [VID-PS: PriceSwing_04 @ 00:05:05–00:05:45] [VID-PS: PriceSwing_08 @ 00:15:12–00:16:20]. Infiere: inventario de ambos lados consumido → probabilidad de respuesta "**low**" [VID-M2020: Session 14 @ 00:34:51]; única condición bajo la que EM espera paso directo sin dealing — "& even then expect some stalling & absorption" [IMG: Trade Example p.5]. Fiabilidad: **fuerte**, PERO con excepción contextual documentada: responde según CÓMO llega el precio ("broke midflow, broke shelf, sideways pop into it" responde más que "strong midflow becoming inefficient into it" — "They're both washed but the contextual environment is completely different") [VID-M2020: Session 14 @ 00:35:11–00:35:40]. ⚠️ Context-dependent por cita explícita.

**Ob-18 · Zona "drifty".** Se ve: área construida a la deriva, sin dealing compacto. Infiere: típicamente drained (picked muchas veces). [VID-M2020: Session 14 @ 00:16:09] Fiabilidad: **sugerente** ("typically").

**Ob-19 · Absorción (buildup que atraviesa).** Se ve: un core/base responde, pero el precio "pauses, accumulates, accumulates and pushes through it" — incapacidad de expulsar el precio + buildup hasta atravesar. [VID-PS: PriceSwing_03 @ 00:03:38–00:04:05] Infiere: el lado del nivel está siendo absorbido; deterioro de la hipótesis de hold (en trade example: "liquidez del shelf absorbida en el high" habilita compound en la otra dirección [IMG: Trade Example p.6]). Fiabilidad: **fuerte** como comportamiento; EM lo declara "observable, no trigger autónomo".

**Ob-20 · Fallo de rebotes en un supuesto low.** Se ve: los bounces fallan; los vendedores absorben a los compradores en la zona del low. Infiere: "failure of bounces, sellers absorbing buyers = **NOT characteristics of lows**" — no es un low real. [IMG: Trade Example p.7] Fiabilidad: **fuerte** (formulada como característica negativa).

**Ob-21 · Respuesta post-break del shelf.** Se ve: cómo responde el precio DESPUÉS de atravesar — "the weakness isn't necessarily confirmed once price has pushed through — **it's confirmed in how price responds off it**"; mejor señal: la primera pierna atraviesa el shelf de una vez (vs aguantar dentro). [VID-M2020: Session 12 @ 00:12:22–00:13:04] Infiere: si la ruptura fue de verdad (shelf muerto) o no. Fiabilidad: **fuerte** — y es una lectura DIFERIDA: prohíbe concluir en el momento del break.

**Ob-22 · Reentrada al shelf vs asomarse.** Se ve: si el precio vuelve a meterse materialmente en el shelf o solo lo asoma. Infiere: en midflow fuerte el precio apenas reentra; asomar/pasar el shelf = debilidad del momentum. [VID-M2020: Session 13 @ 00:06:30–00:06:53] Fiabilidad: **sugerente** ("señal sutil", palabra de EM).

**Ob-23 · Velas/punto de release.** Se ve: el precio se aquieta contra el borde de la base (bodies/volumen se apagan), construye y sale en skinny leg; el borde del nivel se refina al **release point** de la vela que salió. [VID-PS: PriceSwing_02 @ 00:01:20–00:02:57] [VID-M2020: Session 14 @ 00:03:03–00:05:05] Infiere: el punto exacto donde la base liberó el run (borde ejecutable del nivel refinado). Fiabilidad: **fuerte** (regla de trazado explícita).

### 1.3 Estructura y fase

**Ob-24 · Extremo "jumpy" vs limpio.** Se ve: top irregular, saltarín, en el final del run. Infiere: exhaustion — "agotamiento (top 'jumpy', bids exhausted)" [PDF: The Price Run p.5–p.10]; "arrival débil/jumpy/washed" como condición de selección [VID-PS: PriceSwing_06 @ 00:03:12–00:04:28]. Fiabilidad: **sugerente** — el adjetivo se usa sin anatomía definida (ver §6).

**Ob-25 · Reach limpio vs buildup/swipes en el apex.** Se ve: el precio "reaches" al nivel con delivery pronunciadamente débil, o llega con buildup, varios swipes y deeper tests. Infiere: la primera variante depende menos de la fuerza contraria (preferida por EM); la segunda "puede seguir siendo favorable, pero el inventory aún alimenta parcialmente y exige gestión más estrecha". [VID-M2020: Session 11 part 2 @ 00:25:44–00:29:33, 01:33:00–01:35:10] Fiabilidad: **sugerente/comparativa** — dos morfologías favorables con exigencias distintas. ⚠️ Context-dependent.

**Ob-26 · Technical break (primera ruptura del último base).** Se ve: el primer base contrario atraviesa el último base que creó un extremo. Infiere: primera evidencia de debilidad del momentum — puede justificar cortar a favor del midflow, "pero no obliga a reversal inmediato ni constituye por sí solo un trigger" [VID-M2020: Session 8 @ 01:25:00–01:25:53]. Statement asociado a validar: tras el primer break "it typically won't continue for a long while after" [VID-M2020: Session 13 @ 00:05:44–00:06:12]. Fiabilidad: **fuerte para debilidad, ambigua para reversal** — S9 lo acota: puede aparecer pronto y el precio continuar, puede no existir break limpio, y un break menor puede quedar contenido en el inventory HTF [VID-M2020: Session 9 @ 01:16:49–01:45:46]. ⚠️ Context-dependent por escala.

**Ob-27 · Higher low / lower high.** Se ve: estructura de extremos. Infiere: qué lado se debilita ("vendedores absorbidos en el nuevo pickup + higher low establecido ⇒ sell side débil" [IMG: Trade Example p.2]) — pero es un sensor TARDÍO: la debilidad existe antes de que el lower high/higher low la haga visible [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50]. Fiabilidad: **sugerente y rezagada** (declarado).

**Ob-28 · Poor high / poor low.** Se ve: extremo donde se facilitó poco trade — el precio llegó y no hubo dealing ("Not a lot of trade was facilitated down there basically. Offers dried up"). Infiere: exhaustion/unfinished business — "more times than not it'll trade through it", SIN garantía de liquidez fresca detrás. [DISCORD: Disc 73, 75–77] Fiabilidad: **sugerente** ("more times than not", con la doble negativa explícita).

### 1.4 Régimen y entorno

**Ob-29 · LLS (reconocimiento) y su duración.** Se ve: contracción con volumen bajo y estable, menor tick frequency; tras pickups, apexes, pausas de runs; por horario (fin de día, Asia, pre-datos). [PDF: Low Liquidity State p.1, p.9] [PDF: Variable Volume Flow p.4] Infiere: estado de máxima susceptibilidad a un run hacia CUALQUIER lado, incluso contra sentimiento [PDF: Low Liquidity State p.2, p.5]; cuanto más dura, mayor tiende a ser la salida [IMG: Low Liquidity State p.4]. Fiabilidad: **fuerte** como estado; **direccionales: ninguna** (explícito).

**Ob-30 · Runs, doesn't fill.** Se ve: las extensiones dejan de llenarse. Infiere: viraje de régimen HTF eficiente→ineficiente — "**runs, doesn't fill — that's your first sign**". [VID-M2020: Session 15 @ 01:00:00–01:06:07] Fiabilidad: **fuerte** ("first sign", con caso real de dos shorts fallidos gestionados por esa lectura).

**Ob-31 · Extensión bajo el rango de Asia + continuación de tendencia.** Se ve: el patrón nombrado. Infiere: "a very common characteristic of higher time frame inefficiency". [VID-M2020: Session 15 @ 01:00:00–01:06:07] Fiabilidad: **sugerente** ("very common").

**Ob-32 · Niveles que dejan de responder.** Se ve: niveles antes operativos son atropellados en serie ("you'll see them get rolled over"). Infiere: el estado del mercado cambió — los niveles SON el sensor de régimen: "when it's the time that it runs out, none of these levels are going to work". [VID-M2020: Session 15 @ 01:17:59–01:18:44] Fiabilidad: **fuerte** — y con la contracara epistémica: un nivel atravesado no refuta el trazado ("you're not wrong about anything — it just became inefficient" [VID-M2020: Session 14 @ 00:34:05]).

**Ob-33 · Tempo del midflow (pullbacks cortos vs profundos).** Se ve: profundidad y duración de las corrections. Infiere: midflow agresivo (liquidity persiguiendo precio → fills pequeños, contraflujo casi inviable) vs estable/eficiente (pullbacks profundos, ambas direcciones viables). [VID-M2020: Session 9 @ 00:36:57–00:38:36, 00:47:09–00:55:48] Fiabilidad: **fuerte** como clasificador de entorno; "no confundir una correction por VVF con fin del swing".

**Ob-34 · Hora del día / sesión.** Se ve: reloj (exógeno visible). Infiere: pondera probabilidad de invalidación ("my invalidation... was unlikely due to time of day (1900HRS BST)" [PDF: Trade Example p.5]), gestión (tarde = tomar beneficio; mañana = mantener/añadir [VID-M2020: Session 13 @ 01:18:27–01:19:07]) y dónde esperar LLS/runs. "STUDY the orderflow and price behaviour RELATIVE to the price swing stage & context & **time of day**." [IMG: Fractals _ Scaling p.11] Fiabilidad: **fuerte** como ponderador, nunca como señal autónoma.

### 1.9 Fuera del alcance de la lectura visual (mencionado en el corpus, EXCLUIDO del motor)

- **DOM/heatmap/order book**: EM afirma que el estado "podría verse en heatmap/order book, pero también inferirse mediante price action" [VID-M2020: Session 3 @ 00:18:28–00:21:24]; su única observación directa citada es el DOM de ES [IMG-TWIT: Bid Void].
- **Bookmap**: poco fiable incluso teniéndolo — "most liquidity is hidden — you can have seemingly no clear level even though someone's eating it" [DISCORD: Disc 60, 63].
- **Volume profile / footprint / delta**: "information is not a trading signal — requires judgement... valuable af, though its not needed, **can be seen in price**" [DISCORD: Disc 2]; "VP is just complicated version to describe simple trade matching" [DISCORD: Disc 77–78]; VP "takes a lot of fitting" [DISCORD: Disc 60].
- **Lectura de absorción por volumen** ("seeing heavy selling and no movement, you infer what's happening" [DISCORD: Disc 60, 63]) — la versión precio-only de la absorción es Ob-19.
- **Tape/orderflow inmediato**: el edge del orderflow trader "es solo inmediatez: with the right framework it's possible to see it in prices too" [DISCORD: Disc 24].

---

## 2. Reglas de inferencia

Formato: **SI** [observable(s)] → **ENTONCES** [estado] · **CON** [fuerza] · **SALVO** [invalidadores] · [fuente]. ⚠️ marca las context-dependent.

### Estado: liquidez sin recoger (unpicked)

- **R1** · SI un área de origen/base no ha sido revisitada (parte no recogida intacta) → ENTONCES unfilled/unpicked liquidity esperando ahí; el nivel vigente ES solo la parte unpicked ("that original level's gone" cuando se recoge). CON fuerte. SALVO dispersión post-evento: "**liquidity is dispersed post event/sentiment shift — there's nothing in those pockets anymore**" ⚠️. [VID-M2020: Session 14 @ 00:00:16–00:02:40] [DISCORD: Disc 54]
- **R2** · SI el precio se detuvo/respondió ahí repetidamente en el pasado → ENTONCES hay/hubo liquidez en ese precio ("liquidity turns up in the same places"). CON fuerte. SALVO drain acumulado (R4) y cambio de régimen (R22). [DISCORD: Disc 24] [DISCORD: Disc 13]

### Estado: nivel washed / drained

- **R3** · SI top y bottom/middle de un shelf picked antes de la extensión → ENTONCES shelf washed (inventario de ambos lados consumido). CON fuerte (anatomía binaria, sin threshold). [VID-PS: PriceSwing_04 @ 00:05:05–00:05:45] [VID-PS: PriceSwing_08 @ 00:15:12–00:16:20]
- **R4** · SI tests repetidos + penetraciones crecientes + respuestas menguantes → ENTONCES área drained. CON fuerte. [VID-M2020: Session 13 @ 01:03:29–01:05:24] [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50]
- **R5** · SI área washed/drained → ENTONCES respuesta improbable ("low"). CON fuerte. **SALVO el modo de llegada** ⚠️ — el mismo washed responde si el precio llega tras "broke midflow, broke shelf, sideways pop into it", y no si llega por "strong midflow becoming inefficient into it": "They're both washed but the contextual environment is completely different". [VID-M2020: Session 14 @ 00:34:51–00:35:40]
- **R6** · SI zona de aspecto drifty → ENTONCES típicamente drained. CON sugerente ("typically"). [VID-M2020: Session 14 @ 00:16:09]
- **R7** · SI el precio alcanzó el bottom de la base → ENTONCES toda su liquidez consumida; solo queda el último pickup (débil). CON fuerte. [VID-M2020: Session 13 @ 01:03:29–01:05:24]

### Estado: inventario que sostiene / inventario roto

- **R8** · SI las bases a favor del movimiento sostienen y el precio apenas reentra al shelf → ENTONCES inventario sostiene, midflow activo ("the inventory that's pushing price holds"). CON fuerte. SALVO conflictos de escala (un flip fractal es inconsecuente contra el midflow H1) ⚠️. [VID-M2020: Session 13 @ 00:05:44–00:06:53] [VID-M2020: Session 13 @ 00:13:13–00:15:07]
- **R9** · SI primera ruptura del último base que creó extremo (technical break) → ENTONCES primera debilidad del momentum. CON fuerte PARA DEBILIDAD, ambigua para reversal ⚠️ — "no obliga a reversal inmediato ni constituye trigger"; puede ser temprano, faltar, o quedar contenido en el fractal mayor. [VID-M2020: Session 8 @ 01:25:00–01:25:53] [VID-M2020: Session 9 @ 01:16:49–01:45:46]
- **R10** · SI cada feed del inventario empuja menos / falla en alcanzar el core del fractal → ENTONCES inventario perdiendo capacidad ANTES de que la estructura lo muestre. CON fuerte. [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50, 01:12:26–01:13:55]
- **R11** · SI tras el break la primera pierna atraviesa el shelf de una vez → ENTONCES shelf muerto, continuación probable; SI aguanta dentro → ruptura no confirmada. CON fuerte — la conclusión se DIFIERE a la respuesta, no al break ⚠️. [VID-M2020: Session 12 @ 00:12:22–00:13:04]

### Estado: exhaustion vs presión genuina (el LIC)

- **R12** · SI extensión ineficiente + secado del tick rate + extremo jumpy tras void → ENTONCES extremo exhaustion del continuum: el estado natural del flujo contrario basta para rebalancear; el trade es fill de pierna débil, NO de tendencia. CON fuerte (diagnóstico obligatorio pre-trade). [PDF: Liquidity Imbalance continuum p.1–2] [PDF: The Price Run p.5–p.10]
- **R13** · SI shift completado (apex + shelf flip) y el precio rompe y SE ESTABILIZA encima → ENTONCES presión genuina/convicción (el otro extremo del LIC). CON fuerte. [PDF: Liquidity Imbalance continuum p.1] [VID-M2020: Session 13 @ 00:58:02–00:58:36]
- **R14** · SI el fill ocurre EN TENDENCIA → ENTONCES trending extension fill: rebalance para encontrar contrapartida, no reversal ("no reversal, just rebalance to find sellers"). CON fuerte. ⚠️ Mismo observable (fill) con lectura opuesta según régimen. [IMG: Liquidity Void p.15] [PDF: p.16]

### Estado: one-sided liquidity

- **R15** · SI ranges above ranges / dealing ranges apilados + drift sostenido que no llena → ENTONCES one-sided liquidity (limits aceptando peores precios con el otro lado abierto). CON fuerte en contexto de catalizador. SALVO taper: "it often tapers off" ⚠️. [IMG-TWIT: EMTRADES] [IMG-TWIT: Emergency Cut] [DISCORD: Disc 66]

### Estado: balanced liquidity

- **R16** · SI dealing bilateral estable, respuestas en ambos extremos, sin desplazamiento neto → ENTONCES balanced/equilibrium (distribución similar de ambos lados); el trend trading ahí produce chop. CON sugerente — nota del proyecto: el corpus infiere el balance en parte DEL chop que predice (riesgo de circularidad ya señalado en 20_modelo_causal.md §3.2 CL-33). [DISCORD: Disc 85–88] [VID-M2020: Session 3 @ 00:33:09–00:35:46]

### Estado: residual vs core

- **R17** · SI el nivel es el ORIGEN del run (la base de la que salió) → core: máxima respuesta esperada al retorno; SI es pocket dejado en mitad del recorrido → residual: respuesta débil, absorbible en midflow. CON fuerte (es la taxonomía base). [IMG: Price Swings Continued p.3] [PDF: p.7] [VID-M2020: Session 8 @ 01:00:24–01:04:55]
- **R18** · SI el primer break de midflow golpea un nivel → ENTONCES típicamente es residual, no área fuerte — pondera reversal vs continuación; y el TIPO de nivel que creó el extremo pondera si el high/low aguanta (residual → no esperar hold; core → mayor probabilidad). CON sugerente ("typically"). [VID-M2020: Session 13 @ 01:26:45–01:29:49]

### Estado: entrega eficiente vs ineficiente

- **R19** · SI la pierna es fina Y deja pocos/débiles pockets residuales → ENTONCES entrega ineficiente (relativa a su escala); la densidad residual es el comparador, no el tamaño de vela. CON fuerte. SALVO juzgar micro-legs aisladas: la ineficiencia es del movimiento/estado completo ⚠️. [VID-M2020: Session 6 @ 00:31:17–00:37:07] [IMG-MIET: InNeFFiciencY]
- **R20** · SI llegada eficiente a un nivel → no trade (respuesta improbable); SI llegada ineficiente/extendida a good/core → candidata a respuesta "manageable". CON fuerte (el "50%" de la selección). SALVO que el nivel esté washed sin el contexto de R5. [VID-M2020: Session 14 @ 00:16:29–00:17:07] [VID-M2020: Session 5 @ 02:15:15–02:16:15] [PDF: Trade Example p.8]
- **R21** · SI el movimiento drifta ("worked its way through") en vez de correr → ENTONCES posible metaorden/autocorrelación: NO tratar como spike fadeable; puede no llenar. CON fuerte como veto. ⚠️ Lectura opuesta al spike (R12). [DISCORD: Disc 47–51] [DISCORD: Disc 94.1]

### Estado: fase del swing

- **R22** · SI niveles antes operativos dejan de responder en serie → ENTONCES cambio de régimen/estado ("none of these levels are going to work and you'll see them get rolled over"); SI además "runs, doesn't fill" → viraje HTF a ineficiente ("that's your first sign"). CON fuerte. [VID-M2020: Session 15 @ 01:17:59–01:18:44, 01:00:00–01:06:07]
- **R23** · SI contracción estable de volumen/ticks tras pickup/apex/pausa → ENTONCES LLS: susceptibilidad máxima a run hacia cualquier lado; duración ∝ tamaño esperado de la salida; NINGUNA lectura direccional. CON fuerte (estado), nula (dirección). [PDF: Low Liquidity State p.1–p.9] [IMG: p.4]
- **R24** · SI sideways tras primer break → ENTONCES pop/parabólica probable (drenaje del inventario restante); SI tick rate "flash flash flash" → parabólica en curso = último inventario drenándose = zona de máxima probabilidad de exhaustion; la parabólica "typically" no es pierna de significancia — reversal/shift después. CON sugerente→fuerte encadenada. [VID-M2020: Session 13 @ 00:18:55–00:19:57, 01:23:47–01:24:00] [VID-M2020: Session 4 @ 00:00:00–00:01:31] [VID-M2020: Session 9 @ 01:17:48–01:20:25]
- **R25** · SI el precio localiza en la secuencia CPS (base→PoR→skinny→pause→continuation→apex→retests→gap slip→CBP→PoR→base) → ENTONCES fase del swing identificada; el CPS es "a representation of HOW price moves rather than why" — mapa de navegación, no predicción. CON fuerte como localizador. [PDF: Price Swings Continued p.2] [IMG: Tracking Unfilled Liquidity p.4]

### Meta-regla documentada (transversal)

- **R26** · La respuesta esperada es SIEMPRE función relativa: fuerza del nivel × debilidad de la llegada — "you can have a relatively weak level and an even weaker move into it — generating response until liquidity absorbs the response and continues". Ninguna regla anterior se aplica en absoluto, todas en relativo. [DISCORD: Disc 6]

**Los casos context-dependent (los importantes):** R1 (pockets vaciados post-evento), R5 (washed responde según llegada), R8 (escala), R9 (break ≠ reversal), R11 (conclusión diferida a la respuesta), R14 (fill en tendencia ≠ fill en exhaustion), R15 (taper), R19 (micro-leg vs estado), R21 (drift invierte la lectura del spike) — más Ob-14 (poke con doble lectura por rol del nivel) y Ob-25 (dos morfologías de apex favorables con gestión distinta). **11 casos documentados donde el mismo observable admite lecturas distintas según contexto.**

---

## 3. Orden de lectura (el procedimiento reconstruido)

Secuencia reconstruida de S14/S15/S13 + PS10; los pasos son de EM, el ordinal exacto es reconstrucción [INFERENCIA] salvo donde la fuente lo dicta.

**Paso 0 — Filtro estructural (una vez):** saber qué mercado/feed se observa — FX OTC quote-driven, fragmentado, con internalización: un quote no es una limit firme, y el precio observado son quotes agregadas, no un libro. Condiciona qué significa todo lo demás. [VID-M2020: Session 1 @ 00:02:38–00:05:34, 00:10:01–00:12:17]

**Paso 1 — Workspace fijo de 4 charts:** **Higher-higher TF** (weekly, separado para que sus cajas no ensucien el H1) · **HTF** (H1/H4/D) · **Levels** (chart dedicado a identificar/refinar niveles históricos) · **Local PA** (tracking del día, 1–5min). [VID-M2020: Session 15 @ 00:56:22–00:57:45]

**Paso 2 — Rutina diaria de sincronización:** cada mañana, trackear y dibujar niveles ("get back in my groove"); el exercising no termina nunca — "second level information is easy to get out of touch with". [VID-M2020: Session 15 @ 00:54:31–00:55:59] [VID-M2020: Session 13 @ 01:53:22–01:59:57]

**Paso 3 — Trazado y refinado de niveles (procedimiento S14, en este orden):**
1. Identificar el área en 15min.
2. Zoom: "numerous levels inside of the level" → redibujar cada subnivel a su liquidez real → repetir en 5min → separar todos (aunque disten 4 pips) → ajustar el borde al release point de la vela que salió. Si no se ve, bajar hasta tick charts. (Un área de 15min queda típicamente en 2 niveles.)
3. El shelf se dibuja ENTERO, sin refinar.
4. Categorizar SIEMPRE cada nivel (OP top side ≠ shifting point ≠ residual ≠ apex retest; small vs big shelf; BA; washed o no).
5. **Dibujar antes, no después**: todo trazado antes de que el precio llegue.
[VID-M2020: Session 14 @ 00:00:16–00:05:05, 00:07:19, 00:13:53–00:15:36, 00:34:05]

**Paso 4 — Las tres métricas permanentes** (vigilancia continua, no puntual): **volatilidad · estado de liquidez · fase del price swing**. [VID-M2020: Session 13 @ 00:56:47–00:57:33]

**Paso 5 — Clasificar el TF gobernante ANTES de leer el inferior:** "higher time frame governs lower time frame"; clasificar el midflow/swing gobernante (¿qué base creó el último extremo? ¿sostienen las bases a favor? ¿tempo agresivo o estable?) antes de operar dirección en el LTF. Un shelf LTF no influye en el TF superior ("if it's a H1 price run, you need a H1 shelf flip"), pero los flips fractales SON la herramienta para operar fills de extensiones. Ver cada swing relativo a su timeframe y, a la vez, saber en qué fase del swing mayor vive el menor. [VID-M2020: Session 13 @ 00:13:13–00:21:18] [VID-M2020: Session 8 @ 01:05:30–01:10:45]

**Paso 6 — Bajar de escala solo como zoom:** el LTF/tick es "microscope" para timing, selección, avoidance y strength dentro de la fase HTF — identificar el nivel en la escala que lo gobierna y bajar SOLO hasta ver su anatomía; EM usa 1min/tick para temporizar exhaustion pero "no opera el 1min". [VID-M2020: Session 6 @ 00:31:17–00:37:07] [VID-M2020: Session 11 part 2 @ 01:19:40–01:23:01]

**Paso 7 — Diagnóstico LIC previo a todo trade:** ¿en qué extremo del continuum está el movimiento — exhaustion/rebalance o presión con convicción? Determina target y gestión. [PDF: Liquidity Imbalance continuum p.2]

**Paso 8 — Selección por llegada:** de ~50 niveles dibujables se operan 1-2; el filtro es CÓMO llega el precio (R20), con la regla del 50% (nivel Y movimiento). Sin touch del nivel no hay trade ("I am not allowed to take a trade ahead of the level"); si el precio no llega, no perseguir ("when price misses your level, don't chase — often it will end up spiking to it later"). [VID-M2020: Session 14 @ 00:16:29–00:17:07] [VID-M2020: Session 5 @ 02:12:51–02:13:34] [VID-M2020: Session 15 @ 00:55:12–00:55:30]
- Ponderar SIEMPRE con hora del día y event risk ("CONTEXT MATTERS, ALWAYS"). [IMG: Fractals _ Scaling p.11] [PDF: Trade Example]

**Paso 9 — Post-entry, lectura lineal desde el primer pip:** la respuesta se lee en secuencia (¿sostiene el lado del trade? ¿fallan los rebotes contrarios? ¿stair-step?); actualización bayesiana continua con más peso a incoming information que al forecast; seguimiento del espectro favourable/unfavourable escalando al fractal. [VID-M2020: Session 7 @ 00:55:10–00:59:40] [VID-M2020: Session 11 part 2 @ 01:14:18–01:19:40] [IMG: Fractals _ Scaling p.12]

**Cómo se adquiere el motor (meta-procedimiento):** primero localizar swings y marcar TODOS los features relacionándolos con principios; solo después escoger UN comportamiento y ejercitarlo (sample sets de 10/día; first touch y retest por separado; incluir también no-trades y ejemplos que contradicen la hipótesis). [VID-PS: PriceSwing_09 @ 00:10:33–00:12:48] [VID-PS: PriceSwing_10 @ 00:25:19–00:28:54] [VID-M2020: Session 10 @ 00:52:01–00:57:10] [PDF: Process Over Profits p.5]

---

## 4. Ambigüedad declarada

El propio corpus prohíbe que el motor concluya siempre:

- **Ningún observable aislado significa nada:** "the features are definable... but theres a whole spectrum of things that happen at highs and lows. **Any single aspect of it on its own is kinda irrelevant** — so its better for you to observe it yourself." [DISCORD: Disc 25.1]
- **La instantánea no es el desarrollo:** una foto del estado "solo describe ese microsegundo... quotes pueden retirarse, reaparecer o repricing"; la práctica es seguir cada cambio y actualizar, no congelar el imbalance en certeza. [VID-M2020: Session 3 @ 00:16:26–00:18:16, 00:21:39–00:24:01]
- **Doctrina bayesiana explícita:** "You can certainly anticipate things but **Bayesian observation is more important**. You need to observe incoming info. Relentlessly." [DISCORD: Disc 49] Countermeasures to randomness: track very closely · considerar múltiples outcomes · probabilístico, nunca expectativas rígidas. [VID-M2020: Session 15 @ 00:17:40–00:23:28]
- **Conclusiones diferidas por diseño:** la debilidad del shelf no se confirma en el break sino en la respuesta posterior (R11); el technical break puede ser temprano, faltar o quedar contenido (R9); "midflow is an EXPECTATION" — si no aparece, reevaluar, no insistir. [VID-M2020: Session 12 @ 00:12:22–00:13:04] [VID-M2020: Session 9 @ 01:16:49–01:45:46] [PDF: Price Swings Continued p.7]
- **Los espectros nunca son binarios:** "Weakness (or strength) is a spectrum, it's never binary." [IMG-TWIT: Washed iv wti] Las bases tienen variaciones visuales que exigen exposición: "you need to test every single type many times over". [VID-M2020: Session 14 @ 00:22:01–00:22:58]
- **Etiquetas < tempo:** `range` y `bearish trend` pueden describir el mismo tramo según escala y ocultan CÓMO se entrega; clasificar por entrega, no por dirección. [VID-M2020: Session 3 @ 00:33:09–00:37:50] Trend/range es taxonomía insuficiente: hay trends ineficientes y eficientes que se operan al revés. [VID-M2020: Session 13 @ 00:23:56–00:25:47]
- **Los absolutos del profesor no son estadísticas:** `guaranteed`, `99 to 1`, `80/20` son retórica pedagógica no calibrada. [VID-M2020: Session 7 @ 00:50:24–00:56:49]
- **Incluso el setup completo puede fallar:** con todos los parámetros presentes la probabilidad puede cambiar durante el desarrollo por incoming information; dos o tres fallos próximos tampoco refutan la relación. [VID-M2020: Session 2 @ 00:07:04–00:13:15, 00:18:38–00:21:13]
- **Anti-narrativa como higiene del motor:** ante una respuesta, "no need to infer a reason why it happened — its the what conditions/combination of events led to that"; "avoid finding causal and specific reasons... markets too random and complex. Hence why observing it against a prism of governing principles." [DISCORD: Disc 5.1] [DISCORD: Disc 13]

---

## 5. Lo que la lectura NO puede dar

Invisible en el gráfico, reconocido por el corpus:

- **El timing, nunca:** "Outcome can be anticipated and what it will look like. **But never when it will happen.**" [DISCORD: disc 11] "But WHEN they will diverge is random." [DISCORD: Disc 44]
- **La debilidad antes de que arranque:** existe antes de ser visible (Ob-16/Ob-27 son sensores rezagados), y "la debilidad a menudo solo se hace evidente cuando el movimiento arranca" — de ahí la primacía de la observación sobre la anticipación. [VID-M2020: Session 11 part 2 @ 00:30:37–00:33:50] [DISCORD: Disc 49]
- **La liquidez latente:** "most liquidity is hidden — you can have seemingly no clear level even though someone's eating it"; solo se conoce al convertirse, y su conversion rate varía. [DISCORD: Disc 60, 63] [DISCORD: Disc 64–65]
- **El estado de la parent order:** ninguna señal visual cerrada dice si el execution algorithm terminó — mientras siga activo, la extensión puede no llenar; el estilo se infiere de la morfología pero sin umbral ni señal de finalización. [VID-M2020: Session 6 @ 01:20:26–01:22:55]
- **El quién y el porqué:** "Trying to predict why someone lifted the offer is futile"; "i dont care why theyre selling — could simply be a huge order being filled over time." [DISCORD: Disc 42–45] [DISCORD: Disc 5.1]
- **La dirección después de la respuesta:** `response ≠ hold ≠ reversal` — la lectura da la respuesta local, no lo que sigue; "I shouldn't go into the territory of forecasting". [VID-M2020: Session 8 @ 00:56:19–00:57:19] [VID-M2020: Session 14 @ 00:29:44, 00:33:53]
- **El sub-segundo:** "efficiently inefficient" — los HFTs ven el precio verdadero antes; "by the time the breakout is seen on our screen the volatility is finished". [VID-M2020: Session 13 @ 02:06:35–02:07:39]
- **El skew máximo en vivo:** la asimetría de profundidad "dura muy poco y no es fácil de identificar en vivo". [VID-M2020: Session 2 @ 01:01:24–01:03:09]
- **La magnitud de una sorpresa:** el juicio "significance of the catalyst on available liquidity" que separa fade de chase no tiene criterio observable especificado. [IMG-TWIT: Emergency Cut] [PDF: Liquidity Void p.11]
- **La falsación del trazado:** un nivel atravesado no dice que el trazado fuera erróneo — "you're not wrong about anything — it just became inefficient" — lo que hace al motor difícil de refutar trade a trade (nota del proyecto: esto conecta con la crítica de falsabilidad de 20_modelo_causal.md §3.3). [VID-M2020: Session 14 @ 00:34:05]

---

## 6. Observables SIN inferencia clara asociada (registro para el cierre)

Aparecen en el corpus como observables pero sin regla de lectura articulada:

1. **Gap slip** — etiqueta descriptiva sobre charts; la inferencia (vacío detrás) es implícita/definicional, nunca formulada como regla de uso. [IMG: Price Swings Continued p.3]
2. **"Jumpy"** — adjetivo usado para extremos y llegadas ([PDF: The Price Run p.5–p.10], [VID-PS: PriceSwing_06]) sin anatomía visual definida en ninguna fuente.
3. **YO / WO / MO (aperturas)** — dibujadas como niveles de referencia en las anticipaciones, sin regla operativa; [USUARIO] confirma que eran descriptivos, sin prioridad sobre shelf/CPS. [IMG-MIET: Prediction 1, 2] [02_conceptos]
4. **HOTW (High Of The Week)** — mismo caso. [PDF: Tracking Unfilled Liquidity p.3]
5. **SR / SR flip** — reconocido como caja distinta del shelf con justificación "Reasoning — my eyes": sin criterio. [DISCORD: Disc 25.1]
6. **"Breakdown characteristics"** — invocadas como condición de entrada del fade PS04 y NUNCA definidas (caso inverso: inferencia que apela a un observable no especificado). [VID-PS: PriceSwing_04 @ 00:20:19–00:21:09]
7. **Las 4 variaciones principales de apex** — template anunciado ("there's 4 main variations") y no localizado en el corpus; solo 2 morfologías comparadas en S11.2. [VID-M2020: Session 13 @ 01:45:10–01:45:27] (pregunta 4 de 90_preguntas_abiertas)
8. **Low volume nodes en tick charts** — mención única ("the market preserves history of low volume nodes as levels") sin regla de uso ni jerarquía frente a los niveles del método. [DISCORD: disc 28]

---

## Resumen estructural

- **34 observables** catalogados (9 de tempo/entrega · 14 de interacción con niveles · 5 de estructura/fase · 6 de régimen/entorno), más 5 fuentes de información EXCLUIDAS por la regla de oro (DOM/heatmap, bookmap, VP/footprint/delta, absorción por volumen, tape).
- **26 reglas de inferencia** (R1–R26) cubriendo los 10 estados pedidos: unpicked (R1–R2), washed/drained (R3–R7), inventario sostiene/roto (R8–R11), LIC (R12–R14), one-sided (R15), balanced (R16), residual vs core (R17–R18), eficiente/ineficiente (R19–R21), fase del swing (R22–R25), más la meta-regla relativa (R26).
- **11 casos context-dependent documentados** donde el mismo observable admite lecturas distintas u opuestas — los críticos: washed que responde según llegada (R5), drift que invierte la lectura del spike (R21), fill en tendencia vs en exhaustion (R14), poke con doble lectura según rol del nivel (Ob-14), break que es debilidad pero no reversal (R9), conclusión del shelf diferida a la respuesta (R11).
- **8 observables sin inferencia clara** (§6) — de ellos, "breakdown characteristics" y las 4 variaciones de apex son promesas de la fuente nunca cumplidas; el resto son etiquetas descriptivas o menciones únicas.
- El motor es explícitamente **no-concluyente por diseño** (§4) y tiene **10 límites declarados** de lo que el gráfico no puede dar (§5) — el primero de todos: el timing, nunca.
