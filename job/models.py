from django.db import models
from helpers.models import BaseModel

REGION = (
    ("toshkent", "toshkent"),
    ("samarqand", "samarqand")
)

STATUS = (
    ("premium", "premium"),
    ("urgant", "urgant"),
    ("basic", "basic")
)
#
# TIME = (
#     ("24 soat", "24 soat"),
#     ("3 kun", "3 kun"),
#     ("7 kun", "7 kun"),
#     ("butun vaqt", "butun vaqt"),
# )
# SALARY = (
#     ("3 million", "3 milliongacha"),
#     ("3 - 7 ", "3 - 7"),
#     ("7 -15", "7 -15"),
#     ("15 <<<< ", "15 <<<<<"),
# )


class Job(BaseModel):
    title = models.CharField(max_length=256)
    context = models.TextField()
    time = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=20)
    status = models.CharField(max_length=20, blank=True, null=True)
    salary = models.CharField(max_length=20, blank=True, null=True)
