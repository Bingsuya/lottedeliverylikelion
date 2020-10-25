from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 30 ,null = True, default = True)
    phone = models.CharField(max_length = 30, null = True, default = True)
    address = models.CharField(max_length = 100, null = True, default = True)

