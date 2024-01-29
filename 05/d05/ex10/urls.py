from django.urls import path
from . import views

urlpatterns = [
    path('', views.Display.as_view(), name='ex10_display'),
]
