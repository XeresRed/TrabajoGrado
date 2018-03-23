from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.adopcion.models import Persona
from apps.adopcion.forms import PersonaForm
# Create your views here.

def index(request):
    if request.method == "POST":
        persona = Persona.objects.get(email=request.POST["correo"])
        if(persona.password == request.POST["pass"]):
            return HttpResponse("Bienvenido al sistema " + persona.username)
        else:
            return HttpResponse("paso algo")

    return render(request,"index/index.html")


def mascota_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, 'index/registro.html', {'form':form, 'correto':'v'})
        elif request.POST["correo"] != '':
            persona = Persona.objects.get(email=request.POST["correo"])
            if(persona.password == request.POST["pass"]):
                return HttpResponse("Bienvenido al sistema " + persona.username)
            else:
                return HttpResponse("paso algo")

        return redirect('index')
    else:
        form = PersonaForm()

    return render(request, 'index/registro.html', {'form':form, 'correto':'f'})
