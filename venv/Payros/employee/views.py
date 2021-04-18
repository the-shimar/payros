from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee, Qualification

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def add_employee(request):
    if request.method == 'POST':
        try:
            emp_obj = Employee(
                employee_id= request.POST['emp_id'],
                name= request.POST['name'],
                dob= request.POST['dob'],
                doj= request.POST['doj'],
                address= request.POST['address'],
                dor= request.POST['dor'],
                qualification= request.POST['qualification'],
                department= request.POST['derpartment'],
                phone= request.POST['ph'],
                bank_ac= request.POST['bank_ac'],
            )
            emp_obj.save()
            print(f'Success')
            return redirect('/employee/add')

        except Exception as e:
            print(f" Emp Add Error: {e}")
        return redirect('/employee')
    
    else:
        qualification = Qualification.objects.all()
        return render(request, 'add_employee.html', { 'qualification': qualification})

def view_employee(request):
    emp_obj = Employee.objects.all()
    return render(request, 'view_employee.html', {'emp_obj': emp_obj})

def delete_employee(request, emp_id):
    emp_obj = Employee.objects.get(employee_id=emp_id)
    emp_obj.delete()
    return redirect('/employee')

def edit_view(request, emp_id):
    if request.method == 'POST':
        try:
            emp_obj = Employee.objects.filter(employee_id=emp_id)
            emp_obj.update(
                name= request.POST['name'],
                dob= request.POST['dob'],
                doj= request.POST['doj'],
                address= request.POST['address'],
                dor= request.POST['dor'],
                qualification= request.POST['qualification'],
                department= request.POST['derpartment'],
                phone= request.POST['ph'],
                bank_ac= request.POST['bank_ac'],
            )
            emp_obj.save()
            print(f'Success')
            return redirect('/employee/add')

        except Exception as e:
            print(f" Emp Edit Error: {e}")
        return redirect('/employee')
    emp_obj = Employee.objects.filter(employee_id=emp_id)
    qualification = Qualification.objects.all()

    return render(request, 'edit_employee.html', {'emp_obj': emp_obj, 'qualification': qualification})


