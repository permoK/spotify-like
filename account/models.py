from django.db import models

# Create your models here.

class Artist(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    Age = models.IntegerField()
    password = models.CharField(max_length=10)
    

    def __str__(self):
        return self.firstname + " " + self.lastname
