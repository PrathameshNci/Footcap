from django.db import models
from django.contrib.auth.models import User
from product.models import Prod
# Create your models here.

class Order(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    order_main_id = models.CharField(max_length=50)
    status = models.CharField(max_length= 50, default='Ordered')