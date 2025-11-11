from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from rest_framework.response import Response
from myapp.serializer import *
@api_view(['GET'])
def get_users(request):
    return HttpResponse("GET API CALLING")

@api_view(['POST'])
def post_users(request):
    return HttpResponse("POST API CALLING")

@api_view(['PUT'])
def put_users(request):
    return HttpResponse("PUT API CALLING")

@api_view(['DELETE'])
def delete_users(request):
    return HttpResponse("DELETE API CALLING")

@api_view(['GET'])
def test(request):
    return HttpResponse("")

class StudentView(APIView):

    def get(request,self):
        allstudents = Student.objects.all()
        students =  StudentSerializer(allstudents,many=True)
        return Response({"students":students.data})
    
    def post(request,self):
        return HttpResponse("POST api calling")
    
    def put(request,self):
        return HttpResponse("PUT api calling")
    
    def delete(request,self):
        return HttpResponse("DELETE api calling")