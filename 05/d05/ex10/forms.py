from .models import People
from django import forms

class SearchForm(forms.Form):
  min_release_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
  max_release_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
  min_planet_diameter = forms.IntegerField(required=True)
  gender = forms.ChoiceField(required=True, choices=list(set(People.objects.values_list('gender', 'gender'))))

