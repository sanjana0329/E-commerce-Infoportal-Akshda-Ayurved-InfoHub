from accounts.models import CustomUser
import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"
