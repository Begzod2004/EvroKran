from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.blog.models import Category, Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
from datetime import datetime
# Create your views here.


@api_view(['GET'])
def Category_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=CategoryBlogSerializer(instance=Category.objects.all(), many=True).data, status=200)
        else:
            the_Category = get_object_or_404(Category, pk=pk)
            return Response(data=CategoryBlogSerializer(instance=the_Category).data, status=200)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryBlogSerializer


@api_view(['GET'])
def Blog_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=BlogSerializer(instance=Blog.objects.all(), many=True).data, status=200)
        else:
            the_Blog = get_object_or_404(Blog, pk=pk)
            return Response(data=BlogSerializer(instance=the_Blog).data, status=200)


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer