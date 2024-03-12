from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Get Tasks
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)
    

def create_task(title, description, start_date_time, completed):
    task = Task.objects.create(title=title, description=description, start_date_time=start_date_time, completed=completed)
    serializer = TaskSerializer(task)
    return JsonResponse(serializer.data, safe=False)


# Update Task
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if 'title' in request.data:
        task.title = request.data['title']
    if 'description' in request.data:
        task.description = request.data['description']
    if 'start_date_time' in request.data:
        task.start_date_time = request.data['start_date_time']
    if 'completed' in request.data:
        task.completed = request.data['completed']
    task.save()
    serializer = TaskSerializer(task)
    return JsonResponse(serializer.data, safe=False)


# Delete Task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully'}, status=204)
