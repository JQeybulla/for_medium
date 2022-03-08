from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField(_('email address'), blank=True, unique=True)
    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'
    def save(self, *args, **kwargs): 
        self.username = self.email
        return super().save(*args, **kwargs)
