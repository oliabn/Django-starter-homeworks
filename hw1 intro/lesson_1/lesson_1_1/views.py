from django.shortcuts import render
from django.http import HttpResponse


def lesson_1(request):
    return render(request, 'lesson_1_1/lesson_1.html')


def lesson_1_1(request):
    return render(request, 'lesson_1_1/lesson_1_1.html')

def home(request):
    return render(request, 'lesson_1_1/home.html')
