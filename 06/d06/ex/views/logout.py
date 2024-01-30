from django.contrib.auth import logout
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect

class Logout(View):

    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'You are not logged in.')
            return redirect('index')
        
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('index')