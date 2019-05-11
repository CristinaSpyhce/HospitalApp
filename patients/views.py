from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Doctor, Patient
from django.template import loader,RequestContext
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect

# Create your views here.
def doctors(request):
    doctors_list=Doctor.objects.all()
    template=loader.get_template("patients/doctors_details.html")
    context={
        'doctors_list':doctors_list
    }
    return HttpResponse(template.render(context))

def message(request):
    print("Login successful")
    return HttpResponseRedirect('patients/message/')

def patients_names(request,doctor_id):
    doctor=Doctor.objects.get(pk=doctor_id)
    template=loader.get_template('patients/patients_names.html')
    context={'doctor':doctor}
    return HttpResponse(template.render(context))

def patients_details(request,doctor_id, patient_id):
    patient=Patient.objects.get(pk=patient_id)
    template=loader.get_template('patients/patients_details.html')
    context = {'patient': patient}
    return HttpResponse(template.render(context))