from django.urls import path, re_path
from apps.services.api.api import *

urlpatterns = [
    path('category/', categories, name='categories_api'),
    path('cart/', cart, name='cart_api'),
]
