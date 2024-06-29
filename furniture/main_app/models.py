from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class User_table(User):
    firstname=models.CharField(max_length=255,default=None)
    lastname=models.CharField(max_length=255,default=None)
    Address=models.TextField(default=None)
    


class cart_table(models.Model):
    name=models.CharField(max_length=255)
    Total_price=models.IntegerField()
    rate=models.IntegerField()
    starting_date=models.DateField()
    ending_date=models.DateField()
    user=models.CharField(max_length=255)