from django.shortcuts import render
from django.http import HttpResponse
from.models import create_employee
from.models import *

# Create your views here.
def Employee(request):
    return render(request, 'index.html')

def AddProduct(request):
    return render(request, 'addproduct.html')

def ViewAllProducts(request):
    return render(request, 'viewallproducts.html')

def AddDoctor(request):
    return render(request, 'adddoctor.html')

def ScheduleDoctorAppointment(request):
    return render(request, 'sdappointment.html')

def TodaysSchedule(request):
    return render(request, 'todaysschedule.html')

def DealsDetail(request):
    return render(request, 'dealsdetails.html')