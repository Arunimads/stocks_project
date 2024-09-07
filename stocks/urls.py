from django.urls import path
from .views import save_stock_data

urlpatterns = [
    path('stock/', save_stock_data, name='save-stock-data'),
]
