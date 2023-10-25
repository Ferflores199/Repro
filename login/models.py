from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create Estudiantes.

class Estudiantes (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.ForeignKey(User, related_name='estudiantes_first_name', on_delete=models.CASCADE)
    last_name = models.ForeignKey(User, related_name='estudiantes_last_name', on_delete=models.CASCADE)

    first_name = models.CharField(max_length=150, null=False, default='Nombres')
    last_name = models.CharField(max_length=150, null=False, default='Apellidos')

    username = models.CharField(max_length=150, null=False, default='user')
    email = models.EmailField(max_length=150, default="direccion@gmail.com")

    cui = models.CharField(max_length=13, null=False, default="0")

    profile_image = models.ImageField(upload_to='users_pictures', default='users_pictures/default.png')

    login_attempts = models.IntegerField(null=False, default=0)
    active_account = models.BooleanField(null=False, default=True)

    def str(self):
        return self.username 
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'usuarios_info'
        verbose_name='Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering=['id']

