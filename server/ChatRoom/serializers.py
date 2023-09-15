from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Room,
    RoomMembership,
    Message
)


class RoomModelSerializer(ModelSerializer):
    members_username = serializers.SerializerMethodField()
    members_id = serializers.SerializerMethodField()
    admin = serializers.StringRelatedField()
    created_date_time = serializers.SerializerMethodField()

    class Meta:
        model = Room
        exclude = ["messages", "created_at", "members"]

    def get_members_username(self, obj):
        return [user.username for user in obj.members.all()]

    def get_created_at(self, obj):
        return str(obj.created_at)

    def get_created_date_time(self, obj):
        return str(obj.created_at).split(" ")

    def get_members_id(self, obj):
        return [member.id for member in obj.members.all()]


class RoomMembershipModelSerializer(ModelSerializer):
    class Meta:
        model = RoomMembership
        fields = "__all__"


class MessageModelSerializer(ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = "__all__"
