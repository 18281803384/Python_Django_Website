"""
URL configuration for Python_Django_Website project.

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
from django.urls import path

from app01.views import Login, Home

urlpatterns = [
    # 登录页面
    path('index', Login.show_index),
    path('index/user_register', Login.user_register),
    path('index/user_login', Login.user_login),
    path('index/change_password', Login.change_password),
    path('index/image_code',Login.image_code),

    # 首页
    path('home_page', Home.home_page),
]
