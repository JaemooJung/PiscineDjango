from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('tip/', views.Tip.as_view(), name='tip'),
]