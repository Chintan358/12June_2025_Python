from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,"index.html")

def accounts(request):
    return render(request,"accounts.html")

def cart(request):
    return render(request,"cart.html")

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
            login(request,user)
            return render(request,"index.html")
        else:
            return render(request,"login-register.html",{"err":"Invalid Username or Password"})
            
    return render(request,"login-register.html")



