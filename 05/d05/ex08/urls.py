from .views import *
from django.urls import path

urlpatterns = [
    path('init/', Init.as_view(), name='ex08-init'),
    path('populate/', Populate.as_view(), name='ex08-populate'),
    path('display/', Display.as_view(), name='ex08-display'),
]