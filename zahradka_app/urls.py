from django.urls import path
# from . import views
from .views import homepage, RegistrationView, LoginView, LogoutView, ChangePasswordView, garden_detail, garden, \
    update_garden, delete_garden, contact, create_garden

urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("garden/", garden, name="garden"),
    path("garden/<int:garden_id>/", garden_detail, name="garden_detail"),
    #path("settings/<str:garden_name>/", GardenSettingsView.as_view, name="garden_settings"),
    path("create_garden/", create_garden, name="create_garden"),
    path("garden/<int:garden_id>/update_garden/", update_garden, name="update_garden"),
    path("garden/<int:garden_id>/delete_garden/", delete_garden, name="delete_garden"),
    path("contact", contact, name="contact"),
]