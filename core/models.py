from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy
from django.conf import  settings

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(('email_address'),unique= True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email','first_name','last_name']
    def __str__(self):
        return "{}".format(self.email)