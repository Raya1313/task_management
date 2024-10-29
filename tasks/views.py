from django.shortcuts import render
from tasks.models import Task
from django.http import Http404


def menu(request):
    return render(request, 'tasks/base.html')


def task_details(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404
    return render(
        request,
        'tasks/task/details.html',
        {'task': task}
    )


def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/task/list.html',
        {'tasks': tasks}
    )


def set_status(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = not task.is_completed
    task.save()

    return render(
        request,
        'tasks/task/details.html',
        {'task': task}
    )


def filter_tasks(request, status: int):
    is_completed = bool(status)
    tasks = Task.objects.filter(is_completed=is_completed)
    return render(
        request,
        'tasks/task/list.html',
        {'tasks': tasks}
    )
