from django.shortcuts import render
from django.http import HttpResponse


def bio(request, username: str):
    return HttpResponse(f'<h1>Task2: BIO</h1> <p>Username: {username}</p>')
