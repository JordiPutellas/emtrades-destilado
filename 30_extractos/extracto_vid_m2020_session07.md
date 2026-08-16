# Extracto — M2020 Session 7: Variable Volume Flow, exhaustion y probabilidades dinámicas

> Fuente primaria: `Session 7.mov` (01:22:16; pantalla fechada 5-oct-2020). Navegación: transcripción `.md/.srt/.json`. Revisados íntegramente la transcripción/SRT, los 23 frames indexados y los pasajes audiovisuales críticos. Instrumento principal: GBPUSD, desde ticks/1min hasta mensual. Los ejemplos institucionales y porcentajes son afirmaciones pedagógicas de EM, no datos externos validados.

## 1. Variable Volume Flow: definición formal

- `Volume` conserva el significado fijado por EM: **market orders**. `Variable` significa que su intensidad cambia; `flow`, el flujo de esas órdenes: “**volume shot, volume dries off... Variable Volume Flow. Variable meaning it's changing up and down, volume meaning market orders, flow — the flow of market orders**”. [VID-M2020: Session 7 @ 00:47:17–00:47:36]
- Formulación compacta: “**the flow rises, the flow contracts... The volume isn't constant**”; no existe una presión uniforme durante toda una tendencia. [VID-M2020: Session 7 @ 00:39:56–00:40:26]
- Ciclo causal: estabilidad/dealing bilateral → pequeña debilidad en un lado + volume shot → retirada/repricing de liquidity → expansión fina → el volumen se seca y deja thinness → cualquier volumen contrario puede iniciar drawback/fill → nueva estabilización y nuevo ciclo. [VID-M2020: Session 7 @ 00:38:40–00:40:43]
- EM da a `large inefficient extension → exhaustion → extension fill` el “**specific name of that behavior**”. Es un **comportamiento/secuencia causal**, no un setup completo: no especifica todavía nivel elegible, trigger reproducible, hard stop ni gestión cerrada. [VID-M2020: Session 7 @ 00:40:47–00:41:12]
- En una tendencia alcista, la buy liquidity real puede sostener cada base mientras buy volume aparece, se seca y permite corrections; después vuelve a aparecer desde una base nueva. Por ello se puede estar equivocado sobre la dirección global y capturar correctamente respuestas locales de exhaustion. [VID-M2020: Session 7 @ 00:47:41–00:48:26]

## 2. Exhaustion = debilidad del impulsor, no fuerza contraria obligatoria

- El retorno no exige strong opposing liquidity. En el ejemplo numérico, la sell liquidity en cada escalón permanece constante; lo que cambia es que la orden compradora se va llenando (`9 → 7 → 5 → 3 → 1`) y deja casi ninguna buy liquidity acompañando el recorrido. El tramo cae por **thin buyers**, no necesariamente por strong sellers. [VID-M2020: Session 7 @ 00:43:06–00:44:48]
- Que se detenga market buying no mueve por sí solo el precio hacia abajo: “**just because the market order buying has stopped doesn't mean price is going to drop — now sellers have to come in**”. Una market sell sigue siendo necesaria; el book skew solo hace que poco volumen baste. [VID-M2020: Session 7 @ 00:44:04–00:44:16]
- En la práctica suele coincidir también con una zona más gruesa de sell liquidity, pero no es condición causal necesaria para el primer drawback. [VID-M2020: Session 7 @ 00:44:51–00:45:23]
- El retorno valida visualmente el origin: si al alcanzarlo el precio vuelve a estabilizarse, había buy liquidity real. Si no existiera, las siguientes sells atravesarían la zona y buscarían el nivel inferior. [VID-M2020: Session 7 @ 00:45:57–00:46:24]
- EM resume lo anterior como “**price simply finds liquidity; if price is moving, it's looking for liquidity**”. Se conserva como explicación de matching compatible con `price goes to the less liquid side`, no como teleología ni pronóstico autónomo. [VID-M2020: Session 7 @ 00:46:24–00:46:43]

## 3. Entrada en el punto de máximo skew

- EM localiza la mejor asimetría en el exhaustion/thinnest point: menor profundidad del lado del run frente a liquidity opuesta relativamente más gruesa. Lo llama “highest probability”. [VID-M2020: Session 7 @ 00:48:26–00:48:38]
- Uno o dos pips tarde todavía pueden dejar debilidad, pero la probabilidad de respuesta inmediata ya cae. En el punto exacto espera el menor drawdown y el mayor espacio para gestionar; una entrada tardía empieza más cerca del adverse move y reduce ese espacio. [VID-M2020: Session 7 @ 00:51:39–00:53:16]
- Esto permite capturar la respuesta local aun estando equivocado sobre la tendencia general. En bubble/event-driven states donde la liquidity acepta precios crecientes, EM admite como excepción operar con la fuerza en vez de fading. [VID-M2020: Session 7 @ 00:48:17–00:49:58]
- `Guaranteed`, `absolutely certain`, `99 to 1`, `80/20` y la certeza de 20 pérdidas seguidas son retórica pedagógica sin estudio, muestra ni calibración. No se convierten en probabilidades del playbook. [VID-M2020: Session 7 @ 00:50:24–00:56:49]

