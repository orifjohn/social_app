from django.contrib import admin
from django.urls import path, include
from message.views import MessageView, ChatView, MessageCreateView, CustomAuthToken
from rest_framework.authtoken import views

urlpatterns = [
    path("chat/", ChatView.as_view()),
    path("message/<int:chat_id>/", MessageView.as_view()),
    path("message/create", MessageCreateView.as_view()),
    # path('api-token-auth/', views.obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view())
]
