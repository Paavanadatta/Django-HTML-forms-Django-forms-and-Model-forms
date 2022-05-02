from django.db import models
from datetime import datetime

# Create your models here.

class enqmodel(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    email=models.EmailField()
    desc=models.TextField()
    date=models.DateTimeField(default=datetime.now())
