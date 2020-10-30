from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from knox import views as knox_views

from .api import RegisterAPI, LoginAPI
from rest_framework import routers
from .api import AccountViewSet, ParentViewSet, ChildScheduleViewSet, ChildViewSet, TeacherViewSet, CameraViewSet
from .api import TeacherScheduleViewSet, ClassroomViewSet, StoryViewSet, SickFormViewSet, PaymentViewSet, ImageViewSet
from .api import ManagerViewSet, AnnouncementViewSet, RegisterAPI
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register('api/Account', AccountViewSet, 'Account')
router.register('api/ParentView', ParentViewSet, 'Parent')
router.register('api/ChildScheduleView', ChildScheduleViewSet, 'ChildSchedule')

router.register('api/ChildView', ChildViewSet, 'Child')
router.register('api/TeacherView', TeacherViewSet, 'Teacher')
router.register('api/CameraView', CameraViewSet, 'Camera')
router.register('api/TeacherScheduleView', TeacherScheduleViewSet, 'TeacherSchedule')
router.register('api/ClassroomView', ClassroomViewSet, 'Classroom')
router.register('api/StoryView', StoryViewSet, 'Story')
router.register('api/SickFormView', SickFormViewSet, 'SickForm')
router.register('api/PaymentView', PaymentViewSet, 'Payment')
router.register('api/ImageView', ImageViewSet, 'Image')
router.register('api/ManagerView', ManagerViewSet, 'Manager')
router.register('api/AnnouncementView', AnnouncementViewSet, 'Announcement')
# router.register('api/RegisterAPI', RegisterAPI, 'Register')

urlpatterns = [

    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('', TemplateView.as_view(template_name='index.html'))
]

# urlpatterns = [
#     path("", views.index, name="index"),
#     path('parent/all', views.ParentListView.as_view()),
#     # path('parent/<int:Parentid>/detail', views.ParentDetailView.as_view()),
#     path('Manager/all', views.ManagerListView.as_view()),
#     path('api/auth', include('knox.urls')),
#     path('api/auth/register', views.RegisterAPI.as_view()),
#     path('api/auth/login', views.LoginAPI.as_view()),
# ]
