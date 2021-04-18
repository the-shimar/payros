from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/edit_view/<str:emp_id>', views.edit_view, name='edit_view'),
    path('employee/delete/<str:emp_id>', views.delete_employee, name='delete_employee'),
    path('employee', views.view_employee, name='employee'),
    path('employee/add', views.add_employee, name='employee_add'),
]