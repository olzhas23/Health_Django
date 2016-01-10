from django.shortcuts import render
from django.http import HttpResponse
from doctor.models import Doctor, Patient
from django.views.generic import ListView, CreateView

def index(response):
    return HttpResponse('Doctor Portal')


def doctors(k):
    return  HttpResponse('List of Doctors')

class Docotor_Info (ListView):
    model = Doctor
    doctors_list = 'doctors_list.html'



# Create your views here.
