from django.urls import path
from core.views import room_views as views

urlpatterns = [
    path("room_type/", views.RoomTypeListCreateView.as_view(), name="room-type-list"),
    path(
        "room_type/<str:pk>/",
        views.RoomTypeRetrieveUpadteDelete.as_view(),
        name="room-type-retrieve-update-delete",
    ),
    path("amenity/", views.AmenityListCreateView.as_view(), name="amenity-list"),
    path(
        "amenity/<str:pk>/",
        views.AmenityRetrieveUpdateDeleteView.as_view(),
        name="amenity-retrieve-update-delete",
    ),
    path("room/", views.RoomListCreateView.as_view(), name="room-list"),
    path(
        "room/<str:pk>/",
        views.RoomRetrieveUpdateDeleteView.as_view(),
        name="room-retrieve-update-delete",
    ),
    path("equipment/", views.EquipmentListCreateView.as_view(), name="equipment-list"),
    path(
        "equipment/<str:pk>/",
        views.EquipmentRetrieveUpdateDeleteView.as_view(),
        name="equipment-retrieve-update-delete",
    ),
]
