from django.contrib import admin
from django.urls import path
from mini_url.views import *

urlpatterns = [
    path('', liste, name='url_liste'),
    path('nouveau/', nouveau, name='url_nouveau'),
    path('<str:code>\w{6}/', redirection, name='url_redirection')

]
