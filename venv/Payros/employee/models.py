from django.db import models

# Create your models here.


class Qualification(models.Model): 
    qualification = models.CharField(max_length = 200, default = 'None')
    
    def __str__(self): 
        return self.qualification

class Employee(models.Model):
    employee_id = models.CharField(max_length=200, default = 'None' )
    name = models.CharField(max_length=200, default = 'None')
    dob = models.DateTimeField(default = 'None')
    doj = models.DateTimeField(default = 'None')
    address = models.TextField(default='None')
    dor = models.DateTimeField(default = 'None')
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    department = models.CharField(max_length=200, default = 'None')
    phone = models.CharField(max_length=200, default = 'None')
    year = models.CharField(max_length=200, default = 'None')
    month = models.CharField(max_length=200, default = 'None')
    
    def __str__(self): 
        return self.employee_id
        