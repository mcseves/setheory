from django import forms
from .models import *


class ConstructForm(forms.ModelForm):
    class Meta:
        model = Construct
        fields = ['name']
        labels = {
            'name': 'Name'
        }


class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['name']
        labels = {
            'name': 'Name'
        }


class CauseForm(forms.ModelForm):
    def __init__(self, area, *args, **kwargs):
        super(CauseForm, self).__init__(*args, **kwargs)
        self.fields['cause'] = forms.ModelChoiceField(queryset=Construct.objects.filter(area=area), label="Name")

    class Meta:
        model = Cause
        fields = ['cause', 'reference_value_c', 'observed_value_c']
        labels = {
            'reference_value_c': 'Reference value',
            'observed_value_c': 'Observed value'
        }


class EffectForm(forms.ModelForm):
    def __init__(self, area, *args, **kwargs):
        super(EffectForm, self).__init__(*args, **kwargs)
        self.fields['effect'] = forms.ModelChoiceField(queryset=Construct.objects.filter(area=area), label="Name")

    class Meta:
        model = Effect
        fields = ['effect', 'observed_value']
        labels = {
            'observed_value': 'Observed value'
        }


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = EvidenceEffect
        fields = ['name', 'scope', 'evidence_type', 'doi_number']
        labels = {
            'doi_number': 'DOI Number'
        }
