from django.urls import path
from .views import index, getTasks, getSubTasks

# ============================================================================#
urlpatterns = [
    path('', index, name='api_index'),
    path('tasks/', getTasks, name='tasks'),
    path('sub_tasks/', getSubTasks, name='sub_tasks'),
]
