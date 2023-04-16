from django.urls import path
from .views import *

urlpatterns = [
    path('', star_wars),
    path('luke/', luke),
    path('leia/', leia),
    path('hun/', hun),
]
