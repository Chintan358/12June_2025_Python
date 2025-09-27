from django.contrib import admin
from myapp.models import *
# Register your models here.

class EmpModel(admin.ModelAdmin):
    list_display=['id','name','email','dept','jdata']

admin.site.register(Student)
admin.site.register(Employee,EmpModel)
admin.site.register(Product)