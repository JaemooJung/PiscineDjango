from django.conf import settings
import time
import random

class SessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        if request.user.is_authenticated:
            return self.get_response(request)
        
        resistered_time = request.session.setdefault('registered_time', 
                                                     time.time())

        if time.time() - resistered_time > 42:
            request.session.flush()

        request.user.username = request.session.setdefault('username', 
                                                           random.choice(settings.RANDOM_USERNAMES))

        return self.get_response(request)