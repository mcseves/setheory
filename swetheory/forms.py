from django import forms
from .models import *


class CauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = '__all__'


class EffectForm(forms.ModelForm):
    class Meta:
        model = Effect
        fields = '__all__'


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = EvidenceEffect
        fields = '__all__'
