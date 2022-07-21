from rest_framework import serializers
from .models import Chat, Message
from common.models import User


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ChatViewSerializer(serializers.ModelSerializer):
    members = UserViewSerializer(many=True)

    class Meta:
        model = Chat
        fields = "__all__"


class MessageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MessageCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        print(self.context["request"].user)
        if self.context["request"].user in data["chat"].members.all():
            return data
        raise serializers.ValidationError("siz bu chatga message jo'nata olmaysiz")

    class Meta:
        model = Message
        fields = "__all__"
