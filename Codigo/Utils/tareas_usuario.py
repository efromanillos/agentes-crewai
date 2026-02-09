# Utils/tareas_usuario.py

from datetime import datetime

from datetime import datetime

def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje).strip()
        try:
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
            hoy = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

            if fecha < hoy:
                print('La fecha no puede ser anterior a hoy.\n')
                continue

            return fecha_str, fecha
        except ValueError:
            print('Formato incorrecto. Usa DD-MM-AAAA.\n')

def pedir_dificultad():
    while True:
        dificultad = input('Dificultad (baja / media / alta): ').strip().lower()
        if dificultad in ['baja', 'media', 'alta']:
            return dificultad
        print('Valor no válido. Escribe baja, media o alta.\n')

def pedir_horas():
    while True:
        horas = input('Horas disponibles al día: ').strip()
        try:
            horas_float = float(horas)
            if horas_float > 0:
                return horas
            else:
                print('Debe ser un número de horas mayor que 0.\n')
        except ValueError:
            print('Introduce un número de horas válido.\n')

def pedir_tareas():
    print('\nIntroduce tus tareas. Escribe \'fin\' en la descripción para terminar.\n')

    tareas = []
    cont_tareas = 0

    while True:
        descripcion = input('Descripción breve de la tarea: ').strip()
        if descripcion.lower() == 'fin':
            break

        fecha_inicio_str, fecha_inicio = pedir_fecha('Fecha de inicio (DD-MM-AAAA): ')
        fecha_fin_str, fecha_fin = pedir_fecha('Fecha de entrega (DD-MM-AAAA): ')

        # Validar que la fecha de fin sea posterior a la de inicio, puede ser el mismo día
        while fecha_fin < fecha_inicio:
            print('La fecha de entrega debe ser posterior a la fecha de inicio.\n')
            fecha_fin_str, fecha_fin = pedir_fecha('Fecha de entrega (DD-MM-AAAA): ')

        horas_dia = pedir_horas()
        dificultad = pedir_dificultad()

        tarea = {
            'descripcion': descripcion,
            'fecha_inicio': fecha_inicio_str,
            'fecha_fin': fecha_fin_str,
            'horas_dia': horas_dia,
            'dificultad': dificultad
        }

        tareas.append(tarea)
        cont_tareas += 1
        print(f'\nTarea {cont_tareas} añadida.\n')

    return tareas

# PARA PRUEBAS
if __name__ == '__main__':
    tareas = pedir_tareas()
    print(tareas)
