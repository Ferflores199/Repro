from django.shortcuts import render

def home(request): # primera Vista

    return render(request, 'Academia/index.html')

def about(request): # Conocenos

    return render(request, 'Academia/about.html')

def services(request): # Conocenos

    return render(request, 'Academia/services.html')



