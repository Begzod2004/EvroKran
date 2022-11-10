from django.urls import path
from .views import OrderCreateAPIView, OrderListAPIView, Order_api_view



urlpatterns = [
    path('Order-api-view/', OrderListAPIView.as_view()),
    path('Order-api-view/create', OrderCreateAPIView.as_view()),

    path('Order-api-view/<int:pk>/', Order_api_view)
]