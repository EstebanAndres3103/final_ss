'''
# Definimos la información de las habitaciones
HABITACIONES = {
    'sencilla': {'precio': 50, 'huespedes': 2, 'cantidad': 20},
    'doble': {'precio': 40, 'huespedes': 4, 'cantidad': 20},
    'suite': {'precio': 60, 'huespedes': 6, 'cantidad': 5}
}

def reservar_habitacion(tipo, noches, huespedes):
    # Verificamos que haya disponibilidad de la habitación
    if HABITACIONES[tipo]['cantidad'] <= 0:
        return 'No hay disponibilidad de habitaciones de este tipo'
    # Verificamos que la cantidad de huéspedes sea menor o igual a la permitida
    if huespedes > HABITACIONES[tipo]['huespedes']:
        return f'Esta habitación solo permite {HABITACIONES[tipo]["huespedes"]} huéspedes'
    # Calculamos el precio total de la reserva
    precio = HABITACIONES[tipo]['precio'] * huespedes * noches
    # Disminuimos la cantidad de habitaciones disponibles
    HABITACIONES[tipo]['cantidad'] -= 1
    return f'El total a pagar es ${precio} por {noches} noches de estadía en una habitación {tipo} para {huespedes} huéspedes'

# Ejemplo de uso
reserva = reservar_habitacion('doble', 3, 3)
print(reserva)
'''

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
        
a=''
while a!='parar':
    a=input('')
    a=asignar_habitacion(a)
    print(a)