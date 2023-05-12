# Definimos la información de las habitaciones
HABITACIONES = {
    'sencilla': {'precio': 50, 'huespedes': 2, 'cantidad': 20},
    'doble': {'precio': 40, 'huespedes': 4, 'cantidad': 20},
    'suite': {'precio': 60, 'huespedes': 6, 'cantidad': 5}
}

def reservar_habitacion(tipo, noche, huespedes):

    precio = HABITACIONES[tipo]['precio'] * huespedes * noche
    # Disminuimos la cantidad de habitaciones disponibles

    return precio


from datetime import datetime

def noches(fecha_in,fecha_out):
    # Obtener la fecha de entrada y la fecha de salida del formulario
    fecha_entrada = datetime.strptime(fecha_in, '%Y-%m-%d')
    fecha_salida = datetime.strptime(fecha_out, '%Y-%m-%d')

    # Calcular la diferencia entre las fechas en días
    num_noches = (fecha_salida - fecha_entrada).days
    return num_noches