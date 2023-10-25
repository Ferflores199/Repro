from django.shortcuts import render, redirect
from .carro import carro
from Asignacion.models import curso

# Create your views here.
def agregar_curso(request, curso_id): # Conocenos
    
    carro=carro(request)

    curso=curso.objets.get(id=curso_id)

    carro.agregar(curso=curso)

    return render('carrito')

def eliminar_curso(request, curso_id): # Conocenos
    
    carro=carro(request)

    curso=curso.objets.get(id=curso_id)

    carro.eliminar(curso=curso)

    return render('carrito')

def restar_curso(request, curso_id): # Conocenos
    
    carro=carro(request)

    curso=curso.objets.get(id=curso_id)

    carro.restar_curso(curso=curso)

    return render('carrito')

def limpiar_carro(request, curso_id): # Conocenos
    
    carro=carro(request)

    carro.limpiar_carro()

    return render('carrito')