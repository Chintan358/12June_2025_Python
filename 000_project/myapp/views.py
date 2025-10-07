from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    try :
        cid =  int(request.GET['cid']  )
       
        if cid!=0:
            products = Product.objects.filter(category_id=cid)
        else:
            products = Product.objects.all()
        return render(request,"index.html",{"categories":categories,"products":products})
    except Exception as e:
         return render(request,"index.html",{"categories":categories,"products":products})

@login_required(login_url="login-register")
def accounts(request):
    return render(request,"accounts.html")

@login_required(login_url="login-register")
def cart(request):
    return render(request,"cart.html")

@login_required(login_url="login-register")
def checkout(request):
    return render(request,"checkout.html")

def compare(request):
    return render(request,"compare.html")

def details(request):
    return render(request,"details.html")

def login_register(request):
    return render(request,"login-register.html")

def shop(request):
    return render(request,"shop.html")

@login_required(login_url="login-register")
def wishlist(request):
    return render(request,"wishlist.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).exists()
        if user:
            return render(request,"login-register.html",{"rerr":"Username Already Exists"})
        u = User(username=username,email=email)
        u.set_password(password)
        u.save()
        return render(request,"login-register.html",{"msg":"User Registered Successfully"})
    return render(request,"login-register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            print(user.last_login)
            login(request,user)
            return render(request,"index.html")
        else:
            return render(request,"login-register.html",{"err":"Invalid Username or Password"})
            
    return render(request,"login-register.html")



def user_logout(request):
    logout(request)
    return redirect("index")