from django.urls import path
from .views import index, getTasks, getSubTasks,  getUsers, addTask, modifyTask

# ============================================================================#
urlpatterns = [
    path('', index, name='api_index'),
    path('tasks/', getTasks, name='tasks'),
    path('add_task/', addTask, name='add_task'),
    path('delete_task/<str:id>', modifyTask, name='dele_task'),
    path('users/', getUsers, name='users'),
    path('sub_tasks/', getSubTasks, name='sub_tasks'),
]
