"""ex_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as log
from habitaciones import views as hab

urlpatterns = [
    path('mostrar_tablas/',log.mostrar_tablas, name='mostrar_tablas'),
    path('eliminar_tablas/',log.eliminar_tablas, name='eliminar_tablas'),
    path('exito/',hab.exito, name='exito'),
    path('registro/',hab.registro, name='registro'),
    path('confirmacion/', hab.confirmacion, name='confirmacion'),
    path('habitaciones/', hab.habitaciones, name='habitaciones'),
    path('login/', log.logon, name='logon'),
    path('logout/', log.logout_view, name='logout'),
    path('menu_admin/', log.menu_admin, name='menu_admin'),
    path('home/', log.homepage, name='home'),
    path('', log.homepage, name='home'),
    path('admin/', admin.site.urls),

]
