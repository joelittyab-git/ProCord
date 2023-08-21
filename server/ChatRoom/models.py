from django.db import models
from django.contrib.auth.models import User

'''
------------------------------------------------------------------------------ChatRoom-model-------------------------------------------------------------------------------------------------
[room_id]:IntegerField -> stores the primary key of the particular room
[name]:CharField -> stores the name of the room
[description]:CharField -> stores the description of the room 
[admin]:ForeignKey -> points to the admin(:User) of the room
[members]:ManyToManyField -> points to the  the users(:User) which are a part of that particular room :through:
[messages]:ManyToManyField -> Points to the messages that belongs to a particular room
[created_at]:DateTimeField -> stores the date and time of the room created
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
class Room(models.Model):
     room_id = models.BigAutoField(primary_key=True)
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=300)
     admin = models.ForeignKey(
          to=User,
          on_delete=models.DO_NOTHING,
          related_name="owner"
     )
     members = models.ManyToManyField(
          to=User,
          through='RoomMembership',
          related_name="participants"
     )
     messages = models.ManyToManyField(
          to="Message"
     )
     created_at = models.DateTimeField(auto_now_add=True)
     

'''
------------------------------------------------------------------------------RoomMembership-model[through]-------------------------------------------------------------------------------------------------
[membership_id]:IntegerField -> stores the primary key of the particular membership
[room]:ForeignKey -> points to the room(:Room) of the membership (Many RoomMembership -> single Room)
[user]:ForeignKey -> points to the user(:User) of the membership (Many RoomMembership -> single User)
[joined_at]:DateTimeField -> stores the date and time of the membership created
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''  
class RoomMembership(models.Model):
     membership_id = models.BigAutoField(primary_key=True)
     room = models.ForeignKey(
          to=Room,
          on_delete=models.CASCADE
     )
     user = models.ForeignKey(
          to=User,
          on_delete=models.CASCADE
     )
     joined_at = models.DateTimeField(auto_now_add=True)
 

'''
------------------------------------------------------------------------------Message-model-------------------------------------------------------------------------------------------------
[message_id]:IntegerField -> stores the primary key of the particular message
[content]:TextField -> stores the content of the message
[posted_by]:ForeignKey -> points to the author(:User) of the message
[posted_at]:DateTimeField -> stores the date and time of the message posted
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''    
class Message(models.Model):
     message_id = models.BigAutoField(primary_key=True)
     content = models.TextField(max_length=500)
     posted_by = models.ForeignKey(
          to=User,
          on_delete=models.DO_NOTHING
     )
     posted_at = models.DateTimeField(auto_now_add=True)