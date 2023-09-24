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


class HotelListCreateView(APIView):
    """List of hotels"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request):
        hotel = models.Hotel.objects.all()
        serializer = serializers.HotelSerializer(hotel, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class HotelRetrieveUpdateDeleteView(APIView):
    """retrieve update delete hotel"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

    def get(self, request, pk):
        try:
            hotel = models.Hotel.objects.get(pk=pk)
        except models.Hotel.DoesNotExist():
            return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.HotelSerializer(hotel, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        hotel = models.Hotel.objects.get(pk=pk)
        serializer = serializers.HotelSerializer(hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hotel = models.Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


