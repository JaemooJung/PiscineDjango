from django.http import HttpResponse
from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy

class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def get(self, request) -> HttpResponse:
        if request.user.is_authenticated:
            messages.error(self.request, 'You are already logged in.')
            return redirect('index')
        return super().get(request)
    
    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            messages.error(self.request, 'Invalid username or password.')
            return
        login(self.request, user)
        messages.success(self.request, f'Welcome back {user.username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

