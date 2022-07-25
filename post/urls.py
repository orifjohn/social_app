from django.urls import path, include
from .views import PostCreateView, PostUpdateView

urlpatterns = [
    # path("post/", PostListView.as_view()),
    path("postcreate/", PostCreateView.as_view()),
    path("postupdate/<int:pk>/", PostUpdateView.as_view(), name='post_partial_update')
]
