from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django import forms


class Doctor(models.Model):


    FIRSTNAME = models.CharField(max_length=40)
    LASTNAME = models.CharField (max_length=40)
    MIDLLENAME = models.CharField(max_length=40)
    DOB = models.DateField(max_length=8)
    SSN = models.IntegerField(4)

    @property
    def Doctor_ID(self):
        return self.ID
    def __unicode__(self):
        return "%s %s" ' Id: ' "%s" %(self.FIRSTNAME,self.LASTNAME)

class Patient(models.Model):


    DOCTOR = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    FIRSTNAME = models.CharField(max_length=40)
    LASTNAME = models.CharField(max_length=40)
    MIDLLENAME = models.CharField(max_length=40)
    DOB = models.DateField()
    SSN = models.IntegerField()
    EMAIL = models.EmailField('Email Address:',max_length=100)
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

    @property
    def Patient_ID(self):
        return self.ID

    def __unicode__(self):

        return  (self.FIRSTNAME,self.LASTNAME, self.DOB,self.SSN,self.INSURANCE)

# Notes is a class that is used by doctors and patients

class Notes(forms.Form):

    Doctor_Info = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient_Info = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Notes = forms.Textarea()
    TimeStamp = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):

        return (self.Notes)





# Create your models here.
