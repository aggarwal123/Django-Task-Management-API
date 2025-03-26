from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from api.models import User, Task
import random

class Command(BaseCommand):
    help = "Populate the database with dummy data"

    def handle(self, *args, **kwargs):
        for i in range(1,11):
            # Create Users
            user = User.objects.create(
                name=f"User {i}",
                email=f"user{i}@example.com",
                mobile=f"12345678{i:02}",
                username=f"user{i}",
                password=make_password("1234")
            )

            # Create Tasks
            task = Task.objects.create(
                name=f"Task {i}", 
                description=f"Description for task {i}", 
                task_type=random.choice(["Development", "Testing", "Deployment"]),
                status=random.choice(["pending", "in_progress"]),
            )

            # Assign Users to Tasks
            task.assigned_users.add(user)

        self.stdout.write(self.style.SUCCESS("Dummy data successfully added!"))
