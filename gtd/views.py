from django.shortcuts import render

# Create your views here.

def task_list(request):
    return render(request, 'gtd/task_list.html', {})
