from django import forms
from .models import *


class CauseForm(forms.ModelForm):
    def __init__(self, area, *args, **kwargs):
        super(CauseForm, self).__init__(*args, **kwargs)
        self.fields['cause'] = forms.ModelChoiceField(queryset=Construct.objects.filter(area=area),label="Nome")

    class Meta:
        model = Cause
        fields = ['cause', 'reference_value_c', 'observed_value_c']
        labels = {
            'reference_value_c': 'Valor de referência',
            'observed_value_c': 'Valor observado'
        }


class EffectForm(forms.ModelForm):
    def __init__(self, area, *args, **kwargs):
        super(EffectForm, self).__init__(*args, **kwargs)
        self.fields['effect'] = forms.ModelChoiceField(queryset=Construct.objects.filter(area=area),label="Nome")

    class Meta:
        model = Effect
        fields = ['effect', 'observed_value']
        labels = {
            'observed_value': 'Valor observado'
        }


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = EvidenceEffect
        fields = ['name', 'scope', 'evidence_type', 'doi_number']
        labels = {
            'name': 'Nome',
            'scope': 'Escopo',
            'evidence_type': 'Tipo de evidência',
            'doi_number': 'Número DOI'
        }
