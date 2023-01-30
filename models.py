from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime
# Create your models here.


class create_employee(models.Model):
       
    Employee_Firstname = models.CharField(max_length=50)
    Employee_Lastname = models.CharField(max_length=50)
    Employee_Email = models.EmailField(max_length=25)
    Employee_Password = models.CharField(max_length=10)
    Employee_Date_of_Joining = models.DateTimeField()
    Employee_Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Employee_Firstname +" "+ self.Employee_Lastname

    


class add_product(models.Model):
    
    Product = models.ForeignKey(create_employee, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=50)
    Product_Company_Name = models.CharField(max_length=50)
    Product_Image = models.ImageField(upload_to=None, height_field=None, width_field=100, max_length=100)
    Product_Price = models.DecimalField(max_digits=8, decimal_places=2)
    Entered_by = models.CharField(max_length=50)

    def __str__(self):
        return self.Product_Name +" "+ self.Entered_by 

    

class add_doctor(models.Model):
    
    Doctor = models.ForeignKey(create_employee, on_delete=models.CASCADE)
    Doctor_Name = models.CharField(max_length=50)
    Doctor_Specialization = models.CharField(max_length=50)
    Doctor_Contact_Number = models.CharField(max_length=10)
    Doctor_Location = models.CharField(max_length=50)
    Entered_by = models.CharField(max_length=50)

    def __str__(self):
        return self.Doctor_Name +" "+ self.Doctor_Specialization

    

class doctor_schedule(models.Model):
    
    Doctor_Schedule = models.ForeignKey(add_doctor, on_delete=models.CASCADE)
    Doctor_Name = models.CharField(max_length=50)
    Date_of_Schedule = models.DateField()
    Time_of_Schedule = models.TimeField()
    Entered_by = models.CharField(max_length=50)

    def __str__(self):
        return self.Doctor_Name +" "+ self.Entered_by

    

class deals_detail(models.Model):
    
    Doctor_Deals_Detail = models.ForeignKey(add_doctor, on_delete=models.CASCADE)
    Doctor_Name = models.CharField(max_length=50)
    Product_Deals_Detail = models.ForeignKey(add_product, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=50)
    Quantity_Ordered = models.IntegerField()
    Entered_by = models.CharField(max_length=50)

    def __str__(self):
        return self.Doctor_Deals_Detail


    


    

    
