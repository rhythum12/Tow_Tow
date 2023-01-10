from django.db import models
from user.models import  User
from vehicle.models import Vehicle




# Create your models here.
class Servicing(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    vehicle_name=models.TextField(max_length=250,default="",null=True)
    vehicle_type=models.TextField(max_length=100,default="",null=True)
    color=models.TextField(max_length=50,default="",null=True)
    license_plate_no=models.TextField(max_length=250,default="",null=True)
    latitude=models.FloatField(default=0.0,null=True)
    longitude=models.FloatField(default=0.0,null=True)
    pick_up_date=models.TextField()
    status=models.TextField()
    

    