from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name =models.CharField(max_length=255)
    price =models.FloatField()
    image =models.ImageField(upload_to='media/product_image')

class Carousel(models.Model):
    name =models.CharField(max_length=100)
    price =models.IntegerField()
    image =models.ImageField(upload_to='media/Carousel_image')
    Decoration=models.TextField()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Address=models.TextField()
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pincode=models.IntegerField()
    Phone=models.IntegerField()
    Email=models.EmailField(max_length=50)
 
    def __str__(self):
        return self.First_Name
    
class Orderitem(models.Model):
    Order=models.ForeignKey(Order,on_delete=models.CASCADE)
    Product=models.CharField(max_length=40)
    image=models.ImageField(upload_to='media/order')
    qunatity=models.IntegerField()
    price=models.FloatField()
    total=models.IntegerField()
    paid=models.BooleanField(default=False)