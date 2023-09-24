from django.urls import path
from core.views import hotel_views as views

urlpatterns = [
    path("hotel_list/", views.HotelListCreateView.as_view(), name="hotel-list"),
    path(
        "hotel_list/<str:pk>/",
        views.HotelRetrieveUpdateDeleteView.as_view(),
        name="hotel-retrieve-update-delete",
    ),
  
]
