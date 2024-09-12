
from django.urls import path
from .views import StocksListCreateView

urlpatterns = [
    path('stocks/', StocksListCreateView.as_view(), name='stocks_list'),
    # path('read-csv/',read_csv_and_print.as_view(), name='read_csv'),
]
