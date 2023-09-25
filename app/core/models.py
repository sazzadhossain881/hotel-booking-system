from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """manage user in the system"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("user must have an email address")

        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """user in the system"""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_short_name(self):
        """retrieve short name of the user"""
        return self.name

    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def __str__(self):
        """string representation of the user"""
        return self.email


class UserToken(models.Model):
    """user token objects"""

    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()


class Hotel(models.Model):
    """Hotel objects"""

    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class RoomType(models.Model):
    """room type objects"""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    """amenity objects"""

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    """room objects"""

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    equipments = models.ManyToManyField("Amenity", related_name="room_equipments")
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    """room amenities object"""

    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(null=True)
