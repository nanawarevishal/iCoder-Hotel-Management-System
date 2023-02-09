from asyncio.windows_events import NULL
from distutils.command.upload import upload
from turtle import home
from django.contrib.auth.models import User
from email import message
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Myfood(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=50)
    food_title = models.CharField(max_length=50)
    food_price = models.FloatField(default=0)
    food_desc = models.TextField(max_length=100)
    food_img = models.ImageField(upload_to='food/images',default="")

    def __str__(self):
        return self.food_type

class BookTable(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    msg = models.TextField(max_length=150)
    no_of_people = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class contact(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    msg = models.TextField(max_length=150)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    # food_id = models.ForeignKey(Myfood,on_delete=models.CASCADE)
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=12)
    address = models.TextField(max_length=100)
    food_type = models.CharField(max_length=50,default=NULL)
    food_title = models.CharField(max_length=50,default=NULL)
    food_price = models.FloatField(default=0)
    food_desc = models.TextField(max_length=100,default=NULL)
    # food_img = models.ImageField(upload_to='food/images',default="")
    no_ofDish = models.IntegerField(max_length=50)
    msg = models.TextField(max_length=100)
    # orderdetails = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
