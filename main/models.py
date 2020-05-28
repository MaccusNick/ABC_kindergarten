from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Manager(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

    def __str__(self):
        return self.FirstName


class Teacher(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)


class Announcement(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Title = models.TextField(blank=True, null=True)
    Content = models.TextField(blank=True, null=True)
    Date = models.DateTimeField(auto_now=False)


class TeacherSchedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    StartTime = models.DateTimeField(auto_now=False)


class Classroom(models.Model):
    tSchedule = models.ForeignKey(TeacherSchedule, on_delete=models.CASCADE)
    Capacity = models.SmallIntegerField(default=22)


class Camera(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    Location = models.CharField(max_length=40)


class Parent(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

    # class Meta:
    #     managed = False
    #     db_table = 'main_parent'


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    ChildStatus = models.BooleanField(default=False)


class ChildSchedule(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    StartTime = models.DateTimeField(auto_now=False)


class Story(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    StoryContent = models.TextField(blank=True, null=True)
    CreateDate = models.DateTimeField(auto_now=False)


class SickForm(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    FormTitle = models.TextField(blank=True, null=True)
    FormContent = models.TextField(blank=True, null=True)


class Payment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    PaymentTitle = models.TextField(blank=True, null=True)
    PaymentStatus = models.BooleanField(default=False)


class Image(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    ImageName = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now=False)
    Description = models.TextField(blank=True, null=True)


class Account(models.Model):
    Email = models.CharField(max_length=20, unique=True)
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Created_at = models.DateTimeField(auto_now=True)
