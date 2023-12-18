from django.shortcuts import render

def my_project(request):
    return render(request, 'my_project.html')
