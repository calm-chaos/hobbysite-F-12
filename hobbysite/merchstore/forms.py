from django import forms 

from .models import Product, Transaction


class TransactionForm(forms.ModelForm):
    class Meta: 
        model = Transaction
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        exclude = ['owner']


    