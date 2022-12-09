from django.db import models

# Create your models here.
class db123(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=35)
    esal = models.IntegerField()
    eaddr = models.TextField()

