from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *



urlpatterns = [
    # path('test-api-view/', test_api_view),
    path('Category-api-view/', CategoryListAPIView.as_view()),
    # path('Category-api-view/create', CategoryCreateAPIView.as_view()),
    # path('Category-api-view/update/<int:pk>', CategoryUpdateAPIView.as_view()),
    # path('Category-api-view/delete/<int:pk>', CategoryDestroyAPIView.as_view()),
    # # path('Category-api-view/detail/<int:pk>', CategoryDetailView.as_view()),
    
    path('Category-api-view/<int:pk>/', Category_api_view),
    
# Blog   
    # path('test-api-view/', test_api_view),
    path('Blog-api-view/', BlogListAPIView.as_view()),
    # path('Blog-api-view/create', BlogCreateAPIView.as_view()),
    # path('Blog-api-view/update/<int:pk>', BlogUpdateAPIView.as_view()),
    # path('Blog-api-view/delete/<int:pk>', BlogDestroyAPIView.as_view()),
    # path('Blog-api-view/detail/<int:pk>', BlogDetailView.as_view()),
    path('Blog-api-view/<int:pk>/', Blog_api_view),

]