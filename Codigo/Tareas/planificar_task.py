#====================================================
# Módulo: planificar_task.py
# Tarea para el planificador con salida en markdown y
# nombre de archivo formateado con fecha actual.
#====================================================

from datetime import datetime
from crewai import Task
from Agentes.planificador import planificador

# Generar nombre dinámico del archivo de salida
fecha_hoy = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
nombre_archivo = f'plan_{fecha_hoy}.md'

planificar_tareas = Task(
    name='planificar_tareas',
    agent=planificador,
    description="""
        Crear un calendario académico semanal o multisemanal basado en el informe
        generado por el agente analista. Distribuir las tareas según su urgencia, peso,
        holguras y las horas disponibles del estudiante. Asegurar que la carga diaria
        sea equilibrada y sostenible, evitando sobrecargas y respetando todas las fechas ajustadas.

        Para cada tarea incluida en el calendario:
        - Asignar horas concretas por día.
        - Indicar márgenes y holguras.
        - Generar una breve recomendación práctica.
        - Incluir un consejo breve generado por el módulo buscador_consejos.

        Si es necesario para ordenar datos, calcular horas o generar tablas limpias en Markdown,
        puedes usar herramientas de ejecución de código.

        El calendario debe ser claro, estructurado y fácil de seguir.
    """,
    expected_output="""
        Un calendario académico en formato Markdown que incluya:

        - Distribución diaria de tareas.
        - Horas asignadas por día.
        - Indicaciones de holguras y márgenes.
        - Recomendaciones de estudio.
        - Un consejo breve por cada tarea.
        - Resumen final del plan.
    """,
    output_file=f'Planes/{nombre_archivo}'
)
