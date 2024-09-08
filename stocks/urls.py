from django.urls import path
from .views import StocksListCreateView, StocksDetailView, RegisterView, LoginView

urlpatterns = [
    path('stocks/', StocksListCreateView.as_view(), name='stocks_list'),
    path('stocks/<int:pk>/', StocksDetailView.as_view(), name='stock_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
