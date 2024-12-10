# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Exterior, Interior, Usuario, Carnivora


def inicio(request):
    return render(request,"App1/index.html")

def exterior(request):
    return render(request,"App1/exterior.html")

def interior(request):
    query = request.GET.get("q")
    if query:
        planta_int = Interior.objects.filter(nombre_cientifico__icontains=query)

    else:
        planta_int = Interior.objects.all()
    print(planta_int)
    return render(request,"App1/interior.html",{"planta_int":planta_int})

def carnivora(request):
    return render(request,"App1/carnivoras.html")


def formulario_exteriores(request):
    if request.method == "POST":
        planta = Exterior(nombre_cientifico = request.POST["nombre_cientifico"],
                        nombre_comun = request.POST["nombre_comun"],
                        tipo_de_clima= request.POST["tipo_clima"],
                        riego_semanal= request.POST["riego_semanal"],
                        ciudados_especiales=request.POST["cuidados_especiales"],
                        foto = request.POST["foto"])
        planta.save()
        return redirect("exterior")
    else:    
        return render(request,"App1/forms/exteriores-formulario.html")
    
def formulario_interiores(request):
    if request.method == "POST":
        planta = Interior(nombre_cientifico = request.POST["nombre_cientifico"],
                        nombre_comun = request.POST["nombre_comun"],
                        tipo_de_luz= request.POST["tipo_luz"],
                        riego_semanal= request.POST["riego_semanal"],
                        foto = request.POST["foto"])
        planta.save()
        return redirect("interior")
    else:    
        return render(request,"App1/forms/interiores-formulario.html")
    
def formulario_carnivoras(request):
    if request.method == "POST":
        planta = Carnivora(nombre_cientifico = request.POST["nombre_cientifico"],
                        nombre_comun = request.POST["nombre_comun"],
                        tipo_de_clima= request.POST["tipo_clima"],
                        riego_semanal= request.POST["riego_semanal"],
                        ciudados_especiales=request.POST["cuidados_especiales"],
                        alimentacion = request.POST["alimentacion"],
                        foto = request.POST["foto"])
        planta.save()
        return redirect("carnivoras")
    else:    
        return render(request,"App1/forms/carnivoras-formulario.html")

