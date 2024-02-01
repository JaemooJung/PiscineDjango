from django import forms
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from ..models import TipModel

class TipForm(ModelForm):
    class Meta:
        model = TipModel
        fields = ['content']

class VoteForm(forms.Form):
    _method = forms.CharField(widget=HiddenInput(), initial='put')
    tip_id = forms.IntegerField(widget=HiddenInput())
    is_upvote = forms.CharField(widget=HiddenInput())
    
    def __init__(self, tip_id, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        if tip_id:
            self.fields['tip_id'].initial = tip_id

class DeleteTipForm(forms.Form):
    _method = forms.CharField(widget=HiddenInput(), initial='delete')
    id = forms.IntegerField(widget=HiddenInput())

    def __init__(self, id, *args, **kwargs):
        super(DeleteTipForm, self).__init__(*args, **kwargs)
        if id:
            self.fields['id'].initial = id
