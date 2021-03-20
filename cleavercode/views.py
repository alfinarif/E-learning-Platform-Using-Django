from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'contact.html')

def Course(request):
    return render(request, 'courses.html')

def Details(request):
    return render(request, 'single-course.html')
