from django.shortcuts import render


def Index(request):
    return render(request, "index.html")
def Login(request):
    return render(request, "login.html")
def Register(request):
    return render(request, "register.html")
def Inicio(request):
    return render(request, "idnicio.html")