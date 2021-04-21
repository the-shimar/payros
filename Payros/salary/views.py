from django.shortcuts import redirect, render
from .models import Approve, Bills
from employee.models import Employee, Qualification
from calculation.models import Salary
from bankadvice.models import BankAdvice
import django.utils.timezone as timezone
# from salary.models import EmployeeSalaryDetails

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
    list_report = []
    year = timezone.now().year
    month = timezone.now().month   
    print(f'Month : {month}') 

    for each_emp in emp_obj:
        #year
        year_of_emp = each_emp.doj
        year_of_emp = year_of_emp.split('-')
        print(f'Year: {year_of_emp}, now year: {year}')
        emp_working_year = int(year) - int(year_of_emp[2])
        print(f'working year {emp_working_year}')
        if emp_working_year <= 0:
            emp_working_year = 1
        if 4 <= emp_working_year <= 8:
            emp_working_year = 4
        if 9 <= emp_working_year <= 13:
            emp_working_year = 9
        if 14 <= emp_working_year <= 18:
            emp_working_year = 14
        if 19 <= emp_working_year <= 23:
            emp_working_year = 19
        if 24 <= emp_working_year:
            emp_working_year = 24   
        print(f'Refined working year: {emp_working_year}')
        basic = da = hra = ma = cca = increment = 0
        # calculation_obj = Salary.objects.get(qualification=each_emp.qualification, year=each_emp.year)
        qualification_id = Qualification.objects.get(qualification=each_emp.qualification)
        calculation_obj = Salary.objects.get(qualification=qualification_id.id, year=emp_working_year) #need to calculate year
        llp30 = 0

        basic = int(calculation_obj.basic)

        #Increment Calculator works if month is 1 that is Jan
        # if True:
        if month == 1:
            increment = int(qualification_id.increment)
            basic += increment

        # da = int(calculation_obj.basic) * .2
        # hra = int(calculation_obj.basic) * .2
        # ma = int(calculation_obj.basic) * .05
        # cca = int(calculation_obj.basic) * .05

        da = int(basic) * (int(calculation_obj.da)/100)
        hra = int(basic) * (int(calculation_obj.hra)/100)
        ma = int(basic) * (int(calculation_obj.ma)/100)
        cca = int(basic) * (int(calculation_obj.cca)/100)
        
        total_allowance = basic + da + hra + ma + cca

        epf = esi = rbs = llp = society = sarvodhaya = fa = other_det = other = total_deduction = 0
        net_salary = 0
        # epf = (basic + da) * .12
        # esi = total_allowance * .075
        # print(f'epf: {int(calculation_obj.epf)}')
        epf = (basic + da) * (int(calculation_obj.epf)/100)
        esi = total_allowance * (int(calculation_obj.esi)/1000) #thousand because of 3 digit logic
        if esi > 21000:
            esi = 21000

        total_deduction = epf + esi + rbs + llp + society + sarvodhaya + fa + other_det + other
        net_salary = (total_allowance - total_deduction) + increment
        generate_salary = {
            "emp_id" : each_emp.employee_id,
            "name" : each_emp.name,
            "experience": emp_working_year,
            "llp30" : llp30,
            "basic" : calculation_obj.basic,
            "da" : da,
            "hra" : hra,
            "ma" : ma,
            "cca" : cca,
            "total_allowance" : total_allowance, 
            "epf" : epf,
            "esi" : esi,
            "rbs" : rbs,
            "llp" : llp,
            "society" : society,
            "sarvodhaya" : sarvodhaya,
            "fa" : fa,
            "other_det" : other_det,
            "total_deduction" : total_deduction,
            "other" : other,
            "increment": increment,
            "net_salary" : net_salary
        }
        list_report.append(generate_salary)

        #updating employee year
        try:
            emp_obj_year = Employee.objects.filter(employee_id=each_emp.employee_id)
            emp_obj_year.update(year=emp_working_year)
            print(f'Employee Year Updation Done')

        except Exception as e:
            print(f'Employee Year Updation Error: {e}')

        #bank_advice
        try:
            obj = BankAdvice.objects.get(emp_id=each_emp.employee_id) #get is here to find in table, if not returns error, because filter don't return error
            obj = BankAdvice.objects.filter(emp_id=each_emp.employee_id) #filter is to update it
            obj.update(
                salary = net_salary,
                emp_name=each_emp.name
            )
            print(f'update: BA : {each_emp.employee_id}, name: {each_emp.name}')

        except BankAdvice.DoesNotExist:
            obj = BankAdvice(
                emp_id=each_emp.employee_id, account_number=each_emp.bank_ac,
                emp_name=each_emp.name, salary=net_salary)
            obj.save()
            print(f'Save: BA : {each_emp.employee_id}, name: {each_emp.name}')

        except Exception as e:
            print(f'Bank Advice Update Error: {e}')
        
    return render(request, 'all_emp_excelsheet.html', {'list_report': list_report})

def approved(request):
    approve = Approve.objects.filter(status='Approve')
    return render(request, 'approve.html', {'status': 'Approve', 'approve': approve})

def pending(request):
    pending = Approve.objects.filter(status='Pending')
    return render(request, 'approve.html', {'status': 'Pending', 'pending': pending})