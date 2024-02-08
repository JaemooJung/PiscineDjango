from django.shortcuts import render
from django.views import View
from .models import Chatroom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ChatRoomListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account')

    def get(self, request):
        chatrooms = Chatroom.objects.all()
        context = {
            "chatrooms": chatrooms,
        }
        return render(request, 'chatroom_list.html', context)

class ChatRoomView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account')

    def get(self, request, pk):
        chatroom = Chatroom.objects.get(pk=pk)
        context = {
            "chatroom": chatroom,
        }
        return render(request, 'chatroom.html', context)
