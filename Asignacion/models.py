from django.db import models
from login.models import Estudiantes
from django.contrib.auth import get_user_model

# Create your models here.
class curso(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Curso')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = models.ImageField(upload_to='Tienda', null=False, blank=True)
    creditos = models.IntegerField(verbose_name='Creditos')
    cupo = models.IntegerField(verbose_name='Cupo')
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nombre  # Esto mostrará el nombre del curso en lugar del ID

class Horario(models.Model):
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10)  # Puedes usar 'Lunes', 'Martes', etc.
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.curso.nombre} - {self.dia}"  # Esto mostrará el nombre del curso y el día

class Nota(models.Model):
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.estudiante.username} - {self.curso.nombre}"  # Esto mostrará el nombre del estudiante y el nombre del curso

