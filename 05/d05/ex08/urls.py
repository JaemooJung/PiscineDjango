from .views import *
from django.urls import path

urlpatterns = [
    path('init/', Init.as_view(), name='ex08-init'),
]