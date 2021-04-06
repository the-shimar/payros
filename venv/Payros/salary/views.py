from django.shortcuts import redirect, render
from .models import Approve, Bills
from employee.models import Employee

# Create your views here.
def all_bills(request):
    bills = Bills.objects.all()
    return render(request, 'all_bills.html', {'bills': bills})

def employee_view(request):
    employee = Employee.objects.all()
    return render(request, 'employee_view.html', {'employee': employee})

def generate_bill(request, emp_id, name_emp):
    if request.method == 'POST':
        try:
            bills = Bills(
            employee_id = request.POST['emp_id'],
            name = request.POST['name'],
            net_salary = request.POST['net_salary'],
            date = request.POST['date'],
            )
            bills.save()
            return redirect('/salary')
        except Exception as e:
            print(f'Error generate bill: {e}')

    return render(request, 'generate_bill.html', {'emp_id': emp_id, 'name_emp': name_emp})

def view_bill(request, bill_id):
    #Form
    bill = Bills.objects.filter(id=bill_id)
    return render(request, 'view_bill.html', {'bill': bill})

def salary_excelsheet(request):
    #Calculation
    return render(request, 'all_emp_excelsheet.html')

def approved(request):
    approve = Approve.objects.filter(status='Approve')
    return render(request, 'approve.html', {'status': 'Approve', 'approve': approve})

def pending(request):
    pending = Approve.objects.filter(status='Pending')
    return render(request, 'approve.html', {'status': 'Pending', 'pending': pending})