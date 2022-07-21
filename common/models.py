# from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models

# from django.utils import timezone

MALE = 'male'
FEMALE = 'female'

GENDER_STATUS = (
    (MALE, 'male'),
    (FEMALE, 'female'),
)


class User(AbstractUser):
    full_name = models.CharField(("full name"), max_length=256)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        }
    )
    created_at = models.DateTimeField(("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)

    image = models.FileField(upload_to='avatars/', null=True, blank=True)

    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    job = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)

    website = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_STATUS, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)

    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instgram = models.CharField(max_length=50, null=True, blank=True)
    linkedln = models.CharField(max_length=50, null=True, blank=True)

    is_online = models.BooleanField(default=False)
    block_user = models.ManyToManyField('self', related_name='block_users', null=True,
                                        blank=True)
    follower = models.ManyToManyField('self', related_name='followss', symmetrical=False, null=True, blank=True)
    following = models.ManyToManyField('self', related_name='followerss', symmetrical=False, null=True, blank=True)

    follower_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)

    enter_date = models.DateTimeField(null=True, blank=True)
    exit_date = models.DateTimeField(null=True, blank=True)

    # SETTINGS
    # USERNAME_FIELD = "username"
    first_name = None
    last_name = None

    # REQUIRED_FIELDS = ["email", "full_name"]

    def __str__(self):
        return f"{self.email}"

    def follow(self, user):
        self.follower.add(user)
        self.follower_count += 1
        user.following.add(self)
        user.following_count += 1
        self.save()
        user.save()

    def unfollow(self, user):
        self.follower.remove(user)
        self.follower_count -= 1
        user.following.remove(self)
        user.following_count -= 1
        self.save()
        user.save()

    def blocked_user(self, user):
        self.block_user.add(user)
        self.save()

    def unblocked_user(self, user):
        self.block_user.remove(user)
        self.save()

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")
