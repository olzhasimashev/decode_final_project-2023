from django.db import models
from specialists.models import Specialist
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
class Procedure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, related_name="created_procedures")
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="booked_procedures")

    def __str__(self):
        return self.name
