from django.db import models
from django.core.validators import MinLengthValidator

class reservation(models.Model):
    seat = models.CharField(max_length=30)
    date =  models.DateField()
    student = models.CharField(max_length=4, null=True)
    
