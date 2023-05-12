habitaciones_disponibles = {
    'sencillas': list(range(1, 21)),
    'dobles': list(range(21, 41)),
    'suites': list(range(41, 46))
}


def asignar_habitacion(tipo_habitacion):
    if tipo_habitacion == 'sencilla':
        if habitaciones_disponibles['sencillas']:
            habitacion = habitaciones_disponibles['sencillas'].pop(0)
            return habitacion
        else:
            return None
    elif tipo_habitacion == 'doble':
        if habitaciones_disponibles['dobles']:
            habitacion = habitaciones_disponibles['dobles'].pop(0)
            return habitacion
        else:
            return None
    elif tipo_habitacion == 'suite':
        if habitaciones_disponibles['suites']:
            habitacion = habitaciones_disponibles['suites'].pop(0)
            return habitacion
        else:
            return None