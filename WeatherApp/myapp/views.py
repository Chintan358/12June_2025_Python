from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    name = request.session.get('name')
    if name : 
        try :
            
            
            name = request.GET['city']
            geocode = requests.get(f"https://api.opencagedata.com/geocode/v1/json?q={name}&key=2b5459733fbc4cf1b3c8a8e6a38cdaf4")
            g_result = geocode.json()
            lat = g_result['results'][0]['geometry']['lat']
            lng = g_result['results'][0]['geometry']['lng']

            data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric")
            result = data.json()

            resp = {
                "city" : result['name'],
                "lat" : lat,
                "lng" : lng,
                "temp" : result['main']['temp'],
                "pressure" : result['main']['pressure'],
                "humidity" : result['main']['humidity']
            }
        
            return render(request,"index.html",resp)
        except Exception as e:
            return render(request,"index.html")
    else : 
        return HttpResponse("login required")


def user_login(request):
    request.session['name']="hardik"
    return HttpResponse("Login page")

def user_logout(request):
    request.session['name']=""
    return HttpResponse("Logout")