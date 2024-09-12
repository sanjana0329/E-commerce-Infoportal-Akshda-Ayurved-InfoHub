from django.core.mail import send_mail
from django.conf import settings

def send_admin_mail(subject, message):
    """
    Send an email to the admin.
    """
    admin_email = settings.ADMIN_EMAIL
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [admin_email],
        fail_silently=False,
    )

def send_user_mail(subject, message, user_email):
    """
    Send an email to a user.
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )