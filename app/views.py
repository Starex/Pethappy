from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .forms import MascotaForm
from django.core.mail import send_mail  # Asegúrate de importar send_mail

def index(request):
    return render(request, 'app/index.html')

def service(request):
    return render(request, 'app/service.html')


def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            mascota = form.save() # Guarda la mascota y obtén el objeto Mascota
            
            # Calcular la cantidad de comida usando el peso de la mascota guardada
            cantidad_comida = mascota.peso * 0.025 * 30  # peso * 2.5% * 30
            cantidad_diaria = cantidad_comida / 30

            # Mostrar el mensaje con la cantidad de comida
            mensaje = f"Tu mascota deberia comer {cantidad_comida} kg al mes y {cantidad_diaria} kg al dia"
            return render(request, 'app/service.html', {'mensaje': mensaje, 'form': MascotaForm()})  # Ajusta 'app/service.html'

    else: 
        form = MascotaForm() # Crea una instancia del formulario si no es una solicitud POST
    return render(request, 'app/service.html', {'form': form})