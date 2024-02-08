from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatRoomListView.as_view(), name='chatroom_list'),
    path('<int:pk>/', views.ChatRoomView.as_view(), name='chatroom'),
]