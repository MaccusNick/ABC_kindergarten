from .models import (
    Parent,
    Manager,
    Teacher,
    Announcement,
    TeacherSchedule,
    Classroom,
    Camera,
    Child,
    ChildSchedule,
    Story,
    SickForm,
    Payment,
    Image,
    Account,
)
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import viewsets, permissions, generics
from .serializers import AccountSerializer, ParentSerializer,  UserSerializer, RegisterSerializer, LoginSerializer
from .serializers import ImageSerializer, PaymentSerializer, SickFormSerializer, StorySerializer
from .serializers import ChildSerializer, CameraSerializer, ChildScheduleSerializer, ClassroomSerializer
from .serializers import TeacherScheduleSerializer, TeacherSerializer, AnnouncementSerializer, ManagerSerializer


# Account Viewset

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ParentSerializer


class ChildScheduleViewSet(viewsets.ModelViewSet):
    queryset = ChildSchedule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ChildScheduleSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ChildSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherSerializer


class TeacherScheduleViewSet(viewsets.ModelViewSet):
    queryset = TeacherSchedule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherScheduleSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ManagerSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnnouncementSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassroomSerializer


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CameraSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StorySerializer


class SickFormViewSet(viewsets.ModelViewSet):
    queryset = SickForm.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SickFormSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PaymentSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
