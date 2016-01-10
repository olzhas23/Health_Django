from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

class Doctor(models.Model):

    ID = models.AutoField(primary_key= True, max_length=10)
    FIRSTNAME = models.CharField(max_length=40)
    LASTNAME = models.CharField (max_length=40)
    MIDLLENAME = models.CharField(max_length=40)
    DOB = models.DateField(max_length=8)
    SSN = models.IntegerField(4)

    def __str__(self):
        return "%s %s" ' Id: ' "%s" %(self.FIRSTNAME,self.LASTNAME,self.ID)

class Patient(models.Model):


    DOCTOR = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    FIRSTNAME = models.CharField(max_length=40)
    LASTNAME = models.CharField(max_length=40)
    MIDLLENAME = models.CharField(max_length=40)
    DOB = models.DateField()
    SSN = models.IntegerField()
    EMAIL = models.CharField('Email Address:',max_length=100)
    NUMBER = models.IntegerField()
    STREET = models.CharField('Street:',max_length=100)
    CITY = models.CharField('City:',max_length=100)
    STATE = models.CharField('State:',max_length=2)
    ZIP = models.IntegerField()
    PHONE = models.IntegerField()
    INSURANCE_CHOICES = (
        ('VHCP', 'Veterans Health Care Program'),
        ('CHAMPVA', 'CHAMPVA'),
        ('TRICARE', 'TRICARE'),
        ('NONE', 'NONE'),
    )
    INSURANCE = models.CharField(max_length=50,choices=INSURANCE_CHOICES)

    def __unicode__(self):
        print (self.INSURANCE)
        return  (self.FIRSTNAME,self.LASTNAME, self.DOB,self.SSN,self.INSURANCE)

# Create your models here.
