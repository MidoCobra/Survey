from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Role(models.Model):
    role = models.CharField(max_length=100,blank=False, unique=True)
    def __str__(self):
        return self.role



class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=110, null=True)
    email = models.EmailField(_("email address"), unique=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, blank=False, related_name="user_role", null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email