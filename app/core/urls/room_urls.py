from django.urls import path
from core.views import room_views as views

urlpatterns = [
    path("room_type/", views.RoomTypeListCreateView.as_view(), name="room-type-list"),
    path(
        "room_type/<str:pk>/",
        views.RoomTypeRetrieveUpadteDelete.as_view(),
        name="room-type-retrieve-update-delete",
    ),
]
