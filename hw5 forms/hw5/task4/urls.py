from django.urls import path
from .views import *


urlpatterns = [
    # Response form page
    # http://127.0.0.1:8000/task4/add_review/
    path('add_review/', ReviewAddingFormView.as_view(), name='add_review'),
    # Review pages
    # http://127.0.0.1:8000/task4/review/<review_pk>/
    path('review/<int:review_pk>/', show_review, name='review'),
]
