from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Specialist(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
