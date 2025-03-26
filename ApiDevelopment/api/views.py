from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, Task
from .serializers import TaskSerializer, TaskListSerializer
import json


# 1️ API to create a task
class CreateTaskAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2️ API to assign a task to a user
class AssignTaskAPIView(APIView):
    def post(self, request):
        task_id = request.data.get("task_id")
        user_ids = request.data.get("user_ids")  # Expecting a string of list of user IDs example: "[1,2,3]"
        # try:
        #     user_ids = json.loads(user_ids_str)  # Convert to a Python list
        # except json.JSONDecodeError:
        #     user_ids = []
        task = get_object_or_404(Task, id=task_id)
        users = User.objects.filter(id__in=user_ids)

        if not users.exists():
            return Response({"error": "Users not found"}, status=status.HTTP_404_NOT_FOUND)

        task.assigned_users.set(users)  # Assign task to users
        task.save()

        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)


# 3️ API to get tasks assigned to a user
class UserTasksAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        tasks = user.tasks.all()  # Retrieve tasks assigned to this user
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
