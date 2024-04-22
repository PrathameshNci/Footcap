from django.db import models
from django.contrib.auth.models import User
from product.models import Prod
# Create your models here.

class CartItem(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    prod=models.ForeignKey(Prod, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)