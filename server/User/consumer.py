from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Profile
from django.contrib.auth.models import User

class LoginConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          
          user = self.scope["user"]
          await self.accept()
        
     async def receive(self, text_data=None, bytes_data=None):
          pass
     
     async def disconnect(self, code):
          """
          Called when a WebSocket connection is closed.
          """
          pass
     
     @sync_to_async
     def login_user_to_database(self, user:User):
          profile = Profile.objects.get(user = user)
          profile.is_online = True
          profile.save()