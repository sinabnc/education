from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=133)
    email=models.EmailField()
    phone=models.IntegerField()



