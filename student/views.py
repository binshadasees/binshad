from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,'student_temblates/student.html')
def local(request):
    return render(request,'student_temblates/local.html')
    