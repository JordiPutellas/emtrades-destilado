# Protocolo de lectura ejecutable

> **Capa de extensión.** Convierte el catálogo de `20_motor_lectura.md` (34 observables, 26 reglas) en un procedimiento que produzca la MISMA lectura ante el mismo gráfico, la ejecute un humano o un agente. Si dos lectores divergen, el protocolo está mal especificado y se corrige el protocolo — no se improvisa. v1 no se toca.
>
> Autor: proyecto + [USUARIO]. Fecha: 2026-08-16.
>
> **Qué produce y qué no** — formulación de cabecera [USUARIO] (2026-08-16):
>
> "**La liquidez es inferible. Las market orders son aleatorias. El motor no dice si el precio irá ni cuándo — dice dónde habrá fricción SI llega, y de qué magnitud dada la fuerza con la que llegue.**"
>
> La salida del protocolo NO es una predicción de precio: es un **mapa de fricción esperable**. Es la misma partición que el corpus hace por su lado: la liquidez pasiva deja huella observable ("limit orders are friction... that is all you need to see where volume is building up" [DISCORD: Disc 60, 63]) mientras que el timing de las market orders es incognoscible por doctrina ("[when a market order hits] is entirely unpredictable... Outcome can be anticipated and what it will look like. But never when it will happen" [DISCORD: disc 11]).

---

## 1. Regla de trazado que el corpus no formula ([USUARIO])

**Registrada [USUARIO] 2026-08-16.** Enunciado de Jordi, en tres componentes:

1. **Nacimiento y proyección.** Los niveles nacen de las **acumulaciones grandes** — rangos amplios y prolongados donde se construyó posición. De sus bordes salen niveles que se **proyectan hacia adelante indefinidamente**. El precio se apoya en esas proyecciones meses o años después.
2. **Caducidad.** Los niveles NO caducan por tiempo, solo por ser **recogidos**. La cita de EM "liquidity doesn't sit there forever, it appears it disappears" se refiere a la LIQUIDEZ, no al nivel: el nivel es la **memoria de dónde hubo acumulación**, y la liquidez que acude a él se renueva.
3. **Jerarquía por origen.** El peso de un nivel es función del **tamaño y duración del rango del que nace**. Una acumulación de meses no es comparable a un pickup de 5 minutos. Es "HTF pulls more liquidity" expresado como regla de trazado.

### 1.1 Dónde encaja con el corpus

- **Caducidad por recogida, no por tiempo** — converge exactamente con S14: el nivel vigente ES solo la parte unpicked; desaparece cuando se recoge ("that original level's gone"), nunca por antigüedad. [VID-M2020: Session 14 @ 00:00:16–00:02:40] Horizontes largos avalados: "**some lows can take 6 months. Or highs. Gold bottomed out for like 4 years.**" [DISCORD: Disc 53]
- **Memoria de la acumulación** — converge con "liquidity turns up in the same places; price movement shows where there was little volume transacted" [DISCORD: Disc 24] y "the market preserves history of low volume nodes as levels" [DISCORD: disc 28].
- **Acumulación grande = construcción de posición** — converge con la definición de dealing ranges: "in which orders get filled / **big positions built** / volume builds up" [IMG-TWIT: Dealing Ranges] y con la liquidez lenta institucional construyendo posición en rangos sucesivos [IMG-MIET: Gold Ranges 5.1].
- **Renovación de la liquidez que acude al nivel** — tiene mecanismo en el corpus: la liquidez latente "only reveal[s]... **as price approaches levels — conversion rate**" [DISCORD: Disc 21, 64–65]. El nivel como coordenada donde la latente convierte es compatible con la distinción nivel/liquidez de Jordi.
- **Jerarquía por tamaño/duración del origen** — converge con "higher time frame pulls more liquidity" [VID-M2020: Session 13 @ 00:13:52–00:14:17] y su mecanismo ("the higher time frame trades over a longer period of time, more volume transacts, more interest is in it" [VID-M2020: Session 15 @ 00:07:01–00:10:57]), y con core (origen) > residual [R17].
- **Demostración práctica en el propio corpus** — TE-03: la daily buy base ~1.2725–1.2750, formada meses antes, respondió en marzo-2020 con ~450 pips [IMG-MIET: 1.0–1.4]. EM la operaba proyectada; nunca formuló la regla.

### 1.2 Dónde va más allá del corpus

