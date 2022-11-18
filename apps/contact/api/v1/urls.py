from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    # path('test-api-view/', test_api_view),
    path('Contact-api-view/', ContactListAPIView.as_view()),
    path('Contact-api-view/create', ContactCreateAPIView.as_view()),
    # path('Contact-api-view/update/<int:pk>', ContactUpdateAPIView.as_view()),
    # path('Contact-api-view/delete/<int:pk>', ContactDestroyAPIView.as_view()),
    # path('Contact-api-view/detail/<int:pk>', ContactDetailView.as_view()),
    
    # path('Contact-api-view/<int:pk>/', Contact_api_view),path('test-api-view/', test_api_view),


]