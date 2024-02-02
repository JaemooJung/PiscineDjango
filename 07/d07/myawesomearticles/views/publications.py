from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import Article
from django.urls import reverse_lazy

class PublicationsView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'publications.html'
    context_object_name = 'publications'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)