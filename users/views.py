from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Task, Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    tasks = Task.objects.filter(author=request.user)
    context = {'tasks': tasks}
    return render(request, 'users/profile.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        task_content = request.POST['task']
        task_title = request.POST['title']
        t = Task.objects.create(title=task_title,
                                task=task_content,
                                author=request.user)
        t.save()
        return redirect('users-profile')
    return render(request, 'users/createtask.html')

@login_required
def delete_task(request):
    if request.method == 'POST':
        id = request.POST['delete']
        task = get_object_or_404(Task, pk=int(id))
        task.delete()
        return redirect('users-profile')
