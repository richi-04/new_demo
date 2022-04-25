from random import choices
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm




genderChoices = [('F','Female'), ('M','Male')]
# hobby = [('1','Music'),('2','Art'),('3','Dance'),('4','Singing'),('5','Reading')]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    contact = models.IntegerField()
    gender = models.CharField(max_length=10, choices=genderChoices, default='female')
    # hobby = models.CharField(max_length=3, choices=hobby)

 