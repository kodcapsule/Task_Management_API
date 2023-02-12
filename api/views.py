from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Task, Sub_Task
from . serializers import TaskSerializer, SubTaskSerializer

# ============================================================================#


def index(request):
    return HttpResponse('<h1>API application</h1>')


@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSubTasks(request):
    sub_tasks = Sub_Task.objects.all()
    serializer = SubTaskSerializer(sub_tasks, many=True)
    return Response(serializer.data)
