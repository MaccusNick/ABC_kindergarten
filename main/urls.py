from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('parent/all', views.ParentListView.as_view()),
    path('parent/<int:Parentid>/detail', views.ParentDetailView.as_view()),

]