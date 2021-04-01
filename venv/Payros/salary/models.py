from django.db import models
import datetime

# Create your models here.

class Salary(models.Model):
    name = models.CharField(max_length=200, default = 'None')
    year = models.IntegerField(default=0)
    qualification = models.ForeignKey('employee.Qualification', on_delete=models.CASCADE)
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

    def __str__(self): 
        return self.name

class Approve(models.Model):
    employee_id = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    name = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    net_salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    increments = models.ForeignKey(Salary, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default = 'None')
    
