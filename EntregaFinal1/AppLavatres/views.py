from email import message
from django.contrib import messages
from django.shortcuts import render, redirect
from AppLavatres.models import Vehiculo, Indumentaria, Animal
from AppLavatres.forms import FormularioVehiculo, FormularioIndumentaria, FormularioAnimales

def inicio(request):
    contexto = {
        "valor1": "este es un valor"
    }
    return render(request, 'index.html', contexto)


def vehiculo_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioVehiculo(data=request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            vehiculo1 = Vehiculo(tipo_vehiculo=data.get('tipo_vehiculo'), aspirado=data.get('aspirado'), dominio=data.get('dominio'), ingreso=data.get('ingreso'), egreso=data.get('egreso'))
            vehiculo1.save()
            messages.info(request, 'Vehículo cargado satisfactoriamente')
            return redirect('AppLavatresAutoFormulario')
            
        else:
            messages.info(request, 'formulario no cargado')
         
    
    vehiculos = Vehiculo.objects.all()
    contexto = {
        'form': FormularioVehiculo(),
        'vehiculos': vehiculos
    }
    return render(request, 'AppLavatres/vehiculos.html', contexto)
            
            
def indumentaria_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioIndumentaria(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            indumentaria1 = Indumentaria(tipo_indumentaria=data.get('tipo_indumentaria'), ropa_blanca=data.get('ropa_blanca'), nombre_cliente=data.get('nombre_cliente'), fecha_retiro=data.get('fecha_retiro'))
            indumentaria1.save()
            messages.info(request, 'Prenda cargada satisfactoriamente')
            return redirect('AppLavatresIndumentariaFormulario')
    
    indumentaria1 = Indumentaria.objects.all()
    contexto = {
        'form': FormularioIndumentaria(),
        'indumentaria': Indumentaria
    }
    return render(request, 'AppLavatres/indumentarias.html', contexto)
               

def animales_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioAnimales(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            animal1 = Animal(tipo_animal=data.get('tipo_animal'), nombre_duenio=data.get('nombre_duenio'), corte_pelo=data.get('corte_pelo'), fecha_turno=data.get('fecha_turno'))
            animal1.save()
            messages.info(request, 'Mascota cargada satisfactoriamente')
            return redirect('AppLavatresMascotaFormulario')
    
    animal1 = Animal.objects.all()
    contexto = {
        'form': FormularioAnimales(),
        'animal': Animal
    }
    return render(request, 'AppLavatres/animales.html', contexto)




