from django.urls import path
from . import views

urlpatterns = [
    path('display', views.Display.as_view(), name='ex09_display'),
]
