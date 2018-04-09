from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=32)
    comp = models.CharField(max_length=32,default='Title')
    low = models.IntegerField()
    high = models.IntegerField()
    pos = models.CharField(max_length=32,default='Title')
    addr = models.CharField(max_length=32,default='Title')
    site = models.CharField(max_length=32,default='Title')
    status = models.IntegerField()
    
class TotalInfo(models.Model):
    name = models.CharField(max_length=32)
    avg_low = models.IntegerField()
    avg_high = models.IntegerField()
    site = models.CharField(max_length=32)
    count = models.IntegerField()