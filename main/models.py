from django.db import models


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
    Title = models.TextField
    Content = models.TextField
    Date = models.DateField


class TeacherSchedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    StartTime = models.DateField


class Classroom(models.Model):
    tSchedule = models.ForeignKey(TeacherSchedule, on_delete=models.CASCADE)
    Capacity = models.SmallIntegerField


class Camera(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    Location = models.CharField(max_length=40)


class Parent(models.Model):
    Parentid = models.AutoField(db_column='id', primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'main_parent'


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    ChildStatus = models.BooleanField


class ChildSchedule(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    StartTime = models.DateField


class Story(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    StoryContent = models.TextField
    CreateDate = models.DateField


class SickForm(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    FormTitle = models.CharField
    FormContent = models.TextField


class Payment(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    PaymentTitle = models.TextField
    PaymentStatus = models.BooleanField


class Image(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    ImageName = models.CharField(max_length=50)
    CreatedDate = models.DateField
    Description = models.TextField
