from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Task, Sub_Task


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['Task_Id', 'Title', 'Description',
                  'Date_Created', 'Last_Modified', 'Completed']


class SubTaskSerializer(ModelSerializer):
    class Meta:
        model = Sub_Task
        fields = ['Sub_Task_Id', 'Title', 'Description',
                  'Date_created', 'Due_date', 'Last_modified']
