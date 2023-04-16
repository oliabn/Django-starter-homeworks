from django.urls import path
from .views import *

urlpatterns = [
    path('', questions),
    path('<int:question_id>/', question),
]