from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_bills, name='all_bills'),
    path('employee_view', views.employee_view, name='employee_view'),
    path('generate_bill/<str:emp_id>/<str:name_emp>', views.generate_bill, name='generate_bill'),
    path('view_bill/<str:bill_id>', views.view_bill, name='view_bill'),
    path('salary_excelsheet', views.salary_excelsheet, name='salary_excelsheet'),    
    path('approved', views.approved, name='approved'),    
    path('pending', views.pending, name='pending'),    
]