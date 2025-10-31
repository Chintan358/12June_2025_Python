from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse
# Create your views here.
import requests
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request,'index.html')


def payment(request):

    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_R8LF6p6eS7swQn", "WsLBNmXfF7C4e9T4vWgZaLeN"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    
    return JsonResponse(payment)


def sms(request):
    
    phone = request.GET['phone']
    message = request.GET['message']

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"WXfAe5cjnlMG0thTkdLD9IsgRyZbS7w41UzP3H8mKiqQNVEova9vDJtywEXpMNoUieOfPlq1r8HhdnTL","message":message,"language":"english","route":"q","numbers":phone}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return HttpResponse(response.text)


def send_email(request):

    emailto = request.GET['email-to']
    subject = request.GET['subject']
    message = request.GET['message']
    context = {}
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [emailto])
        context['result'] = 'Email sent successfully'
    except Exception as e:
        context['result'] = f'Error sending email: {e}'
   

    return render(request,'index.html',context)