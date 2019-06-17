from django.shortcuts import render
from .models import AreaOfInterest
from django.shortcuts import render, get_object_or_404
# Create your views here.


def home(request):
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for

        areas = AreaOfInterest.objects.all()
        args = {'areas': areas}

    return render(request, 'swetheory/home.html', args)


def area_of_interest(request, name):
    # return render(request, 'swetheory/areas.html', {})
    which_area = get_object_or_404(AreaOfInterest, name=name)

    return render(request, 'swetheory/area.html', {'which_area': which_area})
