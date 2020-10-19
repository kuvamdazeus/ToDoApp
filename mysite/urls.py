"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin # admin is feature which provides adminstrator access to our project

from django.urls import path, include # path is function used for this mapping purpose

# include function redirects users to urls.py of an app

# Here our app name is : "SimpleApp"

urlpatterns = [
    path('admin/', admin.site.urls), # says user browser to run a function
    path('', include('SimpleApp.urls')), # passes the control to "SimpleApp.urls" or urls.py file of SimpleApp
]
