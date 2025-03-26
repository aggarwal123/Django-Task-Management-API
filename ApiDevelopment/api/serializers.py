from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile']


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False
    )
    class Meta:
        model = Task
        fields = [
            'id', 'name', 'description', 'created_at', 'task_type', 
            'completed_at', 'status', 'assigned_users'
        ]
        read_only_fields = ['id', 'created_at', 'completed_at']

    def create(self, validated_data):
        # Pop assigned_users if exists
        assigned_users = validated_data.pop('assigned_users', [])
        task = Task.objects.create(**validated_data)
        task.assigned_users.set(assigned_users)  # Assign users to task
        return task

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status']
