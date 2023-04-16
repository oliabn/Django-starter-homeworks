from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse


def http_response(request):
    return HttpResponse("<h3>It's Http response.</h3>")


def file_response(request):
    file = open('different_types_of_response/static/img/dog.jpg', 'rb')
    return FileResponse(file, status=227)


def json_response(request):
    to_do_list = [{'priority': 100, 'task': 'Make a to-do list'},
                  {'priority': 150, 'task': 'Learn Django'},
                  {'priority': 1, 'task': 'Think about the meaning of life'}, ]
    return JsonResponse(to_do_list, safe=False)
