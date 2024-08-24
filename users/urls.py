from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name= "users" #добавление пространства имен (namespace) в проект

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path("profile/", profile, name="profile"),
    path("sellerprofile/<int:id>/", seller_profile, name="sellerprofile"),
]
