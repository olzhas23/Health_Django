__author__ = 'Olzhas'
from django import forms

from .models import Patient,Doctor, Notes

class PostForm(forms.ModelForm):

    class Meta:

        model = Patient
        #add notes latter
        doctor_rec = Notes
        fields = ('FIRSTNAME', 'LASTNAME','NOTES')


