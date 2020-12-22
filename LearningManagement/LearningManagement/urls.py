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
from django.urls import include, path
from learn import views
from django.conf.urls.static import static
from machina import urls as machina_urls
from django.contrib.auth import views as auth_views
from machina.apps import forum_member

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('home2',views.home2, name='home2'),
    path('imdb', views.imdb, name='imdb'), # Url for the page where we process the api, 1st parameter: url name, second parameter: function in the views.py where the api processing is implemented, third name: way to reach page in html template.
    path('home3', views.home3, name='home3'),
    path('home4', views.home4, name='home4'),
    path('ebooks', views.ebooks, name='ebooks'),
    path('youtubeplay',views.youtubeplay, name='youtubeplay'),
    path('forum/', include(machina_urls)),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="learn/login.html"),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name="learn/logout.html"), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('trendySkills/', views.trendySkills, name="trends"),
    path('userProfile/<int:pk>',forum_member.views.ForumProfileDetailView.as_view(),name='profile'),

]
