from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTheoryForm
from .models import *


def home(request):
    if request.method == 'GET':  # If the form is submitted
        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for

        areas = AreaOfInterest.objects.all()
        args = {'areas': areas}

    return render(request, 'swetheory/home.html', args)


def area_of_interest(request, name):
    # return render(request, 'swetheory/areas.html', {})
    current_area = get_object_or_404(AreaOfInterest, name=name)
    all_construct = Construct.objects.all()

    return render(request, 'swetheory/area.html', {'current_area': current_area, 'all_construct': all_construct})


def new_theory(request, name):
    current_area = get_object_or_404(AreaOfInterest, name=name)
    # user = User.objects.first()

    if request.method == 'POST':
        form = NewTheoryForm(request.POST)
        if form.is_valid():
            construct = form.save(commit=False)
            construct.area = current_area
            construct.save()
            return redirect('area_of_interest', name=name)
        else:
            print(form.errors)
    else:

        form = NewTheoryForm()

    return render(request, 'swetheory/createtheories.html', {'current_area': current_area, 'form': form})
