# Registro de lecturas fechadas — método

> Capa de extensión. Autor: proyecto. Fecha de alta: 2026-08-16. Protocolo de referencia: `../30_protocolo_lectura.md`.

## Propósito

Producir la única evidencia que el proyecto no tiene: **lecturas trazadas ANTES del desenlace, cerradas y no editables**. Todo lo demás del repo (extractos, v1, el caso 01) es retrospectivo o está sesgado por selección — el corpus conserva los casos que funcionaron. Este registro distingue "el marco describe bien lo ocurrido" de "el marco anticipa dónde habrá fricción".

Cada lectura es evidencia bruta para la capa prospectiva (`../00_metodo.md`): un conjunto suficiente de lecturas evaluadas es lo que permitirá que alguna [HIPÓTESIS] ascienda a [EVIDENCIA] — o caiga a [REFUTADA]. Nada de este registro autoriza a operar con dinero real.

## Reglas duras

1. **El commit es el sello temporal.** La Parte A (lectura) se cierra y se commitea ANTES de conocer el desenlace. Sin commit anterior al desenlace, la lectura no vale.
2. **Una vez commiteada, la Parte A NO se edita.** Ni erratas, ni matices, ni "lo que quise decir". Las correcciones van en una ficha de revisión aparte (`*_rev01.md`), nunca sobre la original. El historial de git delata cualquier retoque.
3. **Se registra DÓNDE se espera fricción y de qué magnitud. NUNCA dirección ni timing.** Es la formulación de cabecera del protocolo: el mapa dice dónde habrá fricción SI el precio llega, y de qué magnitud dada la fuerza con la que llegue.
4. **Si el precio no llega a una zona, esa zona no cuenta ni a favor ni en contra: se marca NO EVALUABLE.** Una lectura entera puede resultar NO EVALUABLE; también es un dato (frecuencia de mapas que el precio no visita).
5. **Cada zona lleva la evidencia observable que la sostiene** (qué se ve en el chart, con fecha) — sin evidencia citable la fila está mal rellenada.
6. **Ninguna lectura se borra ni se selecciona.** Las lecturas malas se conservan igual que las [REFUTADA] (regla 4 de `../00_metodo.md`): sin el denominador completo, el registro es autoengaño.
7. **Las zonas donde NO se espera fricción son parte obligatoria de la lectura.** Son igual de falsables — y las sorpresas ahí (respuestas donde no se esperaba) son lo más valioso: los niveles que no supimos ver.

## Formato: dos partes, dos ficheros, dos commits

**Parte A — LECTURA (antes).** Fichero `lectura_AAAA-MM-DD_instrumento.md` (fecha = corte). Contiene: instrumento, TF, fecha/hora de corte, captura adjunta (`lectura_AAAA-MM-DD_instrumento_corte.png`, commiteada junto a la ficha), la ficha del protocolo (8 pasos), las zonas de fricción esperable ordenadas (cada una: rango de precio · evidencia · magnitud esperada grande/moderada/leve · confianza alta/media/baja), las zonas donde NO se espera fricción, incertidumbres declaradas y qué invalidaría la lectura. Se commitea al cerrarla — ese commit es el sello.

**Parte B — RESULTADO (después, mínimo 5 días tras el corte).** Fichero SEPARADO `lectura_AAAA-MM-DD_instrumento_resultado.md` (la Parte A queda byte a byte intacta). Contiene: qué zonas tocó el precio y qué hizo en cada una; el veredicto por zona (acierto / fallo / NO EVALUABLE); las sorpresas (respuestas donde no se esperaba fricción); y qué paso del protocolo falló, si falló. Su commit cierra la lectura.

### Criterios de evaluación de la Parte B

- **Acierto:** el precio llegó a la zona con la condición de llegada declarada y la respuesta observada es de la magnitud esperada (registrar la respuesta en cifras — pips/duración — además del calificativo).
- **Fallo:** el precio llegó y la respuesta contradice el mapa (atravesó sin respuesta una zona de fricción alta; respuesta grande en zona declarada sin fricción — esto último se registra ADEMÁS como sorpresa).
- **NO EVALUABLE:** el precio no llegó a la zona dentro de la ventana de evaluación.
- Si la llegada NO cumplió la condición declarada (p.ej. llegó eficiente donde el mapa condicionaba a llegada ineficiente), la zona se evalúa contra la rama condicional que sí aplicaba; si el mapa no contemplaba esa rama, es fallo de especificación → anotar el paso del protocolo responsable.
- **Ventana de evaluación:** de 5 días (mínimo, regla de esta infraestructura) hasta la fecha de la Parte B; declarar siempre la ventana usada. Zonas aún vivas tras la ventana quedan NO EVALUABLE en esta lectura (pueden reevaluarse en una lectura posterior con nuevo corte).

### Decisión pendiente

- **DP-5 · Umbrales de magnitud:** grande/moderada/leve no tienen definición cuantitativa (el corpus no la da — coherente con DP-2 del protocolo). Mientras esté pendiente: la magnitud se declara RELATIVA al TF del nivel, y la Parte B registra siempre la cifra observada junto al calificativo, para que los umbrales puedan definirse ex post sobre el registro acumulado sin reevaluar nada a mano.

## Flujo resumido

1. Copiar `lectura_TEMPLATE.md` → `lectura_AAAA-MM-DD_instrumento.md`; adjuntar captura del corte.
2. Ejecutar el protocolo (8 pasos), rellenar TODA la plantilla (nada en blanco; `INDETERMINADO` donde aplique).
3. Commit de la Parte A (sello). Añadir fila "abierta" en `00_registro.md` (mismo commit).
4. Esperar ≥5 días. Escribir la Parte B en su fichero separado, sin tocar la A.
5. Commit de la Parte B + actualizar la fila del registro a "evaluada" con resultado resumido.
