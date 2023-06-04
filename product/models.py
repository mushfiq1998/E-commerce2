from django.db import models
from core.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Test(models.Model):
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2, 
    blank=True, null=True)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to="products image", 
    blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    name = models.CharField(max_length=255) 
    product_code = models.CharField(max_length=20, blank=True, null=True)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, 
    blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, 
    blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    image = models.ForeignKey(
        ProductImage, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return f"Product id: {self.pk} , Product name: {self.name}"

@receiver(post_save, sender=Product)
def product_handler(sender, instance, **kwargs):
    Test.objects.create(name=instance.name, price=instance.price)
    print('post save called')
    print(instance)

# Manage Orders
class OrderItem(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.item)

    @property
    def total(self):
        if self.item.sale_price:
            return self.item.sale_price * self.quantity
        else:
            return self.item.regular_price * self.quantity

class Order(models.Model):
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_items = models.ManyToManyField(OrderItem, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
    blank=True, null=True)
    quantity = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)