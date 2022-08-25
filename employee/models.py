from django.contrib.auth.models import AbstractUser
from django.db import models

from employee.managers import CustomUserManager
from restaurant.models import Menu


class Employee(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Vote(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
