from django.db import models

class Stocks(models.Model):
    
    symbol_type = models.CharField(max_length=20, blank=True, null=True)
    stock_name = models.CharField(max_length=100, blank=True, null=True)
    symbol_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    strike_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_type = models.CharField(max_length=100, blank=True, null=True)
    entry_type = models.CharField(max_length=100,  blank=True, null=True)
    option_type = models.CharField(max_length=100,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol_type} - {self.symbol_name or self.stock_name}"
