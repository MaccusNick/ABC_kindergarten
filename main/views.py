from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.models import AuthToken
from main import models, serializers
from main.serializers import UserSerializer, RegisterSerializer, LoginSerializer


def index(response):
    return HttpResponse("<h1>ABCkindergarten</h1>")


class ParentListView(generics.ListAPIView):
    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentSerializer


# class ParentDetailView(generics.RetrieveAPIView):
#     lookup_field = 'Parentid'
#     queryset = models.Parent.objects.all()
#     serializer_class = serializers.ParentSerializer

class ManagerListView(generics.ListAPIView):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.ManagerSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializers_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_expection=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })
