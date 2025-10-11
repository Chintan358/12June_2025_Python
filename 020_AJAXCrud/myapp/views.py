from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method=='POST':
        data = request.POST

        dept_id = data.get('dept')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        dept = Department.objects.get(id=dept_id)

        Student.objects.create(name=name,email=email,phone=phone,age=age,dept=dept)
        return HttpResponse("Registration successfull Done !!!")
    
def display(request):
    allStudents = Student.objects.all()    
    for student in allStudents:
        print(student.dept.name)
    data = list(
            allStudents.values(
                'id',
                'name',
                'email',
                'phone',
                'age',
                'dept__id',
                'dept__name', 
            )
        )
        
    return JsonResponse({"data": data})


def deptdisplay(request):
    alldetps = Department.objects.all()
    return JsonResponse({"data":list(alldetps.values())})