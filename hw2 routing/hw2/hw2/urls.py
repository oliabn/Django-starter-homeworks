from django.contrib import admin
from django.urls import path, include
# from .weather.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main page with all links from tasks
    path('', include('hw2_tasks.urls')),
    # Task1
    path('home/', include('home.urls')),
    path('book/<str:title>/', include('book.urls')),
    path('lesson_2/<path:url_remainder>/', include('lesson_2.urls')),
    # Task2
    path('lesson_1/<path:url_remainder>/', include('lesson_1.urls')),
    path('index/', include('index.urls')),
    path('bio/<str:username>/', include('bio.urls')),
    # Task3
    path('weather/<str:city>/', include('weather.urls')),
]

# handler404 = pageNotFound
