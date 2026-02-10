#====================================================
#Módulo: planificar_tareas.py
#Tarea para el planificador con salida en markdown y
#nombre de archivo formateado con fecha actual.
#====================================================

from datetime import datetime
from crewai import Task
from Agentes.planificador import planificador

# Generar nombre dinámico del archivo con fecha actual
# para dar formato al nombre del fichero de salida.
fecha_hoy = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
nombre_archivo = f'plan_{fecha_hoy}.md'

# El placeholder debe coincidir exactamente con el nombre de la Task anterior.
# CrewAI usará ese nombre para insertar automáticamente la salida de la tarea del analista
# como entrada a la tarea del planificador.

planificarTareas = Task(
    name='planificarTareas',
    description=(
        'Crear un calendario académico semanal o multisemanal basado en el informe '
        'generado por el analista {analizar_tareas}. Distribuir las tareas según su urgencia, peso, '
        'holguras y las horas disponibles del estudiante. Asegurar que la carga diaria '
        'sea equilibrada y sostenible, evitando sobrecargas y respetando todas las fechas '
        'ajustadas. El calendario debe ser claro, práctico y fácil de seguir. '
        'Además, para cada tarea incluida en el calendario, generar una frase breve '
        'de consejo práctico proporcionada por el módulo buscador_consejos. '
        'Si es necesario para ordenar datos, calcular horas o generar tablas limpias en Markdown, '
        'puedes usar herramientas de ejecución de código.'
    ),
    expected_output=(
        'Un calendario académico en formato Markdown que incluya: '
        '- Distribución diaria de tareas. '
        '- Horas asignadas por día. '
        '- Indicaciones de holguras y márgenes. '
        '- Recomendaciones de estudio. '
        '- Un consejo breve por cada tarea, generado por el módulo buscador_consejos. '
        '- Resumen final del plan.'
    ),
    output_file=f'Planes/{nombre_archivo}',
    agent=planificador
)

