from django.contrib import admin
from django.urls import path, include
from .views import JobList
from rest_framework.authtoken import views

urlpatterns = [
    path("job/", JobList.as_view())
]