from django.urls import path
from .views import *

urlpatterns = [
    path('', BooksView.as_view(), name='books_view'),
]
