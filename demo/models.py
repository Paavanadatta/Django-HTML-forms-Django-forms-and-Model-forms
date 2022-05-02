from django.db import models

# Create your models here.
class registermodel(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()