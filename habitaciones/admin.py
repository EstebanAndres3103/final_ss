from django.contrib import admin
from .models import Cliente, Reservacion, Total

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dpi', 'nombre')

class ReservacionAdmin(admin.ModelAdmin):
    pass

class TotalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Total, TotalAdmin)