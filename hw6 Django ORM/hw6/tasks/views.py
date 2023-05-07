from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Author, Book


class BooksView(TemplateView):
    template_name = 'tasks/books.html'

    def get(self, request):
        context = {
            # get all books from db sorted by date
            'all_books': Book.objects.all().order_by('-pub_date'),
            # get book with name='The Green Mile'
            'name_filter': Book.objects.filter(name='The Green Mile'),
            # get book with author surname ='King'
            'author_surname': Book.objects.filter(author__surname='King'),
            # get books where year in pub_date: 1005 < pub_date < 2015
            'books_of_some_period': Book.objects.filter(pub_date__year__gte=2005, pub_date__year__lte=2015),
            # get books whose names start with the letter "T"
            'books_with_some_letter': Book.objects.all().filter(name__startswith='T'),
            # get books whose names contain "100"
            'books_with_number': Book.objects.all().filter(name__contains='100'),
        }
        return render(request, self.template_name, context)
