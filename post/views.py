from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import PostViewSerializer
from .models import Post
from helpers.pagination import CustomPagination
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin
from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class PostCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = PostViewSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostViewSerializer

    def put(self, request, *args, **kwargs):
        # post = self.queryset.get(id=kwargs.get("pk"))
        # post.count += 1
        # post.save()
        return self.partial_update(request, *args, **kwargs)

