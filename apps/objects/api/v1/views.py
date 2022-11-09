from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from apps.objects.models import Objects
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import *
# Create your views here.

@api_view(['GET'])
def Objects_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ObjectsSerializer(instance=Objects.objects.all(), many=True).data, status=200)
        else:
            the_Objects = get_object_or_404(Objects, pk=pk)
            return Response(data=ObjectsSerializer(instance=the_Objects).data, status=200)

class ObjectsListAPIView(ListAPIView):
    queryset = Objects.objects.all()
    serializer_class = ObjectsSerializer


