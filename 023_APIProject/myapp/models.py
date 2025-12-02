from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="cat_img")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price=models.FloatField()
    qty = models.IntegerField()
    description=models.TextField()
    image = models.ImageField(upload_to="prod_img")

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def subtotal(self):
        return self.product.price*self.qty
    

class Address(models.Model):
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class UserOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    total = models.IntegerField()
    paymentid = models.CharField(max_length=20)
    receiptid = models.CharField(max_length=20)
    orderid = models.CharField(max_length=30)
    date = models.DateField()
    
class OrderDetails(models.Model):
    order = models.ForeignKey(UserOrder,on_delete=models.CASCADE,related_name="userorder")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()

    def subtotal(self):
        return self.price*self.qty



