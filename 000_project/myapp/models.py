from django.db import models

# Create your models here.
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

