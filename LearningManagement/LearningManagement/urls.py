"""LearningManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from learn import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('home2',views.home2, name='home2'),
    path('imdb', views.imdb, name='imdb'), # Url for the page where we process the api, 1st parameter: url name, second parameter: function in the views.py where the api processing is implemented, third name: way to reach page in html template.
    path('home3', views.home3, name='home3'),
    path('home4', views.home4, name='home4'),
    path('ebooks', views.ebooks, name='ebooks'),
    path('youtubeplay',views.youtubeplay, name='youtubeplay'),
]