## 4. Respuesta inicial, winner/loser y gestión post-entry

- Una respuesta inicial favorable no equivale a winner: “**price will go your way; it doesn't mean you'll make money though**”. La probabilidad puede cambiar después y obligar a cortar. [VID-M2020: Session 7 @ 00:55:10–00:55:48]
- Para un long basado en thin sellers + thick buyers, la respuesta debería reflejarlo: sellers no deberían poder batir la buy liquidity y el volumen nuevo debería recorrer con facilidad la PI hacia origin. Si aparece weak buyers + strong sellers, la hipótesis se deteriora. [VID-M2020: Session 7 @ 00:57:09–00:58:49]
- La evaluación es lineal desde el primer pip: observar cómo se desarrolla cada segundo/candle y responder a incoming information, en vez de esperar únicamente el hard stop. [VID-M2020: Session 7 @ 00:58:35–00:59:40]
- Criterio concreto mostrado: si el precio atraviesa el área donde debía estar la buy liquidity, “**even one pip beneath... or one second... confirms to me that there is actually no buy liquidity there. I can respond and cut the trade well ahead of my stop loss**”. [VID-M2020: Session 7 @ 01:03:06–01:03:43]
- Alcance: es un criterio de **deterioro probabilístico** dependiente de la hipótesis de liquidez. No se especifica el hard stop, ni se afirma que todo poke de un pip invalide cualquier setup. Las características completas de winners/losers se prometen “at due time”; por tanto, **AVANCE, NO CIERRE**. [VID-M2020: Session 7 @ 00:58:04–00:58:19]
- EM separa dos problemas: outcomes distribuidos aleatoriamente y probabilities dinámicas por información nueva. Su countermeasure es trackear precio y reevaluar el estado de liquidez continuamente. [VID-M2020: Session 7 @ 00:59:42–01:01:34]

## 5. Escala, entornos e inventory

- VVF y microvolatility se repiten dentro de swings mayores: stability → shoot → dry → drawback puede ocurrir muchas veces dentro de un único movimiento HTF. [VID-M2020: Session 7 @ 01:04:55–01:06:06]
- En macro/event-driven volatility la presión persiste durante más tiempo, pero sigue siendo variable, no constante. La ineficiencia se juzga relativa al timeframe: un run mensual puede ser fino respecto a años de estabilidad aunque sea mucho más denso que uno de 1min. [VID-M2020: Session 7 @ 01:19:28–01:21:30]
- Incluso tras meses/años de recorrido, el middle permanece relativamente fino y el origin/core sigue siendo el área preferida. Tras high-volume impulse aparece low-volume state. [VID-M2020: Session 7 @ 01:20:59–01:22:08]
- Introducción terminológica para la siguiente sesión: el `last dealing range` puede clasificarse como **inventory**; cuando el run se aleja, vuelve a esa reserva, recarga y continúa hasta que el inventory deja de sostener. [VID-M2020: Session 7 @ 01:09:25–01:10:08]

## 6. Setups y trades

- `Large inefficient extension → exhaustion → extension fill` no es por sí solo setup: faltan selección formal del nivel, hard stop y gestión completa.
- Sí amplía el contrato de **S-02 Counter flow trading**: entrada preferida en first/exhaustion point; la precisión maximiza cushion y reduce drawdown; tras entrar se vigila si el lado de liquidity esperado sostiene y se puede cortar antes del stop si desaparece.
- Los charts son ejemplos explicativos, no trades reales con entrada, tamaño, stop y resolución asociados sin ambigüedad. No procede crear TE.

## 7. Caza transversal — Session 7

- **Avances:** tradeable PI (máximo skew + precisión de entrada + respuesta esperada); timing del fill (VVF: secado necesario, pero debe llegar volumen contrario); dynamic management.
- **Coincidencia visual sin reglas:** `WO` aparece como etiqueta horizontal en un chart, pero EM no la menciona ni explica su uso. No cierra la pregunta YO/WO/MO. [VID-M2020: Session 7 @ 00:39:39]
- **Ausentes:** CPS como setup; SWE/washed shelf-specific; parámetros Washed IV/CPL; cuatro apexes; gestión dentro de apex; poke del OP; responsive vs market-state-dependent como taxonomía; momentum trade; fractal pushing; HOTW; `transfer of liquidity`.
- `Inventory` aparece como dealing range/base que sostiene el run; no como `washed inventory` ni SWE.

## 8. Límites

- Los porcentajes y absolutos de EM no tienen calibración y pasan a validación, no al playbook.
- `Price finds liquidity` es shorthand explicativo; no asigna intención al precio.
- El criterio de un pip/segundo pertenece al ejemplo y a la zona previamente identificada; no se universaliza.
- Session 7 no entrega todavía una taxonomía completa de winners/losers ni un hard stop reproducible.
