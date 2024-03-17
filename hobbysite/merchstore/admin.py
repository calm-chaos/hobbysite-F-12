from django.contrib import admin

from .models import ProductType, Product
# Register your models here.

class ProductTypeAdmin(admin.ModelAdmin):
    model = Product


class ProductAdmin(admin.ModelAdmin):
    model = Product


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
