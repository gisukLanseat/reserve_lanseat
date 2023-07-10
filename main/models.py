from django.db import models
from django.core.validators import MinLengthValidator

class reservation(models.Model):
    seat = models.CharField(max_length=30)
    date =  models.DateField()
    student = models.CharField(max_length=8, null=True)
    class Meta:
        app_label = 'main'
