# Utils/tareas_usuario.py

from datetime import datetime

# Contador global para ids incrementales
_siguiente_id = 1

#Función auxiliar para crear ids automáticamente
def _generar_id():
    global _siguiente_id
    id_actual = _siguiente_id
    _siguiente_id += 1
    return str(id_actual)

def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje).strip()
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
            hoy = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

            if fecha < hoy:
                print('La fecha no puede ser anterior a hoy.\n')
                continue

            return fecha_str
        except ValueError:
            print('Formato incorrecto. Usa DD/MM/AAAA.\n')

def pedir_dificultad():
    while True:
        dificultad = input('Dificultad (baja / media / alta): ').strip().lower()
        if dificultad in ['baja', 'media', 'alta']:
            return dificultad
        print('Valor no válido. Escribe baja, media o alta.\n')

def pedir_horas_bloque():
    while True:
        horas = input('Horas disponibles al día: ').strip()
        try:
            horas_float = float(horas)
            if horas_float > 0:
                return horas_float
            else:
                print('Debe ser un número de horas mayor que 0.\n')
        except ValueError:
            print('Introduce un número de horas válido.\n')

def pedir_tareas():
    print('\nIntroduce tus tareas. Escribe "fin" en la descripción para terminar.\n')

    tareas = []
    cont_tareas = 0

    while True:
        descripcion = input('Descripción breve de la tarea: ').strip()
        if descripcion.lower() == 'fin':
            break

        # Pedimos las fechas como string
        fecha_inicio_str = pedir_fecha('Fecha de inicio (DD/MM/AAAA): ')
        fecha_fin_str = pedir_fecha('Fecha de entrega (DD/MM/AAAA): ')

        # Convertimos a datetime SOLO para validar
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%d/%m/%Y')
        fecha_fin = datetime.strptime(fecha_fin_str, '%d/%m/%Y')

        # Validar que la fecha de fin sea posterior o igual a la de inicio
        while fecha_fin < fecha_inicio:
            print('La fecha de entrega debe ser igual o posterior a la fecha de inicio.\n')
            fecha_fin_str = pedir_fecha('Fecha de entrega (DD/MM/AAAA): ')
            fecha_fin = datetime.strptime(fecha_fin_str, '%d/%m/%Y')

        dificultad = pedir_dificultad()

        tarea = {
            'id': _generar_id(),
            'descripcion': descripcion,
            'fecha_inicio': fecha_inicio_str,
            'fecha_fin': fecha_fin_str,
            'dificultad': dificultad
        }

        tareas.append(tarea)
        cont_tareas += 1
        print(f'\nTarea {cont_tareas} añadida (id={tarea["id"]}).\n')

    return tareas

def pedir_bloque():
    nombre = input('Nombre del bloque de tareas (opcional): ').strip()
    tareas = pedir_tareas()
    if not tareas:
        print('No se han añadido tareas al bloque.\n')
        return None

    horas_diarias = pedir_horas_bloque()
    bloque_tareas = {
        #si usr le ha puesto nombre, el bloque tendrá esa descripción, si no, el bloque será: Bloque seguido de fecha y hora
        'nombre': nombre or f'Bloque {datetime.now().strftime("%d/%m/%Y_%H:%M:%S")}',
        'tareas': tareas,
        'horas_diarias': horas_diarias
    }
    return bloque_tareas



# PARA PRUEBAS
if __name__ == '__main__':
    bloques = []

    while True:
        bloque_tareas = pedir_bloque()
        if bloque_tareas:
            bloques.append(bloque_tareas)

        salir = input('¿Quieres introducir otro bloque? Escribe "salir" para parar: ').strip().lower()
        if salir == 'salir':
            break

    print(bloque_tareas)