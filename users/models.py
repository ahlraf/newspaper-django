from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    # null = database related. when field has null=True,
    # it can store a database entry as null
    # blank = validation related. if blank=true, then the
    # form allways empty value
