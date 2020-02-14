from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('index/',index),
    path('about',about),
    path('gbook/',gbook),
    path('info/',info),
    path('list/',list),
    path('gbook/',gbook),
    path('base/',base)
]