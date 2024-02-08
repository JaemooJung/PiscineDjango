from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountView.as_view(), name='account'),
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
    path('check_login/', views.check_login, name='check_login'),
]