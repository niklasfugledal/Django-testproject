# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.models import Building


def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'building_list.html', {'buildings': buildings})

def home(request):
    if request.method == 'POST':
        return render(request, 'leaflet_map.html')
    else:
        return render(request, 'home.html')



def create_building(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        geometry = request.POST.get('geometry')

        building = Building(name=name, geometry=geometry)
        building.save()

        return JsonResponse({'status': 'ok'})
    else:
        return render(request, 'leaflet_map.html')