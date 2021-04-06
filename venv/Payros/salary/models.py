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