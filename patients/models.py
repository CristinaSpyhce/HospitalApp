from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

#class Profile(models.Model):
    #user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    #doctor_name=models.ForeignKey(Doctor,on_delete=models.CASCADE, null=False)

class Patient(models.Model):
    pacient_type= [('C','Child'),('A','Adult')]
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    diagnostic=models.CharField(max_length=50)
    no_appointments=models.IntegerField(default=0)
    prescribed_treatment=models.CharField(max_length=50)
    child_or_not=models.CharField(max_length=10,default='A',choices=pacient_type)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name