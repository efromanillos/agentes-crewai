
#Es conveniente pasar las tareas al analista formateadas a texto no como lista
#porque los LLM razonan mejor con texto natural no ejecutan lógicas sobre listas

def formatear_tareas(tareas):
    texto = ""
    for i, t in enumerate(tareas, 1):
        texto += f"""
Tarea {i}:
- Descripción: {t['descripcion']}
- Fecha inicio: {t['inicio']}
- Fecha entrega: {t['entrega']}
- Dificultad: {t['dificultad']}
"""
    return texto