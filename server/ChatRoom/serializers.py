from rest_framework.serializers import ModelSerializer
from .models import (
     Room,
     RoomMembership,
     Message
)

class RoomModelSerializer(ModelSerializer):
     class Meta:
          model = Room
          exclude = ["messages"]
          
class RoomMembershipModelSerializer(ModelSerializer):
     class Meta:
          model = RoomMembership
          fields = "__all__"
          
class MessageModelSerializer(ModelSerializer):
     class Meta:
          model = Message
          fields = "__all__"
          