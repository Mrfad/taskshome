from django.contrib import admin
from .models import Task, TaskPriority, Project, TaskProgressStatus

admin.site.register(TaskPriority)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(TaskProgressStatus)
