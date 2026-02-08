#==========================================================
#Módulo: analizar_tareas.py
#Tarea para el analista con salida en .md preparada
#para que el planificador pueda elaborar el plan de tareas
#==========================================================

from crewai import Task
from Agentes.analista import analista

analizar_tareas = Task(
    description=(
        'Analizar la lista de tareas académicas proporcionadas por el estudiante. '
        'Identificar fechas de entrega, pesos, urgencias y disponibilidad diaria. '
        'Calcular holguras adecuadas para cada tarea y ajustar las fechas internas '
        'para evitar riesgos de retraso. Especificar claramente cuánta holgura se '
        'ha asignado a cada tarea y justificarla cuando sea necesario. Elaborar un '
        'informe claro y estructurado que priorice las tareas y prepare la información '
        'necesaria para la planificación.'
    ),
    expected_output=(
        'Un informe académico detallado en formato Markdown que incluya: '
        '- Lista de tareas analizadas. '
        '- Fecha de entrega original de cada tarea. '
        '- Holgura asignada (en días) para cada tarea. '
        '- Fecha ajustada resultante. '
        '- Nivel de urgencia y prioridad. '
        '- Riesgos detectados y recomendaciones. '
        '- Resumen final listo para que el planificador genere el calendario.'
    ),
    agent=analista
)