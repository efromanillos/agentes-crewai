#=================================================
# Módulo crew.py: lanzar la crew de agentes y tareas
#=================================================

from crewai import Crew, Process
from Agentes.analista import analista
from Agentes.planificador import planificador
from Tareas.analizar_task import analizar_tareas
from Tareas.planificar_task import planificar_tareas
from config_llm import llm

import time


def launch_crew(bloque_formateado):
    # Crear la Crew
    crew = Crew(
        agents=[analista, planificador],
        tasks=[analizar_tareas, planificar_tareas],
        process=Process.sequential,
        verbose=True,
        inputs_from_tasks=True  # <- importante para que outputs de tareas previas sean usados como placeholders
        
    )

    

    # Lanzar la Crew con los inputs
    result = crew.kickoff(inputs=bloque_formateado)


    print("\nPlan generado correctamente en la carpeta 'Planes/'.\n")
    time.sleep(0.1) # para dejar que el panel de tracing termine de renderizar y se imprima debajo del menu principal
