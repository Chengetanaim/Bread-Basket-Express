from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    @property
    def order_price(self):
        return self.product.price * self.quantity
    

class Notice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title