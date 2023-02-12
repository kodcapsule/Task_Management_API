from rest_framework.serializers import ModelSerializer

from base.models import Task, Sub_Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['Title', 'Description',
                  'Date_Created', 'Last_Modified', 'Completed']


class SubTaskSerializer(ModelSerializer):
    class Meta:
        model = Sub_Task
        fields = ['Title', 'Description',
                  'Date_created', 'Due_date', 'Last_modified']
