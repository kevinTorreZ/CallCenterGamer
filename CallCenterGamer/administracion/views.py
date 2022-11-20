from django.shortcuts import render


def IndexAdmin(request):
    return render(request, "indexAdmin.html")