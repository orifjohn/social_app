from django.db import models
from common.models import User
from helpers.models import BaseModel


# Create your models here.


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    context = models.TextField()
    like_count = models.PositiveBigIntegerField()
    view_count = models.PositiveBigIntegerField()

    def count_view(self, id):
        post = Post.objects.get(id=id)
        post.view_count += 1
        post.save()
