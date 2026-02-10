# menu.py
from Utils.entrada_usuario_simple import pedir_bloque
from crew import launch_crew  # launch_crew debe aceptar el bloque como argumento
import os

def menu_simple():
    os.system('cls')
    bloque = None

    while True:
        print('\n--- MENÚ ---')
        print('1. Introducir tareas (crear un bloque)')
        print('2. Generar plan (enviar bloque al analista/planificador)')
        print('3. Salir')

        opcion = input('Elige una opción (1/2/3): ').strip()

        match opcion:
            case '1':
                bloque = pedir_bloque()
                if bloque:
                    print(f'Bloque creado: {bloque["nombre"]} con {len(bloque["tareas"])} tareas.\n')

            case '2':
                if not bloque:
                    print('No hay bloque. Crea uno primero con la opción 1.\n')
                    continue
                try:
                    launch_crew(bloque)
                except Exception as e:
                    print('No se pudo lanzar Crew:', e)

            case '3':
                print('Saliendo.')
                break

            case _:
                print('Opción no válida.\n')

if __name__ == '__main__':
    menu_simple()