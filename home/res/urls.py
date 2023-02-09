"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('food',views.food,name="food"),
    path('onlinefood',views.onlinefood,name="onlinefood"),
    path('handlesignup',views.handlesignup,name='handlesignup'),
    path('loginuser',views.loginuser,name ='loginuser'),
    path('logoutuser',views.logoutuser,name ='logoutuser'),
    path('booktable/',views.booktable,name="booktable"),
    path('contact/',views.contactus,name="contact"),
    path('orderfood',views.orderfood,name="orderfood"),
    path('order',views.order,name="order"),
    path('orderfood/<int:order_id>',views.orderfood,name="orderfood"),
    path('verify/<auth_token>',views.verify,name="verify"),
]
