app_name='rcv'
from django.urls import path
from app2.views import*
urlpatterns=[
    path('Hari/',Hari,name='Hari'),
]