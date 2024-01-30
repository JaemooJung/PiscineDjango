from django.views import View
from django.shortcuts import render
from ..forms import TipForm
from ..models import Tip

class Index(View):
    def get(self, request):
        try:
            tips = Tip.objects.all().order_by('-date')
        except Exception as e:
            tips = []
        context = {
            'tip_form': TipForm(),
            'tips': tips
        }
        return render(request, 'index.html', context)