from django.db import models

from user.models import User
# Create your models here.

# Create your models here.
class Billbook(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.DO_NOTHING)
    bill_book_no=models.TextField(max_length=150)
    latitude=models.FloatField(default=0.0)
    longitude=models.FloatField(default=0.0)
    pick_up_date=models.TextField()
    status=models.TextField()