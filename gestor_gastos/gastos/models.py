from django.db import models
from django.utils import timezone

class Gasto(models.Model):
    CATEGORIAS = [
        ('Alimentación', 'Alimentación'),
        ('Transporte', 'Transporte'),
        ('Vivienda', 'Vivienda'),
        ('Salud', 'Salud'),
        ('Educación', 'Educación'),
        ('Entretenimiento', 'Entretenimiento'),
        ('Ropa', 'Ropa'),
        ('Servicios', 'Servicios'),
        ('Otros', 'Otros'),
    ]

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.descripcion or "Gasto"} - ${self.monto:.2f}'
