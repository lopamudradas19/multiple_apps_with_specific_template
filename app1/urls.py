app_name='msd'
from django.urls import path
from app1.views import*
urlpatterns=[
    path('Ram/',Ram,name='Ram'),
]