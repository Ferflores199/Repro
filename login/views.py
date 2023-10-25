
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Estudiantes
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class Registro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request,'Academia/register.html',{"form":form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = form.save()
            ncui = form.cleaned_data.get('cui')
            img = form.cleaned_data.get("profile_imagen")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(request=request, username=username, password=password)
            login(request, usuario)

            nuevo_usuario = Estudiantes(user=request.user, username=request.user.username, first_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email, cui=ncui, profile_image=img)
            nuevo_usuario.save()

            return redirect('lista_cursos')
        else:
            for field_name, error_messages in form.errors.items():
                for msg in error_messages:
                    messages.error(request, f"{field_name}: {msg}")

            return render(request, "Academia/register.html", {"form": form})
        
        
def cerrar_session(request):
    logout(request)

    return redirect("home")

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(request=request, username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)  # Asegúrate de que el objeto de usuario se pasa correctamente aquí
                return redirect("lista_cursos")
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = AuthenticationForm()
    return render(request, "Academia/login.html", {"form": form})
