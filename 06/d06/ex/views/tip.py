from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import TipForm

class Tip(LoginRequiredMixin, View):
    http_method_names = ['post']
    login_url = reverse_lazy('login')

    def post(self, request):
        form = TipForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Invalid form.')
            return redirect('index')

        try:
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            messages.success(request, 'Tip saved successfully.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
        return redirect('index')
