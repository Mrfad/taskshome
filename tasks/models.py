from django.db import models
from django.contrib.auth.models import User
from suppliers.models import Currency
from customers.models import Customer, Account
from users.models import Profile


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    project_balance = models.DecimalField(max_digits=20, decimal_places=2)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    notes = models.TextField()

    def __str__(self):
        return str(self.project_name)

class TaskPriority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    task_priority_name = models.CharField(max_length=200)

    class Meta: 
        verbose_name = "Task Priority"
        verbose_name_plural = "Tasks Priority"

    def __str__(self):
        return str(self.task_priority_name)

class TaskProgressStatus(models.Model):
    progress_status_id = models.AutoField(primary_key=True)
    progress_status_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.progress_status_name)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=200)
    task_progress = models.ForeignKey(TaskProgressStatus, on_delete=models.CASCADE, blank=True, null=True)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    task_priority = models.ForeignKey(TaskPriority, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User,related_name='assigned_to', on_delete=models.CASCADE, default=1)
    paid = models.BooleanField(default=False)
    on_account = models.BooleanField(default=False)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE,  blank=True, null=True)
    net_amount = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    # rest_amount = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    delivered = models.BooleanField(default=False)
    delivered_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    create_by = models.ForeignKey(User, related_name='created_by_username', on_delete=models.CASCADE, default=1)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    file_name = models.FileField(upload_to='projects_files', null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return str(self.task_name)



