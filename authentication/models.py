from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(default='media/img/avatar.jpg', upload_to='img')

    def __str__(self):
        return str(self.user)