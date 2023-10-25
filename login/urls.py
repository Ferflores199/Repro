from django.urls import path
from .views import Registro, cerrar_session, logear
from . import views

urlpatterns= [
    path('Register/', Registro.as_view(), name='Register'),
    path('cerrar_session', cerrar_session, name='cerrar_session'),
    path('login/', logear, name='logear'),
]