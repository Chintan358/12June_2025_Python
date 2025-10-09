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


def countries(request):
    allcountries = Country.objects.all()
    return JsonResponse({"data":list(allcountries.values())})

def states(request):
    cid = request.GET['cid']
    allStates = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(allStates.values())})

def cities(request):
    sid = request.GET['sid']
    allCities = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(allCities.values())})