from django.db import models

# Create your models here.
class todo(models.Model):
    name= models.CharField(max_length=255)
    desc = models.CharField(max_length=500)