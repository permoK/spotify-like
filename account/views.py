from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required, user_passes_test

from django.utils import timezone
import datetime
from django.contrib import messages
from .forms import CreateUserForm

#spotify api
from sp

# Create your views here.

def login_user(request):

    if request.method == "POST":
        username = (request.POST.get('username')).lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("songs")
        else:
            messages.error(request, "Invalid Username or password")

    return render(request, template_name="login.html")


def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("username")
            messages.success(request, "account created succesfully")
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request,"register.html", {
        "form":form,
    })

def home(request):
    return render(request, template_name="index.html")
@login_required(login_url='login')
def songs(request):
    time = datetime.datetime.now()
    ctime = time.hour
    ntime = ""
    if ctime <= 11:
        ntime = "good morning"
    elif ctime < 17:
        ntime = "good afternoon"
    else:
        ntime = "good evening"
    return render(request,"songs.html",{
        "time": ntime
    })

def logout_user(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect("login")


def is_user_logged_out(user):
    return not user.is_authenticated

#logout required to access some pages
deco = user_passes_test(is_user_logged_out, login_url='songs')
