from django.db import models

class User(models.Model):
    uid=models.TextField(max_length=500)
    fullname=models.TextField(max_length=100)
    email=models.TextField(max_length=100)

