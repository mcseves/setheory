from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .forms import *
from .models import *


def home(request):
    areas = AreaOfInterest.objects.all()
    args = {'areas': areas}

    return render(request, 'swetheory/home.html', args)


def about(request):

    return render(request, 'swetheory/about.html')


def area_of_interest(request, name):
    current_area = get_object_or_404(AreaOfInterest, name=name)
    all_cause = Cause.objects.all()
    all_effect = Effect.objects.all()
    all_proposition = Proposition.objects.all()
    args = {'current_area': current_area, 'all_cause': all_cause, 'all_effect': all_effect, 'all_proposition': all_proposition}

    return render(request, 'swetheory/area.html', args)


def new_theory(request, name):
    current_area = get_object_or_404(AreaOfInterest, name=name)

    if request.method == 'POST':
        causeform = CauseForm(current_area, request.POST)
        effectform = EffectForm(current_area, request.POST)
        evidenceform = EvidenceForm(request.POST)

        if causeform.is_valid() and effectform.is_valid() and evidenceform.is_valid():
            newcause = causeform.save(commit=False)
            newcause.save()
            neweffect = effectform.save(commit=False)
            neweffect.save()
            newevidence = evidenceform.save(commit=False)
            newevidence.save()

            newproposition = Proposition(area=current_area, evidence=newevidence)
            newproposition.save()
            newproposition.cause.add(newcause)
            newproposition.effect.add(neweffect)
            return redirect('area_of_interest', name=name)

        else:
            print(causeform.errors)
            print(effectform.errors)
            print(evidenceform.errors)
    else:
        causeform = CauseForm(current_area)
        effectform = EffectForm(current_area)
        evidenceform = EvidenceForm()

    return render(request, 'swetheory/createtheories.html', {'current_area': current_area, 'causeform': causeform,
                                                             'effectform': effectform, 'evidenceform': evidenceform})


def search_theory(request):
    if request.method == 'POST':
        search_cause = request.POST.get('search_cause', False)
        search_effect = request.POST.get('search_effect', False)
        search_proposition = request.POST.get('search_proposition', False)

    else:
        search_cause = False
        search_effect = False
        search_proposition = False

    causes = Cause.objects.filter(cause__name=search_cause)
    effects = Effect.objects.filter(effect__name=search_effect)
    # props = Proposition.objects.all()
    print(causes)
    print(effects)

    result_props = set()
    if causes:
        if effects:
            for cse in causes:
                for eff in effects:
                    queryset = Proposition.objects.filter(
                        cause__cause__name__contains=cse,
                        effect__effect__name__contains=eff,
                    )
                    print("query: ")
                    print(queryset)
                    print(result_props)
                    if queryset not in result_props:
                        result_props.add(queryset)

    # print(result_props)

    return render(request, 'swetheory/search.html', {'result_props': result_props})


def add_construct(request, name):
    current_area = get_object_or_404(AreaOfInterest, name=name)
    if request.method == 'POST':
        form = ConstructForm(request.POST)
        if form.is_valid():
            construct = form.save(commit=False)
            construct.area = current_area
            construct.save()
            return redirect('new_theory', name=name)
        else:
            print(form.errors)

    else:
        form = ConstructForm()

    return render(request, 'swetheory/newconstruct.html', {'current_area': current_area, 'form': form})


def add_value(request, name):
    current_area = get_object_or_404(AreaOfInterest, name=name)
    if request.method == 'POST':
        form = ValueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_theory', name=name)
        else:
            print(form.errors)

    else:
        form = ValueForm()

    return render(request, 'swetheory/newvalue.html', {'current_area': current_area, 'form': form})
