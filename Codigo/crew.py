#=================================================
# Módulo crew.py: lanzar la crew de agentes y tareas
#=================================================

import json
from crewai import Crew, Process
from Agentes.analista import analista
from Agentes.planificador import planificador
from Tareas.analizar_tareas import analizarTareas
from Tareas.planificar_tareas import planificarTareas
from config_llm import llm

def launch_crew(bloque_tareas):
    # Convertimos el diccionario en texto legible para el LLM
    bloque_texto = json.dumps(bloque_tareas, indent=2, ensure_ascii=False)

    crew = Crew(
        agents=[analista, planificador],
        tasks=[analizarTareas, planificarTareas],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={'bloque': bloque_texto})
    print("\nPlan generado correctamente en la carpeta 'Planes/'.\n")