from django.urls import path
from django.views.i18n import set_language
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('publications/', PublicationsView.as_view(), name='publications'),
    path('publish/', PublishView.as_view(), name='publish'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('i18n/setlang/', set_language, name='set_language'),
]