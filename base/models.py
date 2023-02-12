from django.db import models
from django.contrib.auth.models import User


import uuid
import datetime

#
# class User(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     User_Id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False)
#     Username = models.CharField(max_length=200, unique=True)

#     def ___str__(self):
#         return self.Username


class Task(models.Model):
    Task_Id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(
        max_length=500, unique=True, blank=False, null=False)
    Description = models.TextField(default='New task')
    Date_Created = models.DateTimeField(auto_now_add=True)
    Last_Modified = models.DateTimeField(auto_now=True)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title


class Sub_Task (models.Model):
    Sub_Task_Id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(
        max_length=250, unique=True, blank=False, null=False)
    Description = models.TextField()
    Date_created = models.DateTimeField(auto_now_add=True)
    Due_date = models.DurationField(default=datetime.timedelta(days=7))
    Last_modified = models.DateTimeField(auto_now=True)
    Completed = models.BooleanField(default=False)
    Reminder = models.BooleanField(default=True)
    main_Task = models.ForeignKey('Task', on_delete=models.CASCADE)
    asigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
