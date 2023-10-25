from django.shortcuts import render , redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            # Tengo que avisar que todo fue bien
            return redirect(reverse('contact')+'?ok')
        
        else:
            #Tengo que generar un error
            return redirect(reverse('contact')+'?error')   

    return render(request, 'Academia/contact.html', {'form':contact_form})
