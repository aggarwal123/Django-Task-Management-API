from django.urls import path
from .views import CreateTaskAPIView, AssignTaskAPIView, UserTasksAPIView

urlpatterns = [
    path('tasks', CreateTaskAPIView.as_view(), name='create-task'),
    path('tasks/assign', AssignTaskAPIView.as_view(), name='assign-task'),
    path('tasks/user/<int:user_id>', UserTasksAPIView.as_view(), name='user-tasks'),
]
