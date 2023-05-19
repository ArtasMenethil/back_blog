from django.db import models
from .manager import UserManager
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="Имя пользователя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия пользователя", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

