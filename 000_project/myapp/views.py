from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

def index(request):
  
   
    return render(request,"index.html")
    

def allcategories(request):
    categories = Category.objects.all()
    return JsonResponse({"data":list(categories.values())})

def allproducts(request):
    cid = request.GET['catid']
   
    if int(cid)==0:
         print(cid)
         products = Product.objects.all()
         return JsonResponse({"data":list(products.values())})
    else : 
        products=Product.objects.filter(category_id=cid)
        return JsonResponse({"data":list(products.values())})

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


def add_to_cart(request):

    if not request.user.is_anonymous  :
        pid = request.GET['pid']
        product = Product.objects.get(id=pid)
        
        Cart.objects.create(product =product,user=request.user,qty=1)
        return HttpResponse("Product added in to cart !!!")
    else :
        return HttpResponse(request.user)