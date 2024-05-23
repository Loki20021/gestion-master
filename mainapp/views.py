from django.shortcuts import render


# Create your views here.


def page_accueil(request):
    return render( request, 'mainapp/page_acceuil.html')

def conexion(request):
    return render( request, 'mainapp/conexion.html')

def BIM(request):
    return render( request, 'mainapp/BIM.html')

def GP(request):
    return render( request, 'mainapp/GP.html')