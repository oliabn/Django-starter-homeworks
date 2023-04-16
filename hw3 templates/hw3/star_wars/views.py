from django.shortcuts import render


def star_wars(request):
    return render(request, 'star_wars/star_wars.html')


def luke(request):
    return render(request, 'star_wars/luke.html')


def leia(request):
    return render(request, 'star_wars/leia.html')


def hun(request):
    return render(request, 'star_wars/hun.html')
