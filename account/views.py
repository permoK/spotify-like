from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request ):
    return render(request, template_name="login.html")


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    
    return render(request,"register.html", {
        "form":form,
    })

def home(request):
    return render(request, template_name="index.html")

def songs(request):
    return render(request, template_name="songs.html")