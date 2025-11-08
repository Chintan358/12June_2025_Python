from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import razorpay
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
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
    addressdata = Address.objects.filter(user=request.user)
    orders = UserOrder.objects.filter(user = request.user)
    return render(request,"accounts.html",{"address":addressdata,"orders":orders})

@login_required(login_url="login-register")
def cart(request):
    cartdata = Cart.objects.filter(user=request.user)
    addressdata = Address.objects.filter(user=request.user)
 
    sum = 0
    for i in cartdata:
       sum+=i.subtotal()

    return render(request,"cart.html",{"cdata":cartdata,"total":int(sum),"address":addressdata})

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
        
        cdata =  Cart.objects.filter(product=product,user=request.user)
        if len(cdata)>0:
            cdata[0].qty = cdata[0].qty+1
            cdata[0].save()
            return HttpResponse("Product added in to cart !!!")
        else:
            Cart.objects.create(product =product,user=request.user,qty=1)
            return HttpResponse("Product added in to cart !!!")
    else :
        return HttpResponse(request.user)
    

def deletecart(request):
    cid = request.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("cart deleted")


def changeqty(request):
    cartid = request.GET['cartid']
    qty  =request.GET['qty']

    cart = Cart.objects.get(pk=cartid)
    if int(qty)<=0:
        cart.delete()
    else:
        cart.qty= qty
        cart.save()
    return HttpResponse("cart updated...")


def payment(request):

    orders = UserOrder.objects.all()
    rid = len(orders)+1
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_R8LF6p6eS7swQn", "WsLBNmXfF7C4e9T4vWgZaLeN"))
     
    data = { "amount": amt*100, "currency": "INR", "receipt": f"order_rcptid_{rid}" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    print(payment)
    return JsonResponse(payment)


def addaddress(request):
    adr = request.GET['adr']
    Address.objects.create(address=adr,user=request.user)
    return HttpResponse("address added")

def makeorder(request):

    rid = request.GET['rid']
    payid = request.GET['payid']
    oid = request.GET['oid']
    aid = request.GET['aid']
    total = request.GET['total']
   
    address = Address.objects.get(pk=aid)

    order = UserOrder.objects.create(
        user=request.user,
        address=address,
        paymentid=payid,
        total = int(total)/100,
        receiptid=rid,
        orderid=oid,
        date = datetime.now()
    )

    rows= ""
    cartdata =  Cart.objects.filter(user = request.user)
    for cart in cartdata:
        OrderDetails.objects.create(order=order,product=cart.product,qty=cart.qty,price=cart.product.price)
        rows+=f"<tr><td>{cart.product.id}</td><td>{cart.product.name}</td><td>{cart.qty}</td><td>${cart.product.price}</td><td>${cart.subtotal()}</td></tr>"
        cart.delete()

    

    
    subject =  "Order Confimation"
    message = "Order Confirmation"
    html_content=f"<table border='1'><thead><tr><th>Order Id : {order.orderid}</th><th>Date : {order.date}</th><th rowspan='2'>Total : {order.total}</th><th rowspan='2'>Address : {order.address.address}</th></tr><tr><th>Pay Id : {order.paymentid}</th><th>Receipt Id : {order.receiptid}</th></tr><tr><th>ID</th><th>Product</th><th>Qty</th><th>price</th><th>Subtotal</th></tr></thead><tbody>{rows}</tbody></table>"
    context = {}
    try:

        msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER , [request.user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        context['result'] = 'Email sent successfully'
    except Exception as e:
        context['result'] = f'Error sending email: {e}'
    


    return HttpResponse("order successfully placed !!!")