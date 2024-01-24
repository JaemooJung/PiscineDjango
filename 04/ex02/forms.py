from django import forms

class TextInput(forms.Form):
    text = forms.CharField(label='Text')
