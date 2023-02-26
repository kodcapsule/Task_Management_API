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


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def getTasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'PUT', 'PATCH'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def modifyTask(request, id):
    if request.method == 'DELETE':
        task = Task.objects.get(Task_Id=id)
        serializer = TaskSerializer(task)
        task.delete()
        return Response(serializer.data, status=HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        task = Task.objects.get(Task_Id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @authentication_classes([BasicAuthentication])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(request.auth)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getSubTasks(request):
    if request.method == 'GET':
        sub_tasks = Sub_Task.objects.all()
        serializer = SubTaskSerializer(sub_tasks, many=True)
        return Response(serializer.data)
    elif (request.method == 'POST'):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSubTask(request):
    if request.method == "GET":
        sub_task = Sub_Task.objects.filter(username=request.user)
        serializer = SubTaskSerializer(sub_task, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def modifySubTask(request, id):
    if request.method == 'PUT':
        sub_task = Sub_Task.objects.get(Sub_Task_Id=id)
        serializer = SubTaskSerializer(sub_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
