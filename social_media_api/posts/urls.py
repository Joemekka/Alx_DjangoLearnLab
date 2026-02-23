from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns += [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view()),  # feed endpoint for Task 2
    path("posts/<int:pk>/like/", LikePostView.as_view()),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view()),
]
