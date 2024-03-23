from django.db import models

from django.contrib.auth.models import User 

class eZy_users(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    uname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    class Meta:
        db_table = 'eZy_users'