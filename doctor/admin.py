from django.contrib import admin
from .models import Doctor,Patient


class Doctor_ID(admin.ModelAdmin):

    list_display = ('FIRSTNAME', 'LASTNAME' , 'SSN')
    list_filter =('FIRSTNAME', 'LASTNAME' , 'SSN')
    search_fields =('FIRSTNAME', 'LASTNAME' , 'SSN')

class Patient_ID(admin.ModelAdmin):
    list_display = ('FIRSTNAME', 'LASTNAME' , 'SSN','INSURANCE','DOCTOR')
    list_filter =('FIRSTNAME', 'LASTNAME' , 'SSN')
    search_fields =('LASTNAME' , 'SSN')



admin.site.register(Doctor, Doctor_ID)
admin.site.register(Patient,Patient_ID)






# Register your models here.
