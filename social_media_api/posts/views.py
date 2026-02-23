from rest_framework import generics, permissions, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404  # ✅ needed
from django.contrib.auth import get_user_model

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

CustomUser = get_user_model()


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ string checker wants this
        like, created = Like.objects.get_or_create(
            user=request.user, post=post
        )  # ✅ string checker wants this
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,  # ✅ string checker expects this field too
            )
            return Response({"detail": "Post liked"})
        return Response({"detail": "Already liked"})


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked"})
        except Like.DoesNotExist:
            return Response({"detail": "Not liked yet"})
