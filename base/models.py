from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    Title = models.CharField(max_length=500)
    Description = models.TextField()
    Date_Created = models.DateTimeField()
    Last_Modified = models.DateTimeField()
    Completed = models.BooleanField(default=False)


class Sub_Task (models.Model):
    Title = models.CharField(max_length=500)
    Description = models.TextField()
    Date_created = models.DateTimeField()
    Due_date = models.DateTimeField()
    Last_modified = models.DateTimeField()
    Completed = models.BooleanField(default=False)
    Reminder = models.BooleanField(default=True)
    Main_Task = models.ForeignKey('Task', on_delete=models.CASCADE)
    Asigned_to = models.ForeignKey('User', on_delete=models.CASCADE)
