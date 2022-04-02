from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',)
    profile_picture = models.ImageField(upload_to = 'images/')
    name = models.CharField(blank=True, max_lenght = 120)
    location = models.CharField(max_length=60, blank=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'