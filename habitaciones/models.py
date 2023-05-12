from django.db import models


class Cliente(models.Model):
    dpi = models.CharField(max_length=50,primary_key=True)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Reservacion(models.Model):
    TIPO_CHOICES = [
        ('S', 'Sencilla'),
        ('D', 'Doble'),
        ('U', 'Suite'),
    ]
    tipo_cuarto = models.CharField(max_length=10, choices=TIPO_CHOICES)
    numero_cuarto = models.IntegerField()
    numero_huespedes = models.IntegerField()
    noches=models.IntegerField(default=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_cuarto} - {self.numero_cuarto}"


class Total(models.Model):
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente} - ${self.monto_total}"
