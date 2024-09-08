from django.urls import path
from .views import StocksListCreateView, StocksDetailView

urlpatterns = [
    path('stocks/', StocksListCreateView.as_view(), name='stocks_list'),
    path('stocks/<int:pk>/', StocksDetailView.as_view(), name='stock_detail'),
]
