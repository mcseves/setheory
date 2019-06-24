from django import forms
from .models import *


class CauseForm(forms.ModelForm):
    def __init__(self, area, *args, **kwargs):
        super(CauseForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = Construct.objects.filter(area=area)
        # for field in self.fields:
        #     self.fields[field].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Cause
        fields = '__all__'


class EffectForm(forms.ModelForm):
    def __init__(self, area, *args, **kwargs):
        super(EffectForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = Construct.objects.filter(area=area)

    class Meta:
        model = Effect
        fields = '__all__'


class EvidenceForm(forms.ModelForm):
    class Meta:
        model = EvidenceEffect
        fields = '__all__'
