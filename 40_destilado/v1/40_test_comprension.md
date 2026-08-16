# v1 · Test ciego de comprensión

> Diez preguntas cuya respuesta completa está contenida en los ficheros de v1 (sin acceso al corpus original). SIN RESPUESTAS por diseño: sirven para comprobar más adelante si v1 es utilizable por otro agente/lector de forma autónoma. Cobertura: ontología (1-3), máquina de estados (4-6), microestructura (7), setups (8-9), claims (10).

1. **[Ontología]** ¿Cuáles son los tres niveles internos de una core liquidity base según S12, y cuál es la regla que valida un Original Pickup como tal?

2. **[Ontología]** ¿En qué se diferencia el trazado de un shelf del trazado de un nivel, y por qué esa diferencia importa para el drain?

3. **[Ontología]** Ante dos niveles candidatos —el original al que el precio alimentó y un pickup posterior— ¿cuál prevalece según EM, cómo se llama cada uno, y qué es una "bay of liquidity"?

4. **[Estados]** Describe la secuencia completa desde el primer break de midflow hasta el apex, incluyendo qué hace el sideways, qué viene después de él, y qué variante existe cuando no hay break limpio.

5. **[Estados]** ¿Dónde se confirma la debilidad de un shelf —en la ruptura o en otro sitio— y cuál es la mejor señal de que el shelf estaba realmente débil?

6. **[Estados]** ¿Qué es exactamente el technical break, qué cambia cuando aparece, y qué NO autoriza por sí solo? ¿Qué combinación espera EM para el fade completo de midflow?

7. **[Microestructura]** ¿Por qué la capa de microestructura de v1 es explícitamente descriptiva y no fuente de reglas operativas? ¿Cuál es el "único absoluto" operativo que EM reconoce, y qué es el conversion rate de la liquidez latente?

8. **[Setups]** Enumera los "three main components" de S-08, sus tres variantes de activación reconciliadas, y el único sub-hueco que impide considerarlo completamente cerrado.

9. **[Setups]** ¿Es S-09 (fade de Washed IV/CPL) direccionalmente bajista por naturaleza? Justifica con las dos capturas espejo, y explica por qué sus campos vacíos están marcados RETENIDO POR LA FUENTE y qué implica eso para la fase 2.

10. **[Claims]** Cita los dos claims que la propia fuente designa como tarea de validación ("EM pide test: SÍ"), qué habría que medir en cada uno, y qué claim de v1 está marcado NO VALIDADO por procedencia dudosa (y de quién podría proceder).
