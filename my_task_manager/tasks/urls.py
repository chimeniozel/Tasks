from django.urls import path
from .views import *

urlpatterns = [
    path('', get_tasks, name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('tasks/create/', create_task, name='task-create'),
    path('tasks/<int:task_id>/update/', update_task, name='task-update'),
    path('tasks/<int:task_id>/delete/', delete_task, name='task-delete'),
]
