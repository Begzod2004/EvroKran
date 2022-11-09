from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *

urlpatterns = [
    # path('test-api-view/', test_api_view),
    path('AboutCompany-api-view/', AboutCompanyListAPIView.as_view()),
    # path('AboutCompany-api-view/create', AboutCompanyCreateAPIView.as_view()),
    # path('AboutCompany-api-view/update/<int:pk>', AboutCompanyUpdateAPIView.as_view()),
    # path('AboutCompany-api-view/delete/<int:pk>', AboutCompanyDestroyAPIView.as_view()),
    # path('AboutCompany-api-view/detail/<int:pk>', AboutCompanyDetailView.as_view()),
    
    # path('AboutCompany-api-view/<int:pk>/', AboutCompany_api_view),path('test-api-view/', test_api_view),
]