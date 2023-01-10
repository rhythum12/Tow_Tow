from django.db import models

# Create your models here.
class Workshop(models.Model):
    workshop_name=models.TextField()
    latitude=models.FloatField()
    longitude=models.FloatField()