from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='media/img/avatar.jpg', upload_to='img')


    def __str__(self):
        return str(self.user)
# Create your models here.
