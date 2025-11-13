from django.shortcuts import render,HttpResponse
from crudapp.models import *
from crudapp.serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def get_data(request):
    try : 
        emps = Employee.objects.all()
        ser = EmployeeSerializer(emps,many=True)
        return Response({"Data":ser.data},status=status.HTTP_200_OK)
    except Exception as e :
        return Response({"message":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)