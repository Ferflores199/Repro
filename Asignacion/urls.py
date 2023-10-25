from django.urls import path
from . import views

urlpatterns=[
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('carrito/', views.carrito, name='carrito'),
]
