from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    """

    :param request:
    :return:
    """
    return  HttpResponse('patient Portal')



# Create your views here.
