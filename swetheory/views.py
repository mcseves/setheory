from django.shortcuts import render, redirect, get_object_or_404
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


    if request.method == 'POST':
        # causeconstruct = request.POST['causeconstruct']
        # refvalue = request.POST['refvalue']
        # obsvalue = request.POST['obsvalue']

        # user = User.objects.first()

        # cause = Cause.objects.create(
        #     name=causeconstruct,
        #     reference_value=refvalue,
        #     observed_value=obsvalue
        # )

        constructname = request.POST['construct']

        construct = Construct.objects.create(
            name=constructname,
            area=current_area
        )


        return redirect('area_of_interest', name=name)

    return render(request, 'swetheory/createtheories.html', {'current_area': current_area})
