"""
URL configuration for hw3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    path('to_do_list/', include('to_do_list.urls')),
    path('star_wars/', include('star_wars.urls')),
    path('get_file/', include('send_file.urls')),
    path('response_types/', include('different_types_of_response.urls')),

    # http://127.0.0.1:8000/dune/
    path('dune/', include('dune.urls')),
    path('questions/', include('questions.urls')),
]
