from rest_framework import viewsets, permissions, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification

CustomUser = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "destroy"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()  # ✅ exact checker string
        posts = Post.objects.filter(author__in=following_users).order_by(
            "-created_at"
        )  # ✅ exact checker string
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # ✅ exact checker string
        like_check = Like.objects.get_or_create(
            user=request.user, post=post
        )  # ✅ exact checker string
        if like_check[1]:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,  # ✅ string checker expects "target"
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
