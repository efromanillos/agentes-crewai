
#from Utils.entrada_usuario import bloque_tareas


#Es conveniente pasar las tareas al analista formateadas a texto no como lista
#porque los LLM razonan mejor con texto natural no ejecutan lógicas sobre listas

def formatear_tareas(tareas):
    texto = ""
    for i, t in enumerate(tareas, 1):
        texto += f"""
Tarea {i}:
- Descripción: {t['descripcion']}
- Fecha inicio: {t['fecha_inicio']}
- Fecha entrega: {t['fecha_fin']}
- Dificultad: {t['dificultad']}
"""
    return texto

# Formatear el bloque de prueba para enviar como inputs
def formatear_bloque(bloque_tareas):
    bloque_formateado = {
        "nombre": bloque_tareas["nombre"],
        "horas_diarias": bloque_tareas["horas_diarias"],
        "tareas": formatear_tareas(bloque_tareas["tareas"])
    }
    return bloque_formateado


