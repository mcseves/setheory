from django import forms
from .models import *


# class NewTheoryForm(forms.ModelForm):
#
#     class Meta:
#         model = Cause
#         fields = ['name', 'reference_value', 'observed_value']

class CauseForm(forms.ModelForm):

    class Meta:
        model = Cause
        fields = ['name', 'reference_value', 'observed_value']


class EffectForm(forms.ModelForm):
    class Meta:
        model = Effect
        fields = ['name', 'observed_value']


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = EvidenceEffect
        fields = '__all__'
