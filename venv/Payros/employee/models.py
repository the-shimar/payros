from django.db import models

# Create your models here.
class Qualification(models.Model): 
    qualification = models.CharField(max_length = 200, default = 'None')
    
    def __str__(self): 
        return self.qualification

class Employee(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=200, default = 'None' )
    name = models.CharField(max_length=200, default = 'None')
    dob = models.DateField(default='April 18, 2021')
    doj = models.DateField(default='April 18, 2021')
    address = models.TextField(default='None')
    dor = models.DateField(default='April 18, 2021')
    qualification = models.CharField(max_length = 200, default = 'None') 
    department = models.CharField(max_length=200, default = 'None')
    phone = models.CharField(max_length=200, default = 'None')
    year = models.CharField(max_length=200, default = 'None')
    month = models.CharField(max_length=200, default = 'None')
    bank_ac = models.CharField(max_length=50, default = 'None')
    
    def __str__(self): 
        return self.employee_id

        
        