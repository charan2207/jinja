from app19.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('jinja/',jinja,name='jinja'),
    
]