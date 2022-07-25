from .models import Post
from rest_framework import serializers


class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "user", "like_count", "context",)
