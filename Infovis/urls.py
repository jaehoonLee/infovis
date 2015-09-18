"""Infovis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main, name='home'),
    url(r'^redirect_url/', redirect_url, name='redirect_url'),
    url(r'^products/', products, name='products'),
    url(r'^product/', product, name='products'),
    url(r'^price/', price, name='price'),
    url(r'^time/', time, name='time'),

    url(r'^me/', me, name='me'),
    url(r'^history/', history, name='history'),
    url(r'^requests/', requests, name='requests')


]
