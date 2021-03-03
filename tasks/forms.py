from django.forms import ModelForm
from .models import Task

class taskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'task_name',
            'task_progress',
            'customer_name',
            'task_priority',
            'assigned_to',
            'paid',
            'on_account',
            'net_amount',
            'delivered',
            'delivered_date',
            'due_date',
            'project',
            'file_name',
            'notes',
        ]