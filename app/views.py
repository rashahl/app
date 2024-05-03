from django.shortcuts import render

# Create your views here.
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})
