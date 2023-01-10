from django.shortcuts import render

from django.core import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializer import WorkshopSerializer
from .models import Workshop

class WorkshopCreateApi(generics.CreateAPIView):
    queryset=Workshop.objects.all()
    serializer_class=WorkshopSerializer

class WorkshopApi(generics.ListAPIView):
    queryset=Workshop.objects.all()
    serializer_class=WorkshopSerializer

class WorkshopUpdateApi(generics.RetrieveUpdateAPIView):
    queryset=Workshop.objects.all()
    serializer_class=WorkshopSerializer

class WorkshopDeleteApi(generics.DestroyAPIView):
    queryset=Workshop.objects.all()
    serializer_class=WorkshopSerializer

class WorkshopDetailApi(generics.RetrieveAPIView):
    queryset=Workshop.objects.all()
    serializer_class=WorkshopSerializer 