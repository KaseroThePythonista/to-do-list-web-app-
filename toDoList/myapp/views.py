from django.shortcuts import render
from myapp.forms import TaskForm
from myapp.models import Task_manager


# Create your views here.

def index(request):

    task_data = Task_manager.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'task_data':task_data, 'form':form}

    return render(request, 'myapp/index.html', context)


def clear(request):
    form = TaskForm()
    Task_manager.objects.all().delete()
    return render(request,'myapp/index.html', {'form':form})

