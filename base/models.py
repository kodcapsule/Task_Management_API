from django.db import models
from django.contrib.auth.models import User
# Create your models here.

import uuid


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    User_Id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    # def ___str__(self):
    #     return self.Title


class Task(models.Model):
    Task_Id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(
        max_length=500, unique=True, blank=False, null=False)
    Description = models.TextField(default='New task')
    Date_Created = models.DateTimeField(auto_now_add=True)
    Last_Modified = models.DateTimeField(auto_now=True)
    Completed = models.BooleanField(default=False)
    asigned_to = models.ManyToManyField('User')

    def ___str__(self):
        return self.Title


class Sub_Task (models.Model):
    Sub_Task_Id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(
        max_length=500, unique=True, blank=False, null=False)
    Description = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True)
    Due_date = models.DurationField()
    Last_modified = models.DateTimeField(auto_now=True)
    Completed = models.BooleanField(default=False)
    Reminder = models.BooleanField(default=True)
    main_Task = models.ForeignKey('Task', on_delete=models.CASCADE)
    asigned_to = models.ForeignKey('User', on_delete=models.CASCADE)

    def ___str__(self):
        return self.Title
