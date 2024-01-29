from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings
import random

class Index(View):
    def get(self, request):
        if not request.session.get('username'):
            request.session['username'] = random.choice(settings.USERNAMES)
            request.session.set_expiry(42)
        request.user.username = request.session.get('username')
        return render(request, 'index.html')