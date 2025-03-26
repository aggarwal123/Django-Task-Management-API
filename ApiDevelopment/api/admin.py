from django.contrib import admin
from .models import User, Task


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','mobile')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','description','task_type','status','created_at')

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(Task, TaskAdmin)
