from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    special_conditions = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Condition(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return str(self.patient)
