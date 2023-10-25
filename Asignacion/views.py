from django.shortcuts import render
from .models import curso
# Create your views here.
def lista_cursos(request):
    
    cursos=curso.objects.all()
    return render(request, 'Academia/shop.html',{'cursos':cursos})

def carrito(request): # Conocenos
    cursos=curso.objects.all()
    return render(request, 'Academia/cart.html',{'cursos':cursos})
