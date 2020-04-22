from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework.views import APIView
from main import models, serializers


# Create your views here.

def index(response):
    return HttpResponse("<h1>ABCkindergarten</h1>")


class ParentListView(generics.ListAPIView):
    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentSerializer


class ParentDetailView(generics.RetrieveAPIView):
    lookup_field = 'Parentid'
    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentSerializer




