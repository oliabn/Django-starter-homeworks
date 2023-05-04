from django.urls import path
from .views import *


urlpatterns = [
    # Article form page
    # http://127.0.0.1:8000/task3/add_article/
    path('add_article/', ArticleAddingFormView.as_view(), name='add_article'),
    # Articles pages
    # http://127.0.0.1:8000/task3/article/<article_slug>/
    path('article/<slug:article_slug>/', show_post, name='article'),
]