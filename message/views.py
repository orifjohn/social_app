from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.shortcuts import render
from .models import Message, Chat
from common.models import User
from rest_framework import generics
from .serializers import MessageViewSerializer, ChatViewSerializer, MessageCreateSerializer
from helpers.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated


class MessageView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = MessageViewSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get("chat_id", None):
            queryset = queryset.filter(chat=self.kwargs["chat_id"])
        return queryset


class ChatView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatViewSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.all().filter(members=user)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
