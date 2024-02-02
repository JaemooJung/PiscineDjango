from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import UserFavoriteArticle
from django.urls import reverse_lazy

class FavoritesView(LoginRequiredMixin, ListView):
    model = UserFavoriteArticle
    template_name = 'favorites.html'
    context_object_name = 'favorites'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return UserFavoriteArticle.objects.filter(user=self.request.user)
