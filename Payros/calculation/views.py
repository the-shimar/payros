from django.shortcuts import redirect, render

# Create your views here.
def calculation_view(request):
    return render(request, 'calculation_view.html')
    
def calculation_edit(request):
    return render(request, 'calculation_edit.html')