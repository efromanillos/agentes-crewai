# Actividad 05 – CrewAI

Proyecto de la asignatura **Programación de IA** 
Planificador Inteligente de Tareas. 
Versión: v1.0‑beta

Este repositorio contiene el desarrollo de una *Crew* de agentes inteligentes utilizando la librería **CrewAI**, orientada a la planificación académica personalizada. El sistema permite analizar un bloque de tareas, generar un informe detallado y construir un calendario de estudio equilibrado y realista.

---

## Cómo ejecutar el programa

Es importante ejecutar el programa **desde la raíz del proyecto**, no desde dentro de la carpeta `codigo/`.

#### Ejecución correcta (recomendada)

Desde la raíz del repositorio:

python codigo/main.py

Funcionalidades principales
---------------------------

#### Análisis automático de tareas

El agente analista:

•     Calcula holguras entre fechas.
•     Evalúa urgencia, dificultad y peso de cada tarea.
•     Detecta riesgos y propone recomendaciones.
•     Genera un informe estructurado que sirve como entrada para el planificador.

#### Planificación académica inteligente

El agente planificador:

•     Distribuye las tareas en un calendario semanal o multisemanal.
•     Ajusta horas por día según disponibilidad del estudiante.
•     Respeta fechas límite y holguras.
•     Añade recomendaciones prácticas y consejos obtenidos mediante búsqueda web.
•     Genera un archivo final en formato Markdown dentro de la carpeta .

#### Menú interactivo

El usuario puede:
•     Introducir tareas.
•     Ejecutar la Crew.
•     Salir del programa.

NOTA: el archivo de salida con los Planes se alamacena en la carpeta Planes tras ejecutar la Crew desde el directorio raíz
