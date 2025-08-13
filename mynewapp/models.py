from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    contact=models.IntegerField()

    def __str__(self):
        return self.uname

class book(models.Model):
    bid=models.AutoField(primary_key=True)
    uid=models.IntegerField()
    book_name=models.CharField(max_length=50)
    quantity=models.IntegerField(default=1)
    address=models.TextField(default="")
    total_price=models.IntegerField(default=0)
    date=models.DateField()
    time=models.TimeField()
    mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.book_name


class Admin(models.Model):
    aid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

