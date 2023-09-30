from django.urls import path
from django.contrib.auth.decorators import user_passes_test, login_required
from . import views

urlpatterns = [
    path("",views.deco (views.home), name= "home"),
    path("login/",views.deco (views.login_user), name= "login"),
    path("register/", views.deco(views.register_user), name= "register"),
    path("songs/", (views.songs), name="songs"),
    path("logout/", (views.logout_user),name="logout"),
    path("search/", (views.search), name="search"),

]
