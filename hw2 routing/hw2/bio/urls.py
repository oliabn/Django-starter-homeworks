from django.urls import path
from .views import *

urlpatterns = [
    path('', bio, name='bio'),
]