- **La proyección indefinida como regla explícita**: el corpus la PRACTICA (charts "Levels" con niveles históricos [VID-M2020: Session 15 @ 00:56:22–00:57:45]; TE-03) pero nunca la enuncia. La formulación es de Jordi.
- **El peso como función de trazado** (peso = f(tamaño, duración del rango de origen)): el corpus tiene el principio (HTF pulls more) pero no lo convierte en regla de ranking al dibujar. La operacionalización es de Jordi.
- **La cita "liquidity doesn't sit there forever, it appears it disappears"**: [NO-LOCALIZADO] textual en el corpus conservado (búsqueda 2026-08-16 sobre extractos y maestros). Los enunciados más próximos: "Liquidity (passive & active) is not a constant" [PDF: The Price Run p.2] y la latente que aparece/desaparece con la conversión [DISCORD: Disc 64–65]. La exégesis (se refiere a la liquidez, no al nivel) es interpretación [USUARIO] razonable y CONSISTENTE con la separación del corpus entre nivel-como-parte-unpicked (S14) y liquidez-como-stock-que-se-drena (R4), pero no puede verificarse contra la cita original.

### 1.3 Tensiones con el corpus (se registran, no se resuelven)

- **T1 — Dispersión post-evento:** un nivel PUEDE morir sin ser recogido — "liquidity is dispersed post event/sentiment shift — **there's nothing in those pockets anymore**" [DISCORD: Disc 54]. Acota el componente 2: la caducidad por recogida es la norma, pero existe al menos un modo de muerte sin recogida.
- **T2 — Renovación no garantizada:** la liquidez que "acude" al nivel proyectado puede no comparecer — tras un poor high/low "**not necessarily, may or may not be there**" [DISCORD: Disc 73, 77].
- **T3 — Reposición sin regla:** el corpus documenta reposición del lado débil tras días ("weak side of book is replenished" [IMG-MIET: Tweet 4]) pero sin criterio de cuándo/cuánto (hueco ya registrado en 20_modelo_causal.md C6).

Las tres tensiones NO refutan la regla: la acotan. Y son coherentes con la formulación de cabecera — el mapa dice dónde habrá fricción **si llega y con qué magnitud dada la llegada**; nunca garantiza la respuesta.

---

## 2. El protocolo (8 pasos ejecutables)

Convenciones: las reglas R1–R26 y los observables Ob-01–Ob-34 son los de `20_motor_lectura.md`. Toda salida ambigua se marca `INDETERMINADO` y pasa a la sección Incertidumbres de la ficha — **nunca se resuelve improvisando**. Las decisiones que el corpus no resuelve están numeradas DP-1…DP-4 en §2.9 y se citan desde los pasos.

### P1 — Corte, instrumento y TF gobernante

- **ENTRADA:** instrumento; fecha/hora de corte (nada posterior al corte entra en la lectura); workspace de 4 charts con roles fijos — higher-higher TF (weekly) · HTF (H1/H4/D) · Levels (histórico de niveles) · Local PA (1–5min). [VID-M2020: Session 15 @ 00:56:22–00:57:45]
- **ACCIÓN:** declarar el corte. Identificar el **swing gobernante**: el run/swing con imbalance activo en el TF más alto cuya base de origen y extensión explican dónde está el precio hoy. Declarar TF gobernante y subordinados. "Higher time frame governs lower time frame"; cada swing se lee relativo a su propio TF. [VID-M2020: Session 13 @ 00:13:52–00:21:18]
- **SALIDA:** `{instrumento, corte, TF gobernante, swing gobernante (origen→extremo actual), TFs subordinados}`.
- **REGLAS APLICABLES:** paso 5 del orden de lectura del motor; R8, R25.
- **SI NO ESTÁ CLARO:** si dos TFs compiten con swings activos distintos, gobierna el MÁS ALTO ("HTF takes precedence" [VID-M2020: Session 13 @ 00:13:52–00:14:17]) y el conflicto se registra en Incertidumbres.

### P2 — Acumulaciones grandes → trazado y proyección

