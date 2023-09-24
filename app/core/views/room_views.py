from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)

from core import models
from core import serializers
from core.authentication import (
    JWTAuthentication,
)
from core.permissions import (
    IsAdminOrReadOnly,
)


class RoomTypeListCreateView(APIView):
    """list of room type"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        room_type = models.RoomType.objects.all()
        serializer = serializers.RoomTypeSerializer(room_type, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomTypeRetrieveUpadteDelete(APIView):
    """room type retrieve update delete"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            room_type = models.RoomType.objects.get(pk=pk)
        except models.RoomType.DoesNotExist():
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.RoomTypeSerializer(room_type, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        room_type = models.RoomType.objects.get(pk=pk)
        serializer = serializers.RoomTypeSerializer(room_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room_type = models.RoomType.objects.get(pk=pk)
        room_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

