from django.db import models
from django.contrib import admin

class Details(models.Model):
    Phone_number=models.IntegerField(primary_key=10)
    Name=models.CharField(max_length=10)
    
    Address=models.TextField()
    Product_name=models.CharField(max_length=20)
    Available_quantity=models.IntegerField()
    Expiry_date=models.DateField()

class DetailsAdmin(admin.ModelAdmin):
    list_display=["Phone_number","Name","Address","Product_name","Available_quantity","Expiry_date"]