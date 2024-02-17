from django.shortcuts import render, redirect
from . import forms, models


# Create your views here.
def add_task(request):
    if request.method == "POST":
        tsk = forms.taskForm(request.POST)
        if tsk.is_valid():
            tsk.save()
            return redirect("add_task")
    else:
        tsk = forms.taskForm()
    return render(request, "add_task.html", {"form": tsk})


def edit_task(request, id):
    task = models.Task.objects.get(
        pk=id
    )  # kon post edit korte chai sheta filter kore niye ashtesi
    tsk = forms.taskForm(instance=task)
    if request.method == "POST":
        tsk = forms.taskForm(
            request.POST, instance=task
        )  # mane user kichu na kore submit korleo save korte hbe
        if tsk.is_valid():
            tsk.save()
            return redirect("home")

    return render(request, "add_task.html", {"form": tsk})


def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect("home")
