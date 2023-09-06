from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django  import forms


class CreateUserForm(UserCreationForm):
    email = forms.CharField(required=True, max_length=254)
        
    age = forms.IntegerField(max_value=100)
    day = forms.IntegerField(max_value=100)
    month = forms.IntegerField(max_value=31)
    year = forms.IntegerField(max_value=3000)
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2","age","day","year","month"]