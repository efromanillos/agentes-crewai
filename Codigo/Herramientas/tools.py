# Herramientas/tools.py

from crewai_tools import CodeInterpreterTool, SerperDevTool

##Herramienta para que los agentes puedan realizar cálculos de tiempos,
# holguras, pesos y otras operaciones numéricas necesarias para el análisis y la planificación.
calculadora = CodeInterpreterTool()

# Herramienta para búsquedas web (Serper) usada 
# por el planificador para dar consejos de realización de las tareas
buscador_consejos = SerperDevTool()