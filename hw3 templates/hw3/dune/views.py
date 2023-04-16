from django.shortcuts import render


def dune(request):
    dune_data = [{'name': 'Shaddam IV', 'surname': 'Corrino'},
                 {'name': 'Paul', 'surname': 'Atreides'},
                 {'name': 'Franklin-Patrick', 'surname': 'Herbert'}]
    return render(request, 'dune/dune.html', context={'dune_data': dune_data})
