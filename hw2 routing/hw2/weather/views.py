from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, Http404
from .get_weather import get_weather


def weather(request, city: str):
    return render(request, 'weather.html', context=get_weather(city))


# def pageNotFound(request, exception):
#     return HttpResponseNotFound("<h1>Page not found</h1>")
