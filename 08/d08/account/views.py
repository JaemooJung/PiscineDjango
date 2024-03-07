from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.middleware.csrf import get_token
from django.urls import reverse_lazy
from typing import Any
from django.contrib import messages
from django.shortcuts import redirect

class AccountView(View):
    def get(self, request):
        context = {
            "login_form": AuthenticationForm(),
        }
        return render(request, 'account.html', context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account')
    template_name = 'signup.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            messages.error(request, "You are already logged in.")
            return redirect('account')
        return super().dispatch(request, *args, **kwargs)


def check_login(request):
    if request.user.is_authenticated:
        data = {
            "status": "logged_in",
            "username": request.user.username,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"status": "logged_out"}, status=401)

@require_POST
def do_login(request):
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        login(request, form.get_user())
        data = {
            "status": "ok",
            "username": request.user.username,
            "csrf_token": get_token(request),
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"status": "error", "errors": form.errors}, status=401)
    
@require_POST
def do_logout(request):
    logout(request)
    data = {
        "status": "ok",
        "csrf_token": get_token(request),
    }
    return JsonResponse(data)
