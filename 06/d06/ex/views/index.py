from django.views import View
from django.shortcuts import render
from ..forms import *
from ..models import TipModel

class Index(View):
    def get(self, request):
        try:
            tips = TipModel.objects.all().order_by('-date')
        except Exception as e:
            tips = []
        context = {
            'tip_form': TipForm(),
            'tips': [{
                'id': tip.id,
                'content': tip.content,
                'author': tip.author,
                'date': tip.date,
                'up_votes': tip.get_upvotes(),
                'down_votes': tip.get_downvotes(),
                'deleteform': DeleteTipForm(tip.id),
                'voteform': VoteForm(tip.id),
            } for tip in tips]
        }
        return render(request, 'index.html', context)