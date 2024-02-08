from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.middleware.csrf import get_token

class AccountView(View):
    def get(self, request):
        context = {
            "login_form": AuthenticationForm(),
        }
        return render(request, 'account.html', context)

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
