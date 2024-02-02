from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
