from django.shortcuts import redirect, render
from .models import Approve, Bills, EmployeeSalaryDetails
from employee.models import Employee
from calculation.models import Salary
from salary.models import EmployeeSalaryDetails

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
    POST = 1
    emp_obj = Employee.objects.all()
    for each_emp in emp_obj:
        basic = da = hra = ma = cca = 0
        calculation_obj = Salary.objects.get(qualification=emp_obj.qualification, year=emp_obj.year)
        basic = int(calculation_obj.basic)
        da = int(calculation_obj.basic) * .2
        hra = int(calculation_obj.basic) * .15
        ma = int(calculation_obj.basic) * .5
        cca = int(calculation_obj.basic) * .1
        total_allowance = da + hra + ma + cca

        epf = esi = rbs = llp = society = sarvodhaya = fa = total_deduction = 0
        net_salary = 0
        generate_salary = EmployeeSalaryDetails(
            emp_id = emp_obj.employee_id,
            name = emp_obj.name,
            basic = calculation_obj.basic,
            da = da,
            hra = hra,
            ma = ma,
            cca = cca,
            total_allowance = total_allowance, 
            epf = epf,
            esi = esi,
            rbs = rbs,
            llp = llp,
            society = society,
            sarvodhaya = sarvodhaya,
            fa = fa,
            total_deduction = total_deduction,
            net_salary = net_salary
        )
        generate_salary.save()
        
    return render(request, 'all_emp_excelsheet.html')

def approved(request):
    approve = Approve.objects.filter(status='Approve')
    return render(request, 'approve.html', {'status': 'Approve', 'approve': approve})

def pending(request):
    pending = Approve.objects.filter(status='Pending')
    return render(request, 'approve.html', {'status': 'Pending', 'pending': pending})