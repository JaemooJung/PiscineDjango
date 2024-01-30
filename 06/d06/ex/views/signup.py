from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy

class Signup(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def get(self, request) -> HttpResponse:
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in.')
            return redirect('index')
        
        return super().get(request)
    
    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Welcome {user.username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form: UserCreationForm) -> HttpResponse:
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)