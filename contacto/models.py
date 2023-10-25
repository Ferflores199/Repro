from django.db import models


options =[
    [0, 'Informacion de ingreso'],
    [1, 'Bloqueo de Usuario'],
    [2, 'Seguimiento de un tramite para Docente'],
    [3, 'No sirve el portal']
]
# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=1000, verbose_name='Nombre y Apellido')
    email= models.EmailField(verbose_name='Correo electrónico')
    message= models.TextField(verbose_name='Mensaje')
    contact= models.IntegerField(choices=options, verbose_name='Tipo de contacto')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envio')
    