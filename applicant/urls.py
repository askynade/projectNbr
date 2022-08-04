from knox.views import LogoutView
from django.urls import path,include
from .views import *
from rest_framework import routers



urlpatterns = [
    path('userlogin',LoginAPI.as_view(),name="userlogin"),
    path('useregister',UserRegisterAPI.as_view(),name="useregister"),
    path('logout', LogoutView.as_view(), name='knox_logout'),

    
]