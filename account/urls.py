from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path("login/", views.login_user, name= "login"),
    path("register/", views.register_user, name= "register"),
    path("songs/", views.songs, name="songs"),
    path("logout/", views.logout_user,name="logout"),
]