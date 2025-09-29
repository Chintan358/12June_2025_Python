from django.contrib import admin
from myapp.models import *
# Register your models here.
class StudentModel(admin.ModelAdmin):
    list_display = ['id','name','email','phone','age']


admin.site.register(Student,StudentModel)
