import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.db.models import Q
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg import openapi
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.contact.models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.

def test_api_view(request):
    first_Contact = Contact.objects.first()
    f_b = {
        'title': first_Contact.title,
        'is_active': first_Contact.is_active,
    }
    return JsonResponse(f_b)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Contact_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ContactSerializer(instance=Contact.objects.all(), many=True).data, status=200)
        else:
            the_Contact = get_object_or_404(Contact, pk=pk)
            return Response(data=ContactSerializer(instance=the_Contact).data, status=200)
    
    elif request.method == "POST":
        sb = ContactSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_Contact = get_object_or_404(Contact, pk=pk)
        sb = ContactSerializer(data=request.data, instance=the_Contact)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_Contact = get_object_or_404(Contact, pk=pk)
        the_Contact.delete()
        return Response('Deleted', status=200)


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdateAPIView(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDestroyAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

