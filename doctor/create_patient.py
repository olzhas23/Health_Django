__author__ = 'Olzhas'
from django.shortcuts import render
from django.http import HttpResponse
from doctor.models import Doctor, Patient

# View for create_patient

def page(req):
  error = False

  if req.POST:
    if 'name' in req.POST:
        name = req.POST.get('name', '')

    else:
      error=True
    if 'login' in req.POST:
      login = req.POST.get('login', '')
    else:
      error=True
  if 'password' in req.POST:
      password = req.POST.get('password', '')
    else:
      error=True
    if 'doctor' in req.POST:
      doctor_id = req.POST.get('doctor', '')
    else:
      error=True
    if not error:

      doctor = doctor.objects.get(id = doctor_id)
      new_patient = patient(FIRSTNAME=f_name, LASTNAME=l_name)
      new_patient.save()
      return HttpResponse("New Patient added")
    else:
      return HttpResponse("N/A")
  else:
    #change file
    patient_list = Doctor.objects.all()
    return render(request, 'newnew.html')
