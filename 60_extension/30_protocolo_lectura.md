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
