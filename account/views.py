from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def login_user(request ):
    return render(request, template_name="login.html")


def register_user(request):
    return render(request, template_name="register.html")

def home(request):
    return render(request, template_name="index.html")

def songs(request):
    return render(request, template_name="songs.html")