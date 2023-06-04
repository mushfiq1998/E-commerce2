from django.db import models
from core.models import User
from product.models import Product
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(
        CartInfo, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cart_id)

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, null=True, blank=True, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        # return str(self.id)
        return f"cartitem #{self.pk} - {self.cart}"

@receiver(pre_save, sender=Cart)
def at_begining_save(sender, instance, **kwargs):
    print('Pre signal')
    print('sender: ', sender)
    print('instance: ', instance)
    print(f'kwargs: {kwargs}')

@receiver(post_save, sender=Cart)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print('Post signal')
        print('sender: ', sender)
        print('instance: ', instance)
        print('created: ', created)
        print(f'kwargs: {kwargs}')
    else:
        print('Post signal')
        print('sender: ', sender)
        print('instance: ', instance)
        print('updated')
        print(f'kwargs: {kwargs}')
