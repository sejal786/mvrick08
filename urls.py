from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views 
from django.conf import settings


urlpatterns = [
    
    path('', views.Employee, name="Employee"),
    path('AddProduct/', views.AddProduct, name="Add Product"),
    path('ViewAllProducts/', views.ViewAllProducts, name="View All Products"),
    path('AddDoctor/', views.AddDoctor, name="Add Doctor"),
    path('ScheduleDoctorAppointment/', views.ScheduleDoctorAppointment, name="Schedule Doctor Appointment"),
    path('TodaysSchedule/', views.TodaysSchedule, name="Today's Schedule"),
    path('DealsDetail/', views.DealsDetail, name="Deals Detail"),  

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )