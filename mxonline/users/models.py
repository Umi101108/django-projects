from __future__ import unicode_literals

from django.db import models
from django.conf.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=)