- **ENTRADA:** charts HTF y higher-higher desde el corte hacia atrás, SIN límite temporal fijo: hacia atrás hasta cubrir la última acumulación grande cuyo borde siga unpicked (regla [USUARIO] §1 — los niveles no caducan por tiempo).
- **ACCIÓN:** identificar rangos amplios y prolongados con dealing bilateral sostenido (acumulaciones grandes). Trazar niveles desde sus bordes; refinar el borde al release point cuando la escala lo permita [VID-M2020: Session 14 @ 00:03:03–00:05:05]; el shelf se dibuja ENTERO, sin refinar [VID-M2020: Session 14 @ 00:07:19]. Proyectar cada nivel hacia adelante indefinidamente [USUARIO §1]. Cada nivel es SOLO su parte unpicked [VID-M2020: Session 14 @ 00:00:16–00:02:40]. Todo trazado ANTES de mirar qué hizo el precio después (en lectura histórica: antes de mirar a la derecha del corte) [VID-M2020: Session 14 @ 00:34:05].
- **SALIDA:** lista de niveles `{banda de precio, TF de origen, rango de origen (fechas, duración, amplitud)}`.
- **REGLAS APLICABLES:** R1, R2; Ob-11, Ob-23; regla [USUARIO] §1.
- **SI NO ESTÁ CLARO:** si un rango no califica claramente como "acumulación grande", se INCLUYE con peso degradado y marca `INDETERMINADO` — mejor un nivel de más marcado como dudoso que un nivel de menos (el umbral mínimo de tamaño/duración es DP-1).

### P3 — Clasificación de cada nivel

- **ENTRADA:** lista de P2 + swing gobernante de P1.
- **ACCIÓN:** etiquetar cada nivel: **origen funcional** (core = base de origen de un run; residual = pocket a mitad de recorrido; shelf/inventory; BA; OP/feeder; apex — taxonomía S14: "categorizar siempre" [VID-M2020: Session 14 @ 00:13:53–00:15:36]) y **peso** = f(tamaño, duración del rango de origen) [USUARIO §1] + TF de origen ("HTF pulls more liquidity" [VID-M2020: Session 13 @ 00:16:40–00:17:06]). Peso en tres grados: alto / medio / bajo, con justificación escrita.
- **SALIDA:** tabla `{nivel, categoría, peso (justificado)}`.
- **REGLAS APLICABLES:** R17, R18; CL-19.
- **SI NO ESTÁ CLARO:** si el rol es doble (p.ej. residual del run gobernante PERO apex de un fractal — el caso TE-02: "technically residual of this H1 price run" pero fractal apex [VID-M2020: Session 13 @ 01:08:51–01:16:08]), registrar AMBAS etiquetas y clasificar por el TF del nivel, no por el del run ("view your price swings relative to the timeframe they're present on" [VID-M2020: Session 13 @ 00:17:41–00:21:18]). Si aun así es ambiguo → `INDETERMINADO`.

### P4 — Estado de cada nivel

- **ENTRADA:** tabla de P3 + historial de interacciones precio↔nivel desde la formación del nivel hasta el corte.
- **ACCIÓN:** asignar a cada nivel UNO de estos estados, con la evidencia observable que lo sostiene:
  - **intacto** — sin visita desde su formación (R1);
  - **parcialmente picked** — visitas que recogieron parte; se redibuja solo la parte viva (S14, R1);
  - **drenado** — tests repetidos/profundos con respuestas menguantes (R4, R10; Ob-12/13/16);
  - **washed** — top y bottom/middle picked (R3; Ob-17), o bottom alcanzado = consumo total (R7).
- **SALIDA:** tabla ampliada `{nivel, estado, evidencia (qué tests, cuándo, profundidad)}`.
- **REGLAS APLICABLES:** R3, R4, R6, R7, R10; Ob-12, Ob-13, Ob-16, Ob-17, Ob-18.
- **SI NO ESTÁ CLARO:** el corpus NO da umbral cuantitativo de drain (hueco C6 de 20_modelo_causal.md; DP-2) → usar solo el criterio funcional (cada feed empuja menos, R10). Evidencia mixta → estado `drenado-parcial (INDETERMINADO)`; nunca promediar hacia un estado limpio. Si desde la formación del nivel hubo un evento mayor (crash, banco central de calibre), añadir la marca `sujeto a dispersión (INDETERMINADO)` (R1-SALVO, [DISCORD: Disc 54]; el detector de dispersión es DP-3).

### P5 — Vacíos (tramos sin estructura)

- **ENTRADA:** charts + niveles trazados de P2.
- **ACCIÓN:** identificar los tramos ENTRE niveles donde el precio nunca se detuvo o que se entregaron rápido (runs finos, gap slips) y no se reconstruyeron después: ahí no hay fricción esperable (inverso de Ob-11: donde no hubo dealing no quedó memoria de liquidez; "what's usually left behind in the move lower is dispersed liquidity, or 'vacuum'" [DISCORD: Disc 7]). Registrar la extensión exacta de cada vacío y cómo se formó.
- **SALIDA:** lista de vacíos `{banda, cómo se formó (run fino/gap), ¿parcialmente rellenado después?}`.
- **REGLAS APLICABLES:** R19; Ob-06, Ob-11 (inverso); [PDF: Liquidity Void p.6].
- **SI NO ESTÁ CLARO:** si el tramo contiene estructura mínima (un pocket residual pequeño), registrarlo como `vacío con residual débil`: la respuesta esperable ahí es local y absorbible (R17), no fricción real.

