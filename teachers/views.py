from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('homepage')
    
def loginfun(request):
    return render(request,'login.html')

def read(request):
    return render(request,'read.html')       