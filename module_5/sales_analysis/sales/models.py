from django.db import models

class SalesData(models.Model): 
    product_name = models.CharField(max_length=255) 
    sales_amount = models.FloatField() 
    date = models.DateField() 

class SalesReport(models.Model): 
    month = models.CharField(max_length=20)
    total_sales = models.FloatField()
    top_product = models.CharField(max_length=255)
