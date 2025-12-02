from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import *
from myapp.serializer import *
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response

# Create your views here.
class CategoryView(APIView):
    def get(self,request):
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CategoryDetailView(APIView):
 
    def get(self,request,pk):
        category=self.get_object(pk)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self,request,pk):
        category=self.get_object(pk)
        serializer=CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        category=self.get_object(pk)
        category.delete()
        return Response({"message":"Category deleted successfully"})

