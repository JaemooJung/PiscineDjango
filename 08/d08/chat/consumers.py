from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from .models import Chatroom, Message
from asgiref.sync import sync_to_async

import json

connected_users = {
    # chatroom_id: [user1, user2, ...]
}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'] == AnonymousUser():
            await self.close()
            return
        
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']

        if self.chatroom_id not in connected_users:
            connected_users[self.chatroom_id] = [self.scope['user'].username]
        else:
            connected_users[self.chatroom_id].append(self.scope['user'].username)

        await self.channel_layer.group_add(
            self.chatroom_id,
            self.channel_name
        )

        await self.accept()

        last_messages = await self.get_last_messages(self.chatroom_id)
        for message in last_messages:
            await self.send(text_data=json.dumps({
                'id': 'chat_message',
                'username': message['username'],
                'message': message['text'],
            }))
        await self.channel_layer.group_send(
            self.chatroom_id,
            {
                'type': 'user_list',
            }
        )

        await self.channel_layer.group_send(
            self.chatroom_id,
            {
                'type': 'user_joined',
                'username': self.scope['user'].username,
            }
        )

    async def disconnect(self, close_code):
        connected_users[self.chatroom_id].remove(self.scope['user'].username)

        await self.channel_layer.group_send(
            self.chatroom_id,
            {
                'type': 'user_list',
            }
        )

        await self.channel_layer.group_send(
            self.chatroom_id,
            {
                'type': 'user_left',
                'username': self.scope['user'].username,
            }
        )

        await self.channel_layer.group_discard(
            self.chatroom_id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.save_message(self.chatroom_id, self.scope['user'], message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.chatroom_id,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.scope['user'].username,
            }
        )


    async def user_joined(self, event):
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'id': 'user_joined',
            'message': f'{username} has joined the chat',
        }))

    async def user_left(self, event):
        username = event['username']

        await self.send(text_data=json.dumps({
            'id': 'user_left',
            'message': f'{username} has left the chat',
        }))

    async def user_list(self, event):
        await self.send(text_data=json.dumps({
            'id': 'user_list',
            'users': connected_users[self.chatroom_id],
        }))

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'id': 'chat_message',
            'message': message,
            'username': username,
        }))

    @staticmethod
    @sync_to_async
    def save_message(room_id, user, message_content):
        room = Chatroom.objects.get(id=room_id)
        message = Message(chatroom=room, user=user, text=message_content)
        message.save()

    @staticmethod
    @sync_to_async
    def get_last_messages(chatroom_id, count=3):
        messages = Message.objects.filter(chatroom_id=chatroom_id).order_by('-created')[:count][::-1]
        return [{'username': message.user.username, 
                 'text': message.text, 
                 'created': message.created} for message in messages]
