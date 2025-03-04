from django.db import models
from django.contrib.auth.models import User

class InfoExtra (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    sobre_ti = models.CharField(null=True, blank=True,default="", max_length = 200)