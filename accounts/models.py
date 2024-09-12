from email.policy import default
from enum import unique
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,AbstractUser,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from django.apps import apps


USER_TYPES=[
    ('ADMIN', 'admin'),
    ('USER', 'user'),
    
]
class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=50,null=True,blank=True)
    lastname = models.CharField(max_length=50,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    type = models.CharField(max_length=10,choices=USER_TYPES,null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField("Date and time", auto_now_add=True,null=True)
    status = models.BooleanField(default=False, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return_str = None
        if self.username:
            return_str = self.username
        else:
            return_str = self.email
        return return_str

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def get_initials(self):
        if not self.username:
            return ""
        parts = self.username.split()
        initials = "".join([part[0].upper() for part in parts])
        return initials
