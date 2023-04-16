from django.urls import path
from .views import *

urlpatterns = [
    path('lesson_1/', lesson_1),
    path('lesson_1_1/', lesson_1_1),
    path('', home),
]
