from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url="userlogin")
def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        img = request.FILES['img']

        Student.objects.create(name=name,email=email,phone=phone,age=age,image=img)
        return render(request,'index.html',{"msg":"Registration successfully"})
    
@login_required(login_url="userlogin")
def display(request):
    Students =  Student.objects.all()
    return render(request,'display.html',{"students":Students})

@login_required(login_url="userlogin")
def home(request):
    return render(request,"home.html")

def delete_student(request):
    sid = request.GET['sid']
    st = Student.objects.get(id=sid)
    st.delete()
    return redirect("display")

def student_by_id(request):
    sid = request.GET['sid']
    st = Student.objects.get(id=sid)
    return render(request,"update.html",{"student":st})


def update_student(request):
    if request.method=='POST':
        data  = request.POST
        sid = data.get('sid')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')
        st  =Student.objects.get(id=sid)
        st.name=name
        st.email = email
        st.phone = phone
        st.age = age
        if len(request.FILES)!=0:
            img = request.FILES['img']
            st.image = img
        st.save()

        return redirect("display")
    
def user_reg(request):
    if request.method=='POST':
        data  = request.POST
        uname = data.get("uname")
        fname = data.get("fname")
        lname = data.get("lname")
        password = data.get("pass")

        u =  User.objects.filter(username=uname).exists()
        if u:
            messages.error(request,"Username already exists")
            return render(request,"reg.html")
        user = User(first_name=fname,last_name=lname,username=uname)
        user.set_password(password)
        user.save()
        messages.success(request,"Registration successfully")
        return render(request,"reg.html")


    return render(request,'reg.html')

def user_login(request):
    if request.method=='POST':
        data  = request.POST
        uname = data.get("uname")
        password = data.get("pass")

        user = authenticate(username=uname,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            return render(request,'login.html',{'msg':"Invalid credentails"})

    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return render(request,'login.html')