from django.db import models
from django.urls import reverse

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    productType = models.ForeignKey(
        ProductType, 
        null=True,
        on_delete=models.SET_NULL, 
        related_name='products'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:merchstore_detail', args=[self.pk])
    
    class Meta: 
        ordering = ['name']