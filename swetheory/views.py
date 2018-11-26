from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'swetheory/home.html', {})

def displaytheories(request):
    return render(request, 'swetheory/displaytheories.html', {})

def createtheories(request):
    return render(request, 'swetheory/createtheories.html', {})