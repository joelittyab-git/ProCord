from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpRequest
from django.contrib.auth.models import User
from .models import(
     Room,
     RoomMembership
)
from .serializers import (
     RoomMembershipModelSerializer,
     RoomModelSerializer
)

'''
-----------------------------------------------------------------------------------------Room-RegistrationView-View-------------------------------------------------------------------------------------------------
**URL["/server/room/register/"](POST) => registers the created room and its users to the database
     :request:{
          "title":...,
          "description":...,
          "users":[
               ...[usernames]
          ]
    }
     :response:
          {"status":"success"} -> registration status successfull
          {"status":"exception","info":{...}}} -> database integrity error / other exceptions
          
**URL["/server/room/register/"](GET) => Gets the registered chat rooms for whcih the user is a part of
     :request:{}
     :response:
          {"status":"success", "rooms":[...]} -> rreturns the rooms the user ios a part of
          {"status":"exception","info":{...}}} -> database integrity error / other exceptions
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' 
class RoomRegistrationView(APIView):
     permission_classes = [
          IsAuthenticated,
     ]
     
     def post(self, request:HttpRequest, *args, **kwargs):  
          # extracting request data        
          admin = request.user
          room_name = request.data.get("title")
          room_description = request.data.get("description")
          participant_list = request.data.get("users")
          
          # attemting to create a room entry to the database
          try:
               room = Room.objects.create(
                    name = room_name,
                    description = room_description,
                    admin = admin,
               )
               room.save()
          except Exception as e:
               return Response({"status":"exception", "info":str(e)})
          
          # extracting participant list from data and adding them
          for username in participant_list:
               try: users = User.objects.get(username = username)
               except Exception as e:return Response({"status":"exception", "info":str(e)})
               
               RoomMembership.objects.create(
                    room = room,
                    user = users
               ).save()

          return Response({"status":"success"})
          
     def get(self, request:HttpRequest, *args, **kwargs):
          user = request.user
          
          # filtering from datbase, the rooms for whcih the logged in user is an admin of
          rooms_admin = Room.objects.filter(admin = user)
          serialized_a = RoomModelSerializer(
               rooms_admin,
               many = True
          )
          
          # filtering from datbase, the rooms for whcih the logged in user is a participant of
          rooms = RoomMembership.objects.filter(
               user = user
          )
          serialized_b = RoomMembershipModelSerializer(rooms, many = True)
          
          room = []
          
          # getting the room for each membership
          try:
               for members in serialized_b.data:
                    member = dict(members)
                    member_room = Room.objects.get(room_id=(member.get("room")))
                    room_serialized =  RoomModelSerializer(member_room)
                    room+=[room_serialized.data]
          except Exception as e:return Response({"status":"exception", "info":{str(e)}})
                
          room = room + (serialized_a.data)

          # rooms = Room.objects.filter(admin=user)
          return Response({"status":"success", "rooms":room})




'''
-----------------------------------------------------------------------------------------RegistrationView-View-------------------------------------------------------------------------------------------------
**URL["/server/room/register/"](POST) => registers the created room and its users to the database
     :request:{
          "title":...,
          "description":...,
          "users":[
               ...[usernames]
          ]
    }
     :response:
          {"action":"redirect"} -> page should be redirected 
          {"action":"exception","info":{...}}} -> database integrity error / other exceptions
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''  
class RoomManagerView(APIView):
     permission_classes = [
          IsAuthenticated
     ]
     
     def get(self, request:HttpRequest, room_id, *args, **kwargs):
          
          # extracting request data
          user = request.user
          
          room = Room.objects.filter(room_id=room_id)
          
          # checking if the room with this number exists
          if(not room.exists() ) :
               return Response({"action":"redirect"})
          
          room = Room.objects.get(room_id=room_id)
          membership = RoomMembership.objects.filter(user=user, room__room_id = room_id)
          if(
               not room.admin is user or 
               not membership.exists()
          ):
               return Response({"action":"redirect"})
          
          print(room.messages)
          
          
          return Response({"data":room_id})
          
     
     