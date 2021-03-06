from django import forms
from django.forms.widgets import DateInput
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class EnterData(forms.ModelForm):
    date_seen = forms.DateField(widget = DateInput)
    class Meta:
        model = models.Species
        fields = ['name', 'in_country', 'county', 'date_seen', 'photo']
