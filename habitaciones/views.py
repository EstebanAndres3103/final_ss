from django.shortcuts import render,redirect
from .total_habitaciones import reservar_habitacion, noches
from .asignacion import asignar_habitacion
from . import models
# Create your views here.
def habitaciones(request):
    return render(request,'habitaciones.html')

def confirmacion(request):
    tipo_habitacion=request.POST.get('tipo_habitacion')
    numero_de_cuarto=asignar_habitacion(tipo_habitacion)
    num_huespedes=int(request.POST.get('num_huespedes'))
    fecha_entrada=request.POST.get('fecha_entrada')
    fecha_salida=request.POST.get('fecha_salida')
    num_noche=noches(fecha_entrada,fecha_salida)
    data=reservar_habitacion(tipo_habitacion,num_noche,num_huespedes)
    print('confirmacion ', numero_de_cuarto)
    context={
        'data':data, 
        'habitacion':tipo_habitacion, 
        'huespedes':num_huespedes,
        'noches': num_noche,
        'numero_de_cuarto': numero_de_cuarto
        }
    return render(request,'confirmacion.html', context)

def registro(request):
    

    habitacion=request.POST.get('habitacion')
    num_cuarto=request.POST.get('numero_de_cuarto')
    huespedes=request.POST.get('huespedes')
    noches=request.POST.get('noches')
    data=request.POST.get('data')

    print('registro ', num_cuarto)
    context={
        'habitacion':habitacion,
        'num_cuarto':num_cuarto,
        'huespedes':huespedes,
        'noches':noches,
        'data':data
    }

    return render(request,'registro.html',context)

def exito(request):

    if request.method=='POST':

        habitacion=request.POST.get('habitacion')
        num_cuarto=request.POST.get('num_cuarto')
        huespedes=request.POST.get('huespedes')
        noches=request.POST.get('noches')
        data=request.POST.get('data')
        print('exito ', num_cuarto)
        dpi=request.POST.get('dpi')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')
        nombre=request.POST.get('nombre')
      
        clientes=models.Cliente(dpi=dpi,correo=correo,telefono=telefono,nombre=nombre)
        clientes.save()

        cuartos=models.Reservacion(tipo_cuarto=habitacion,numero_cuarto=num_cuarto,numero_huespedes=huespedes,
                                   cliente=clientes,noches=noches)
        cuartos.save()

        monto=models.Total(monto_total=data,cliente=clientes)
        monto.save()


    return render(request,'exito.html')