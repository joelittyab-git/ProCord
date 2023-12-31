from django.db import models
from django.contrib.auth.models import User

'''
------------------------------------------------------------------------------Profile-model-------------------------------------------------------------------------------------------------
[user]:OneToOneField -> points to the user of a particular profile
[friend_list]:ManyToManyField -> points to the user(:User) of the friendship (Many Friendship -> single User)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
'''
class Profile(models.Model):
     profile_picture_media_root = "user/pictures"
     
     user = models.OneToOneField(
          User,
          on_delete=models.CASCADE
     )     
     telephone = models.BigIntegerField(default=0)     
     friend_list = models.ManyToManyField("self", through="Friendship")
     image = models.ImageField(upload_to=profile_picture_media_root, null=True, default=None, blank=True)
     is_online = models.BooleanField(default=False)
     
     def __str__(self) -> str:
          return f"{self.user.username}'s profile"
     
'''
------------------------------------------------------------------------------Friendship-model[through]-------------------------------------------------------------------------------------------------
[friendship_id]:IntegerField -> stores the primary key of the particular friendship
[user1]:ForeignKey -> points to the user(:User) of the friendship (Many Friendship -> single User)
[user2]:ForeignKey -> points to the user(:User) of the friendship (Many Friendship -> single User)
[created_at]:DateTimeField -> stores the date and time of the friendship created
[category]:CharField -> stores the type of friendship
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
class Friendship(models.Model):
     
     friendship_id = models.BigAutoField(primary_key=True)
     
     user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_a")
     user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_b")
     
     created_at = models.DateTimeField(auto_now_add=True)
     category = models.CharField(max_length=100)
     
     
