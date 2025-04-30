from operator import truediv

from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    dob = models.DateField()
    weight = models.IntegerField(default=50)
    height = models.FloatField(default=1.60)
    gender = models.CharField(default="Male", max_length=20)
    class Meta:
        db_table = 'people'
