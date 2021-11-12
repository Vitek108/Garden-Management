from django.urls import path
from . import views
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView, garden_detail, garden

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("garden/", garden, name="garden"),
    path("garden/<str:garden_name>/", garden_detail, name="garden_detail"),
    #path("settings/<str:garden_name>/", GardenSettingsView.as_view, name="garden_settings"),
    path("create_garden/", views.create_garden, name="create_garden"),
    path("update_garden/<str:garden_name>/", views.update_garden, name="update_garden"),
    path("delete_garden/<str:garden_name>/", views.delete_garden, name="delete_garden"),
]