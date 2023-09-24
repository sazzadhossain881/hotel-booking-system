from rest_framework import serializers
from core import models


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user objects"""

    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
        fields = ["id", "name", "email", "password", "isAdmin"]
        extra_kwargs = {"password": {"write_only": True}}

    def get_isAdmin(self, obj):
        return obj.is_staff

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class HotelSerializer(serializers.ModelSerializer):
    """serializer for the hotel objects"""

    class Meta:
        model = models.Hotel
        fields = ["id", "name", "address"]


class RoomTypeSerializer(serializers.ModelSerializer):
    """serializer for the room type objects"""

    class Meta:
        model = models.RoomType
        fields = ["id", "name", "description"]


class AmenitySerializer(serializers.ModelSerializer):
    """serializer for amenity objects"""

    class Meta:
        model = models.Amenity
        fields = ["id", "name", "description"]
