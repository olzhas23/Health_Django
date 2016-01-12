from django.shortcuts import render, redirect
from django.http import HttpResponse
from doctor.models import Doctor, Patient, Notes
from django.views.generic import ListView, CreateView
from .forms import PostForm
#needs refractoring
def index(req):
    return render(req,'templates/patient.html')


def search(req):
    if req.method == 'POST':
        # search by SSN last 4 digits

        SSN_ID = req.POST.get('textfield',None)
        try:
            Doctor_name = Patient.objects.get(id=SSN_ID)
            #Doctor_name_match sends as a paragraph, change to better latter
            Doctor_name_match = ('<p> %s </p>', Doctor_name)
            return HttpResponse(Doctor_name_match)
        except Doctor.DoesNotExist:
            return HttpResponse('No DR. under this SSN')
    else:
        return render(req, 'templates/index.html')

#  Doctor Page / Existing patient list

def existing_patient(req):


    return render (req, 'templates/doctor.html', {"patient_name": Patient.objects.all()})

def patient_new_record(req):

    if req.method == "POST":
        print('Add new record')
        form = PostForm(req.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:

        form = PostForm()

    return render(req,'templates/patient.html', {'form' : form})









# Create your views here.
