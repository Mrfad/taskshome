from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Profile
from .models import Task
from .forms import taskForm


@login_required
def mytasks(request):
    profile = Profile.objects.all()
    user = request.user
    alltasks = Task.objects.all()
    tasks = Task.objects.filter(assigned_to=user.id)
    context = {'profile':profile, 'tasks':tasks, 'alltasks':alltasks}
    return render (request, 'tasks/taskslist.html', context)

@login_required
def addtask(request):
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.create_by = request.user
            newform.save()
        return HttpResponseRedirect(request.path_info)
    else:                   
        context = {'form': form}
        return render(request, 'tasks/add_task.html', context)

