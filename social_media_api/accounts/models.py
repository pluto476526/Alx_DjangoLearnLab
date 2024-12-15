from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='my_followers')
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='my_following')

    def __str__(self):
        return self.username
