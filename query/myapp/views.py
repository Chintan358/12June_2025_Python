from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Faculty
# Create your views here.
def index(request):
    Faculty.objects.create(name="abc")
    return HttpResponse("Done")