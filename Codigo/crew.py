#=================================================
# Módulo crew.py: lanzar la crew de agentes y tareas
#=================================================

from crewai import Crew, Process
from Agentes.analista import analista
from Agentes.planificador import planificador
from Tareas.analizar_task import analizar_tareas
from Tareas.planificar_task import planificar_tareas
from config_llm import llm
from Utils.formatear import formatear_tareas
from entradas_prueba import bloque_prueba


# Formatear el bloque de prueba para enviar como inputs
bloque_formateado = {
    "nombre": bloque_prueba["nombre"],
    "horas_diarias": bloque_prueba["horas_diarias"],
    "tareas": formatear_tareas(bloque_prueba["tareas"])
}


def launch_crew(bloque_formateado):
    # Crear la Crew
    crew = Crew(
        agents=[analista, planificador],
        tasks=[analizar_tareas, planificar_tareas],
        process=Process.sequential,
        verbose=True,
        inputs_from_tasks=True  # <- clave para que outputs de tareas previas sean usados como placeholders
    )

    # Mostrar los nombres de las tasks
    print("Tasks en Crew:", [task.name for task in crew.tasks])

    # Lanzar la Crew con los inputs
    result = crew.kickoff(inputs=bloque_formateado)

    # Debug: mostrar qué se ha recibido en cada task
    if "analizar_tareas" in result:
        print("\n[DEBUG] Output de analizar_tareas:\n")
        print(result["analizar_tareas"])
    else:
        print("\n[DEBUG] No se encontró la salida de analizar_tareas.")

    # El resultado final de toda la crew
    print("\n[DEBUG] Resultado completo de la Crew:\n", result)

    print("\nPlan generado correctamente en la carpeta 'Planes/'.\n")
