from django.shortcuts import render
from django.http import HttpResponse


def lesson2(request, url_remainder):
    return HttpResponse(f'<h1>Task1: Lesson_2</h1> <p>Url remainder: {url_remainder}</p>')
