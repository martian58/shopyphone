# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    id = models.BigAutoField(primary_key=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'
    

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        db_table = 'customers'
        managed = True
        verbose_name = 'Customers'
        verbose_name_plural = 'Customers'
    

    
class Product(models.Model):
    RAM_CAPACITY = (
        ('3', '3'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('12', '12'),
        )
    
    ROM_CAPACITY= (
        ('32', '32'),
        ('64', '64'),
        ('128', '128'),
        ('264', '264'),
        ('512', '512'),
        ('1024', '1024')
    )
    brand_name = models.CharField(max_length=100, blank=False)
    model_name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(default =0,max_digits=6, decimal_places=2)
    color = models.ForeignKey("Color", on_delete=models.CASCADE, null=True)
    ram = models.CharField(max_length=2, choices=RAM_CAPACITY)
    memory = models.CharField(max_length=4, choices=ROM_CAPACITY, help_text="GB")
    is_new = models.BooleanField(default=False)
    fingerprint = models.BooleanField(default=False)
    fice_id = models.BooleanField(default=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    description = models.CharField(default='', max_length=250, blank=True)
    image = models.ImageField(upload_to='uploads/pruduct/')
    # Sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default =0,max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.brand_name} {self.model_name}"
    
    class Meta:
        db_table = 'products'
        managed = True
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

class Color(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return f"{self.name}"

class Order(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)   
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=12,blank=True)
    date = models.DateField( auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    
    class Meta:
        db_table = 'orders'
        managed = True
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'

class Mail(models.Model):
    form_user_id = models.PositiveIntegerField(null=True, blank=True)
    to_user_id = models.PositiveIntegerField(null=True, blank=True)
    subject = models.CharField(max_length=256)
    message = models.TextField(max_length=5000)
    from_email = models.EmailField()
    to_email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.pk} {self.from_email} -> {self.to_email}"
