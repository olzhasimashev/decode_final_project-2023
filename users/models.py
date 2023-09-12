from django.contrib.auth.hashers import is_password_usable, make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        if self.pk is None or not is_password_usable(self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
