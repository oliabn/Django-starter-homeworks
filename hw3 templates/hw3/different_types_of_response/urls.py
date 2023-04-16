from django.urls import path
from .views import *

urlpatterns = [
    path('http/', http_response),
    path('file/', file_response),
    path('json/', json_response),
]
