from django.urls import path
from .views import index, getTasks, getSubTasks, addTask

# ============================================================================#
urlpatterns = [
    path('', index, name='api_index'),
    path('tasks/', getTasks, name='tasks'),
    path('add_task/', addTask, name='add_task'),
    path('sub_tasks/', getSubTasks, name='sub_tasks'),
]
