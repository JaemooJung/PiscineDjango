from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('publications/', PublicationsView.as_view(), name='publications'),
]