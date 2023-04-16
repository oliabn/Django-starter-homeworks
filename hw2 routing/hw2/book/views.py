from django.shortcuts import render
from django.http import HttpResponse


def book(request, title: str):
    return HttpResponse(f'<h1>Task1: Book</h1> <p>Title: {title}</p>')
