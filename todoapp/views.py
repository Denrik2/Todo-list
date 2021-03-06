from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all()
            messages.success(request, ('Задача добавлена!'))
            return render(request, 'todoapp/home.html', {'todos': todos})
    else:
        todos = Todo.objects.all()
        return render(request, 'todoapp/home.html', {'todos': todos})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, ('Задача удалена!'))
    return redirect('home')


def mark_complete(request, todo_id):  # завершенная задача
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')


def mark_incomplete(request, todo_id):  # незавершенная задача
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('home')


def edit(request, todo_id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=todo_id)
        form = TodoForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ('Задача изменена!'))
            return redirect('home')
    else:
        todo = Todo.objects.get(id=todo_id)
        return render(request, 'todoapp/edit.html', {'todo': todo})
