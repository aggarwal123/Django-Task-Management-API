from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    name = models.CharField(_("full name"), max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    mobile = models.CharField(_("mobile number"), max_length=15, unique=True)

    # prevents the conflict with Django’s default auth.User.groups
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    # prevents the conflict with Django’s default auth.User.user_permissions
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    USERNAME_FIELD = "email"  # Use email for authentication instead of username
    REQUIRED_FIELDS = ["name", "username", "mobile"]

    def __str__(self):
        return self.email


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    
    def __str__(self):
        return self.name