from django.urls import path
from .views import index, getTasks, getSubTasks,  getUsers

# ============================================================================#
urlpatterns = [
    path('', index, name='api_index'),
    path('tasks/', getTasks, name='tasks'),
    path('users/', getUsers, name='users'),
    path('sub_tasks/', getSubTasks, name='sub_tasks'),
]
