from django.shortcuts import render
from .models import AreaOfInterest
# Create your views here.

def home(request):
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for

        areas = AreaOfInterest.objects.all()
        args = {'areas': areas}

    return render(request, 'swetheory/home.html', args)

def displayareasofinterest(request):
    return render(request, 'swetheory/areaofinterest.html', {})

def displaytheories(request):
    return render(request, 'swetheory/displaytheories.html', {})

def createtheories(request):
    return render(request, 'swetheory/createtheories.html', {})