from django.contrib.auth.models import User

from django.db import models
from common.models import User
from helpers.models import BaseModel


# Create your models here.


class Chat(BaseModel):
    members = models.ManyToManyField(User)
    is_group = models.BooleanField(default=False)

    def set_is_group(self):
        n = self.members.count()
        if n >= 1:
            self.is_group = True
        return self.is_group


class Message(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
