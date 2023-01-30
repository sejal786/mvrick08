from django.contrib import admin
from django.contrib.auth.models import Group
from .models import create_employee , add_product , add_doctor , doctor_schedule , deals_detail

# Register your models here.
from .models import create_employee
admin.site.register(create_employee)

from .models import add_product
admin.site.register(add_product)

from .models import add_doctor
admin.site.register(add_doctor)

from .models import doctor_schedule
admin.site.register(doctor_schedule)

from .models import deals_detail
admin.site.register(deals_detail)




admin.site.site_header = "Sejal's CMS Portal"
admin.site.site_title = "Sejal's CMS Portal"
