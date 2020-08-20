from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Task
from .forms import TaskForm


def index(request):
    task = Task.objects.all()
    form = TaskForm()
    context = {'task': task, 'form': form}
    return render(request, 'task/list.html', context)
