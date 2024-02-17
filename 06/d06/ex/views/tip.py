from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from ..forms import *


class Tip(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def __error(self, request, method, message):
        messages.error(request, f'Invalid {method} request: {message}')
        return redirect('index')
    
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(Tip, self).dispatch(*args, **kwargs)
    
    def get(self, request):
        return redirect('index')

    def post(self, request: HttpRequest):
        form = TipForm(request.POST)

        if not form.is_valid():
            return self.__error(request, 'POST', form.errors)

        try:
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            messages.success(request, 'Tip saved successfully.')
        except Exception as e:
            return self.__error(request, 'POST', e)
        return redirect('index')
    
    def put(self, request: HttpRequest):
        form = VoteForm(None, request.POST)
        
        if not form.is_valid():
            return self.__error(request, 'PUT', "invalid form")
        is_upvote = True if form.cleaned_data['is_upvote'] == 'true' else False
        try:
            tip = TipModel.objects.get(pk=form.cleaned_data['tip_id'])
            if not is_upvote:
                is_author = tip.author == request.user
                if not is_author:
                    is_blacklisted = request.user.groups.filter(name='blacklist').exists()
                    if is_blacklisted or not request.user.can_downvote():
                        return self.__error(request, 'PUT', "user has no permission to downvote this tip")
            tip.vote(request.user, is_upvote)
            messages.success(request, 'Vote saved successfully.')
        except Exception as e:
            return self.__error(request, 'PUT', e)
        return redirect('index')
    
    def delete(self, request: HttpRequest):
        form = DeleteTipForm(None, request.POST)
        if not form.is_valid():
            return self.__error(request, 'DELETE', "invalid form")
        try:
            tip = TipModel.objects.get(pk=form.cleaned_data['id'])
            if tip.author != request.user and request.user.can_delete_tips() == False:
                return self.__error(request, 'DELETE', "user has no permission to delete this tip")
            tip.delete()
            messages.success(request, 'Tip deleted successfully.')
        except Exception as e:
            return self.__error(request, 'DELETE', e)
        return redirect('index')
