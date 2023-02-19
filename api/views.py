# from django.shortcuts import render
# from django.http import HttpResponse


# ============================================================================#
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.models import User
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_200_OK
# ============================================================================#


# ============================================================================#
from base.models import Task, Sub_Task
from . serializers import TaskSerializer, SubTaskSerializer, UserSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
# ============================================================================#


@api_view(['GET'])
def index(request):
    api_endpoints = {'Description': 'a list of end points for tasks api', 'index': 'api/v1/',
                     'tasks': 'api/v1/tasks/', 'subtask': 'api/v1/sub_tasks/'}
    return Response(api_endpoints)


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def addTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        print(request.data)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAdminUser])
def modifyTask(request, id):
    if request.method == 'DELETE':
        task = Task.objects.get(Task_Id=id)
        serializer = TaskSerializer(task)
        task.delete()
        return Response(serializer.data, status=HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        task = Task.objects.get(Task_Id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET'])
def getUsers(request):
    if request.user:
        users = User.objects.filter(username=request.user)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getSubTasks(request):
    if request.method == 'GET':
        sub_tasks = Sub_Task.objects.filter(asigned_to=request.user)
        serializer = SubTaskSerializer(sub_tasks, many=True)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        sub_task = Sub_Task.objects.get()
        serializer = SubTaskSerializer(data=request.data)
        print(request.data)