### P6 — Las tres métricas permanentes

- **ENTRADA:** todo lo anterior + price action reciente (Local PA).
- **ACCIÓN:** leer y anotar las tres métricas de S13 [VID-M2020: Session 13 @ 00:56:47–00:57:33]:
  1. **Volatilidad** — ¿expansión o contracción relativa al período reciente? ("contraction = stable liquidity" [IMG-TWIT: Volatility 2]; Ob-29);
  2. **Estado de liquidez** — ¿qué lado tiene niveles vivos cerca y cuál está drenado/vacío? ¿el precio está en LLS? (R23);
  3. **Fase del swing gobernante** — localizar en la secuencia de estados (run / pausa / midflow / technical break / sideways / parabólica / apex / rebalance / LLS; R24–R25).
- **SALIDA:** tres valores con su evidencia observable.
- **REGLAS APLICABLES:** R22, R23, R24, R25; Ob-01, Ob-29–Ob-33.
- **SI NO ESTÁ CLARO:** la fase puede legítimamente diferir entre escalas (fractalidad): declarar fase POR TF relevante, no forzar una única. Si ni por TF se puede asignar → `fase INDETERMINADA` y el mapa final sale con esa advertencia en cabecera.

### P7 — Diagnóstico LIC

- **ENTRADA:** fase (P6) + carácter del movimiento en curso o del movimiento anticipado hacia el siguiente nivel (drift/spike, calidad de entrega).
- **ACCIÓN:** clasificar en el continuum [PDF: Liquidity Imbalance continuum p.1–2]: **exhaustion** (pierna débil secándose — el flujo natural contrario basta para el rebalance; R12) vs **presión genuina** (rompe y se estabiliza encima, o drift de metaorden; R13). Aplicar el veto del drift: si el movimiento drifta/worked its way through → etiqueta `no-fade` (R21, [DISCORD: Disc 47–51]). Si el fill esperado ocurre EN TENDENCIA → etiquetarlo trending extension fill, no reversal (R14).
- **SALIDA:** posición en el continuum + evidencia + etiquetas de veto si aplican.
- **REGLAS APLICABLES:** R12, R13, R14, R21; Ob-04.
- **SI NO ESTÁ CLARO:** el LIC es un espectro ("weakness is a spectrum, it's never binary" [IMG-TWIT: Washed iv wti]): declarar posición aproximada + qué observable falta para afinar. Si drift vs spike es indistinguible al corte → `INDETERMINADO — esperar más información` (doctrina bayesiana, §4 del motor). No emitir diagnóstico forzado.

### P8 — El mapa de fricción

- **ENTRADA:** salidas P2–P7.
- **ACCIÓN:** componer el mapa final:
  1. Para cada banda del entorno del precio: **fricción esperable = f(peso del nivel × estado)** — alta (core/acumulación grande intacta), media (parcialmente picked o peso medio), baja/nula (drenado, washed sin contexto R5, vacío).
  2. **Condicionar SIEMPRE cada respuesta a la llegada** (R20, R26): la magnitud esperada se enuncia "si el precio llega con entrega ineficiente/débil → respuesta grande; si llega eficiente → nivel probablemente atravesado tras dealing". Nunca respuesta incondicional.
  3. **Destino natural de una respuesta grande** = rebalance hacia el core/origen del run que la extensión completa ("respuesta en la core liquidity base" [IMG: The Price Run p.10]; cadena C3 de 20_modelo_causal.md).
  4. Ordenar las zonas por probabilidad de respuesta (peso × estado × llegada esperable).
  5. Declarar explícitamente qué NO dice el mapa: ni dirección, ni timing (formulación de cabecera).
- **SALIDA:** la ficha de lectura de §3.
- **REGLAS APLICABLES:** R5, R15, R16, R17, R18, R20, R26; formulación [USUARIO] de cabecera.
- **SI NO ESTÁ CLARO:** dos niveles con peso similar compitiendo → NO elegir: listar ambos y anotar qué evidencia futura los separaría — la conclusión se difiere a la respuesta del precio ("it's confirmed in how price responds off it", R11). La renovación de liquidez en niveles muy antiguos no está garantizada (T2 de §1.3; DP-4): los niveles de más de un ciclo macro llevan marca `renovación no verificable`.

