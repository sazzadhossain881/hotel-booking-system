from django.urls import path
from core.views import user_views as views

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("login/", views.LoginApiView.as_view(), name="login"),
    path("profile/", views.UserApiView.as_view(), name="profile"),
    path("users_list/", views.UsersApiView.as_view(), name="users"),
    path("users_list/<str:pk>/", views.RetrieveApiView.as_view(), name="retrieve"),
    path("update/<str:pk>/", views.UpdateApiView.as_view(), name="update"),
    path("delete/<str:pk>/", views.DeleteApiView.as_view(), name="delete"),
]
