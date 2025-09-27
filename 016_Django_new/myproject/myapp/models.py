from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    dept = models.CharField(max_length=20)
    jdata = models.DateField()
    

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    qty = models.IntegerField()
    

