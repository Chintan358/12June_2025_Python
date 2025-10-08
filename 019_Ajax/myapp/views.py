from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    data = request.GET['data']
    # products = Product.objects.filter(name=data)
    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"data":list(products.values())})