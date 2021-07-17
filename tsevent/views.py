from django.shortcuts import render
from rest_framework import generics
from tsevent.serializer import tseventDetailSerialazer , tseventListSerialazer
from tsevent.models import tsevent
# Create your views here.

class tseventCreateView(generics.CreateAPIView):
    serializer_class = tseventDetailSerialazer

class tseventListView(generics.ListAPIView):
    serializer_class = tseventListSerialazer
    queryset = tsevent.objects.all()