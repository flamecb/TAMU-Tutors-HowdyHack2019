"""TAMU_tutors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from tutor_match import views as tutor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tutor_views.index, name='Home'),
    path('signup/', tutor_views.register, name="register"),
    path('login/', tutor_views.login, name='Login'),
    path('search/', tutor_views.search, name='Search'),
    path('profile/', tutor_views.profile, name='Profile'),
    path('new_profile', tutor_views.newProfile, name='New_Profile')
    #path('test/', tutor_views.test, name='Test')
]
