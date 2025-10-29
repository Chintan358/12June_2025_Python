from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')


def payment(request):

    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_R8LF6p6eS7swQn", "WsLBNmXfF7C4e9T4vWgZaLeN"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    
    return JsonResponse(payment)