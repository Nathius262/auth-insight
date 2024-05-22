from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission
from .manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=250, unique=True)
    username = models.CharField(verbose_name="username", max_length=250, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=250)
    last_name = models.CharField(verbose_name="last name", max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_all_permissions(self, obj=None):
        # Get permissions based on email and username
        email_permissions = Permission.objects.filter(name=self.email)
        # username_permissions = Permission.objects.filter(username=self.username)

        # Combine the permissions
        all_permissions = email_permissions  # | username_permissions

        return all_permissions


class LoginRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.ip_address} - {self.timestamp}'
