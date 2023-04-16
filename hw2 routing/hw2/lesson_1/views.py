from django.shortcuts import render
from django.http import HttpResponse


def lesson1(request, url_remainder):
    return HttpResponse(f'<h1>Task2: Lesson_1</h1> <p>Url remainder: {url_remainder}</p>')
