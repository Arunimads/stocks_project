
from django.urls import path
from .views import StocksListCreateView

urlpatterns = [
    path('stocks/', StocksListCreateView.as_view(), name='stocks_list'),
]
