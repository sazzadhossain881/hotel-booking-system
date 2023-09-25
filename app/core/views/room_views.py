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


class AmenityListCreateView(APIView):
    """list of amenity"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        amenity = models.Amenity.objects.all()
        serializer = serializers.AmenitySerializer(amenity, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.AmenitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AmenityRetrieveUpdateDeleteView(APIView):
    """amenity retrieve update delete"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            amenity = models.Amenity.objects.get(pk=pk)
        except models.Amenity.DoesNotExist():
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.AmenitySerializer(amenity, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = models.Amenity.objects.get(pk=pk)
        serializer = serializers.AmenitySerializer(amenity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        amenity = models.Amenity.objects.get(pk=pk)
        amenity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomListCreateView(APIView):
    """list of room"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        room = models.Room.objects.all()
        serializer = serializers.RoomSerializer(room, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomRetrieveUpdateDeleteView(APIView):
    """room  retrieve update delete"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            room = models.Room.objects.get(pk=pk)
        except models.Room.DoesNotExist():
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.RoomSerializer(room, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        room = models.Room.objects.get(pk=pk)
        serializer = serializers.RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room = models.Room.objects.get(pk=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentListCreateView(APIView):
    """List of equiment"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        equipment = models.Equipment.objects.all()
        serializer = serializers.EquipmentSerializer(equipment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class EquipmentRetrieveUpdateDeleteView(APIView):
    """equipment retrieve update delete view"""

    def get(self, request, pk):
        try:
            equipment = models.Equipment.objects.get(pk=pk)
        except models.Equipment.DoesNotExist():
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.EquipmentSerializer(equipment, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        equipment = models.Equipment.objects.get(pk=pk)
        serializer = serializers.EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        equipment = models.Equipment.objects.get(pk=pk)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
