from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync, sync_to_async
from .models import(
   Room,
   RoomMembership,
   MessageReference,
   Message
)

class ChatConsumer(AsyncWebsocketConsumer):
   async def connect(self):
      
      await self.accept()
      # extracting user from header
      user = (self.scope["user"])
      
      # extracting data from url
      room_id = int(self.scope["url_route"]["kwargs"]["room_id"])
      
      # authorizing user membership
      is_member = await (self.is_room_member(room_id, str(user)))
      is_admin = await (self.is_room_admin(room_id, str(user)))
   
      if(
         not (
            is_admin or is_member
         )
      ):
         await self.send(json.dumps({"authorization":"denied"}))
         self.disconnect()
   
      self.group_name = str(room_id)
      await self.send(json.dumps({"authorization":"success"}))
      
      await (self.channel_layer.group_add)(
         self.group_name,
         self.channel_name
      )
      


   async def disconnect(self, close_code):
      try:
         print("disconnecting")
         await self.channel_layer.group_discard(
               self.room_group_name,
               self.channel_name
         )
      except Exception:
         pass

   async def receive(self, text_data):
      # extracting data from params
      data = json.loads(text_data)
      message = data['message']
      user = self.scope["user"]
      
      await(
         self.commit_message_to_db(
            str(message),
            str(user),
            self.group_name
         )
      )
      
      await(
         self.channel_layer.group_send(
            self.group_name,
            {
               "type":"chat.message",
               "message":message
            }
         )
      )
      

   async def chat_message(self, event):
      message = event["message"]
      
      await self.send(
         json.dumps({"message":message})
      )
      

   @sync_to_async
   def is_room_member(self,room:int, user:str):
      return  (
         RoomMembership.
         objects.
         filter(room__room_id = int(room), user__username = user)
         .exists()
      )
   
   @sync_to_async
   def is_room_admin(self, room:int, user:str):
      return(
         Room.
         objects.
         filter(room_id = room,admin__username = user).
         exists()
      )
   
   @sync_to_async
   def commit_message_to_db(
      self,
      content:str,
      posted_by_username:str,
      room_id:int
   ):
      try:
         msg = Message.objects.create(
            content = content,
            posted_by__username = posted_by_username
         )
         msg.save()
         
         MessageReference.objects.create(
            message = msg,
            room = room_id
         ).save()
         
      except Exception as e:
         pass