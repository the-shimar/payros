from django.db import models
import datetime

# Create your models here.
class Approve(models.Model):
    employee_id = models.CharField(max_length=200, default='None')
    name = models.CharField(max_length=200, default='None')
    net_salary = models.IntegerField(default=0)
    increments = models.IntegerField(default=0)
    status = models.CharField(max_length=200, default = 'None')

    def __str__(self):
        return self.employee_id

class Bills(models.Model):
    employee_id = models.CharField(max_length=200, default='None')
    name = models.CharField(max_length=200, default='None')
    net_salary = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee_id

class EmployeeSalaryDetails(models.Model):
    emp_id = models.CharField(max_length=100, default='None')
    generated_date = models.CharField(max_length=10, default='None')
    qualification = models.CharField(max_length=200, default='None') 
    year = models.IntegerField(default=0)
    present_days = models.IntegerField(default=0)
    llp = models.IntegerField(default=0)
    basic = models.IntegerField(default=0)
    ma = models.IntegerField(default=0)
    cca = models.IntegerField(default=0)
    allow_total = models.IntegerField(default=0)
    epf = models.IntegerField(default=0)
    esi = models.IntegerField(default=0)
    rbs = models.IntegerField(default=0)
    llp1 = models.IntegerField(default=0)
    society = models.IntegerField(default=0)
    sarvodhaya = models.IntegerField(default=0)
    hra = models.IntegerField(default=0)
    fa = models.IntegerField(default=0)
    sa = models.IntegerField(default=0)
    det_total = models.IntegerField(default=0)
    net_salary = models.IntegerField(default=0)
    increments = models.IntegerField(default=0)
    da = models.IntegerField(default=0)

    def __str__(self): 
        return self.emp_id