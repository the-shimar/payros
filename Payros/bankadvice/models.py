from django.db import models
from employee.models import Employee

# Create your models here.
class BankAdvice(models.Model):
    emp_id = models.CharField(primary_key=True,max_length=200, default='None')
    account_number = models.CharField(max_length=200, default='None')
    emp_name = models.CharField(max_length=200, default='None')
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.emp_name
