from ast import Del
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Caretaker
from .forms import WateringForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello!</h1>')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    return render(request, 'plants/detail.html', {
        'plant': plant, 'watering_form': watering_form
    })

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'description', 'age']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

def assoc_caretaker(request, plant_id, caretaker_id):
    Plant.objects.get(id=plant_id).caretakers.add(caretaker_id)
    return redirect('detail', plant_id=plant_id)

def unassoc_caretaker(request, plant_id, caretaker_id):
    Plant.objects.get(id=plant_id).caretakers.remove(caretaker_id)
    return redirect('detail', plant_id=plant_id)

class CaretakerList(ListView):
    model = Caretaker

class CaretakerDetail(DetailView):
    model = Caretaker

class CaretakerCreate(CreateView):
    model = Caretaker
    fields = '__all__'

class CaretakerUpdate(UpdateView):
    model = Caretaker
    fields = ['name', 'description']

class CaretakerDelete(DeleteView):
    model = Caretaker
    success_url = '/caretakers/'
