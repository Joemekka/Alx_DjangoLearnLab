from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class FollowUserView(APIView):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        request.user.following.add(user)
        return Response({"detail": "followed"})


class UnfollowUserView(APIView):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        request.user.following.remove(user)
        return Response({"detail": "unfollowed"})
