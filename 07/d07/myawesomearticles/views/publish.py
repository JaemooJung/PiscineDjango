from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PublishView(CreateView, LoginRequiredMixin):
    form_class = ArticleForm
    success_url = reverse_lazy('articles')
    login_url = reverse_lazy('login')
    template_name = 'publish.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)