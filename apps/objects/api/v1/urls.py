from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    
    path('Objects-api-view/', ObjectsListAPIView.as_view()),
    path('Objects-api-view/<int:pk>/', Objects_api_view)


]