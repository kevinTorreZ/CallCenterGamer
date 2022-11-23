from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from online.models import Preguntas,Usuario
@login_required()
def IndexAdmin(request):
    ListaPreguntas = Preguntas.objects.all()

    return render(request, "indexAdmin.html", {"Preguntas":ListaPreguntas})