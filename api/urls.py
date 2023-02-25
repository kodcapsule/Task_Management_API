from django.urls import path
from .views import index, getTasks, getSubTasks,  getUsers, modifyTask

# ============================================================================#
urlpatterns = [
    path('', index, name='api_index'),
    path('tasks/', getTasks, name='tasks'),
    path('modify_task/<uuid:id>', modifyTask, name='dele_task'),
    path('users/', getUsers, name='users'),
    path('sub_tasks/', getSubTasks, name='sub_tasks'),
]
