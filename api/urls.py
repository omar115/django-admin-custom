from django.conf.urls import url 
from django.urls import path 
from .views import *

urlpatterns = [
    path('products/',ProductListApiView.as_view()),
    path('products/update/',ProductUpdateView.as_view()),
]