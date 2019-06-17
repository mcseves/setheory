from django import forms
from .models import Construct


class NewTheoryForm(forms.ModelForm):

    class Meta:
        model = Construct
        fields = ['name']
