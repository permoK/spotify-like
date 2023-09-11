from django.urls import path
from django.contrib.auth.decorators import user_passes_test, login_required
from . import views

urlpatterns = [
    path("",user_passes_test(views.is_user_logged_out, login_url='songs') (views.home), name= "home"),
    path("login/", views.login_user, name= "login"),
    path("register/", views.register_user, name= "register"),
    path("songs/", views.songs, name="songs"),
    path("logout/", views.logout_user,name="logout"),
]