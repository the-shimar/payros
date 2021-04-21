from django.shortcuts import render
from .models import BankAdvice

# Create your views here.
def bank_advice(request):
    bandadvice = BankAdvice.objects.all()
    return render(request, 'bankadvice.html', {'bandadvice': bandadvice})