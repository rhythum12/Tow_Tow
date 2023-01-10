from django.db import models
from user.models import User
# Create your models here.
class Vehicle(models.Model):
    name=models.TextField(max_length=250)
    vehicle_type=models.TextField(max_length=100)
    color=models.TextField(max_length=50)
    license_plate_no=models.TextField(max_length=250)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    