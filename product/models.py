from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=60)

class SubCategory(models.Model):
    name=models.CharField(max_length=60)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)

class Prod(models.Model):
    name=models.CharField(max_length=60)
    scat=models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    img = models.ImageField(upload_to='media/shoe/')
    price=models.IntegerField(default=110)
        
class Special(models.Model):
    prod=models.ForeignKey(Prod, on_delete=models.CASCADE)
    

        
