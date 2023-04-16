from django.shortcuts import render


def to_do(request):
    to_do_list = [{'priority': 100, 'task': 'Скласти перелік справ'},
                  {'priority': 150, 'task': 'Вивчати Django'},
                  {'priority': 1, 'task': 'Подумати про сенс життя'},]
    return render(request, 'to_do_list/to_do.html', context={'to_do_list': to_do_list})
