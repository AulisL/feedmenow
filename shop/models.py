from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # own model for User, so it can be easily changed
    # new fields will be added later
    #name = models.CharField(max_length=256)
    #nick = models.CharField(max_length=256)
    pass