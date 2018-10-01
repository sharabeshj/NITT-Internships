from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name = 'profile', on_delete = models.CASCADE)
    interned = models.BooleanField(default = False)
    resume = models.FileField(null = True)
    cover_letter = models.FileField(null = True)
    lor = modes.FileField(null = True)


