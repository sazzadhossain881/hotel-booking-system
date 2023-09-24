from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.decorators import permission_classes
from core import models
from core import serializers

from django.contrib.auth.hashers import make_password

from core.authentication import (
    create_access_token,
    create_refresh_token,
    JWTAuthentication,
)
import datetime


class RegisterApiView(APIView):
    """register user in the system"""

    def post(self, request):
        data = request.data
        try:
            user = models.User.objects.create(
                email=data["email"],
                name=data["name"],
                password=make_password(data["password"]),
            )
            serializer = serializers.UserSerializer(user, many=False)
            return Response(serializer.data)
        except:
            message = {"detail": "user with this email already exists"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):
    """login user in the system"""

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = models.User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("invalid credentials")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("invalid credentials")

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        models.UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expire_at=datetime.datetime.utcnow() + datetime.timedelta(days=7),
        )

        response = Response()
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.data = {
            "token": access_token,
            "email": user.email,
            "name": user.name,
            "isAdmin": user.is_staff,
        }

        return response


class UserApiView(APIView):
    """user api view"""

    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(serializers.UserSerializer(request.user).data)


class UsersApiView(APIView):
    """users api view"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        user = models.User.objects.all()
        serializer = serializers.UserSerializer(user, many=True)
        return Response(serializer.data)


class RetrieveApiView(APIView):
    """retrieve specific user"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            user = models.User.objects.get(pk=pk)
        except models.User.DoesNotExist():
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.UserSerializer(user, many=False)
        return Response(serializer.data)


class UpdateApiView(APIView):
    """update user"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = models.User.objects.get(pk=pk)
        data = request.data

        user.name = data["name"]
        user.email = data["email"]
        user.is_staff = data["isAdmin"]

        user.save()

        serializer = serializers.UserSerializer(user, many=False)
        return Response(serializer.data)


class DeleteApiView(APIView):
    """delete user"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        user = models.User.objects.get(pk=pk)
        user.delete()
        return Response("user was deleted")
