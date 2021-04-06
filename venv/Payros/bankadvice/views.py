from django.shortcuts import render

# Create your views here.
def bank_advice(request):
    return render(request, 'bankadvice.html')