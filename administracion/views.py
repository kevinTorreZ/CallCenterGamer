from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from online.models import Preguntas,Usuario
@login_required()
def IndexAdmin(request):
    ListaPreguntas = Preguntas.objects.all()

    return render(request, "indexAdmin.html", {"Preguntas":ListaPreguntas})

def BorrarPregunta(request, idUser, idPregunta):
    Pregunta = Preguntas.objects.get(idPregunta=idPregunta)
    User = Usuario.objects.get(id=idUser)
    Pregunta.delete()
    if User.admin:
        return redirect("/Administracion/")
    else:
        return redirect("/Inicio/" + str(User.id))

def RegistroStaff(request):
    return render(request, "RegisterStaff.html")