### 2.9 — Decisiones pendientes (el corpus no las resuelve; NO improvisar)

| ID | Decisión pendiente | Dónde bloquea | Estado |
|---|---|---|---|
| DP-1 | Umbral mínimo (tamaño/duración) para que un rango cuente como "acumulación grande" | P2 | pendiente — conectar con H-xxx si se formaliza |
| DP-2 | Umbral cuantitativo de drain (cuántos tests / qué profundidad = drenado) | P4 | pendiente — hueco C6 del modelo causal |
| DP-3 | Detector operativo de dispersión post-evento (cuándo un nivel murió sin recogerse) | P4 | pendiente — T1 de §1.3 |
| DP-4 | Ponderación de la renovación en niveles muy antiguos (¿descuento por edad pese a la regla de no-caducidad?) | P8 | pendiente — T2 de §1.3; tensión directa con [USUARIO] §1.2 |

Mientras estén pendientes, el protocolo exige la salida marcada (`INDETERMINADO`, `sujeto a dispersión`, `renovación no verificable`) — la ambigüedad se PROPAGA a la ficha, no se tapa.

---

## 3. Formato de salida estandarizado (la ficha de lectura)

Toda ejecución del protocolo produce EXACTAMENTE esta ficha, en este orden. El test de calidad del protocolo es que un humano y un agente, ante el mismo gráfico y el mismo corte, rellenen fichas equivalentes; si divergen, se corrige el protocolo (nunca la ficha a posteriori). Las lecturas de casos se guardan en `60_extension/casos/`.

```markdown
# Lectura · {INSTRUMENTO} · corte {AAAA-MM-DD HH:MM UTC}

Ejecutor: {humano/agente + identificador} · Fecha de ejecución: {fecha}
Protocolo: 30_protocolo_lectura.md v{versión/commit}
Información usada: SOLO anterior al corte — fuentes listadas al pie.

## P1 · Marco
- TF gobernante: … · Swing gobernante: {origen → extremo, fechas}
- TFs subordinados: … · Conflictos de gobierno: {ninguno / detalle}

## P2–P4 · Tabla de niveles
| Banda | Origen (rango: fechas, duración, amplitud) | Categoría | Peso | Estado | Evidencia observable |
|---|---|---|---|---|---|
(un nivel por fila; INDETERMINADO donde aplique, nunca casilla vacía)

## P5 · Vacíos
| Banda | Cómo se formó | ¿Rellenado parcial posterior? |
|---|---|---|

## P6 · Tres métricas
- Volatilidad: {expansión/contracción} — evidencia: …
- Estado de liquidez: … — evidencia: …
- Fase del swing gobernante: … (por TF si difieren) — evidencia: …

## P7 · Diagnóstico LIC
- Posición en el continuum: {exhaustion ←→ presión genuina} — evidencia: …
- Vetos: {no-fade por drift / trending extension fill / ninguno}

## P8 · Mapa de fricción esperable
(ordenado por probabilidad de respuesta, de mayor a menor)
1. {banda} — fricción {alta/media/baja/nula} — respuesta esperable SI el precio
   llega {condición de llegada}: {magnitud/destino esperado} — por {peso×estado}
2. …
Destino natural de la respuesta mayor: {core/origen de referencia}

## Incertidumbres declaradas
- {todo INDETERMINADO propagado de P1–P7, con su paso de origen}
- {marcas: sujeto a dispersión / renovación no verificable / fase INDETERMINADA}

## Lo que invalidaría esta lectura
- {observaciones futuras concretas que obligarían a rehacer el mapa}

## Lo que esta lectura NO dice
Ni si el precio irá, ni cuándo. Mapa de fricción condicional a la llegada.

## Fuentes
- {charts/capturas usados, con fecha de cada uno}
```

Reglas del formato:
- **Ninguna casilla en blanco**: lo no determinable se escribe `INDETERMINADO` con el motivo — la ambigüedad se propaga, no se omite (§2.9).
- **Toda evidencia es observable y citable** (qué se ve en el chart, con fecha); nada de "se siente débil".
- **La sección "Lo que invalidaría esta lectura" es obligatoria**: una lectura sin condiciones de invalidación no es una lectura, es una opinión (misma regla que las fichas de hipótesis de `00_metodo.md`).
- La condición de llegada en P8 es parte de la respuesta esperada, no un adorno: sin ella la fila está mal rellenada (R20/R26).
