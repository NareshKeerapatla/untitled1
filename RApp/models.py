from django.db import models

class Reg(models.Model):
    User=models.CharField(max_length=20)
    Pwd=models.CharField(max_length=10)
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    Dob=models.DateField()
    Mob=models.IntegerField()
