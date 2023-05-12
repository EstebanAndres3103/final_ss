from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from habitaciones import models

# Create your views here.


def homepage(request):
	return render(request,'home.html')


def logon(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		userSession =authenticate(request, username = username, password = password)
		if userSession:
			login(request, userSession)
			return redirect('menu_admin')
		else:
			return render(request, 'login.html', {'error':'Invalid username or password'})
	return render(request,'login.html')


def logout_view(request):
	logout(request)
	return redirect('logon')


@login_required

def menu_admin(request):
	return render(request,'menu_admin.html')

def mostrar_tablas(request):
	clientes=models.Cliente.objects.all()
	reservaciones=models.Reservacion.objects.all()
	totales=models.Total.objects.all()
	print(reservaciones)
	context={
		'clientes':clientes,
		'reservaciones':reservaciones,
		'totales':totales,
	}	
	return render(request,'mostrar.html',context)

def eliminar_tablas(request):
	if request.method == 'POST':
		dpi = request.POST.get('dpi')
		try:
			cliente = models.Cliente.objects.get(dpi=dpi)
			reservaciones = models.Reservacion.objects.filter(cliente=cliente)
			totales=models.Total.objects.filter(cliente=cliente)
			if reservaciones:
				reservaciones.delete()
			

                
				totales.delete()
				mensaje = f"Se eliminaron las reservaciones del cliente {cliente.nombre} con DPI {cliente.dpi}."
			else:
				mensaje = f"No se encontraron reservaciones para el cliente con DPI {dpi}."
		except models.Cliente.DoesNotExist:
			mensaje = f"No se encontró el cliente con DPI {dpi}."
		return render(request, 'eliminar.html', {'mensaje': mensaje})
	else:
		return render(request, 'eliminar.html')

