from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.about_company.models import  AboutCompany
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

def test_api_view(request):
    first_AboutCompany = AboutCompany.objects.first()
    f_b = {
        'title': first_AboutCompany.titke,
        'image':first_AboutCompany.image,
        'category': first_AboutCompany.category,
        'description': first_AboutCompany.description,
        'date_create': first_AboutCompany.date_create,
    }
    return JsonResponse(f_b)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AboutCompany_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=AboutCompanySerializer(instance=AboutCompany.objects.all(), many=True).data, status=200)
        else:
            the_AboutCompany = get_object_or_404(AboutCompany, pk=pk)
            return Response(data=AboutCompanySerializer(instance=the_AboutCompany).data, status=200)
    
    elif request.method == "POST":
        sb = AboutCompanySerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_AboutCompany = get_object_or_404(AboutCompany, pk=pk)
        sb = AboutCompanySerializer(data=request.data, instance=the_AboutCompany)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_AboutCompany = get_object_or_404(AboutCompany, pk=pk)
        the_AboutCompany.delete()
        return Response('Deleted', status=200)


class AboutCompanyListAPIView(ListAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer


class AboutCompanyCreateAPIView(CreateAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
    parser_classes = (FormParser, MultiPartParser)


class AboutCompanyUpdateAPIView(UpdateAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer


class AboutCompanyDestroyAPIView(DestroyAPIView):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer

