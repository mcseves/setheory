from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'swetheory/home.html', {})

def areaofinterest(request):
    return render(request, 'swetheory/home.html', {})