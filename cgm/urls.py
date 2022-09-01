from knox.views import LogoutView
from django.urls import path,include
from .views import *
from . import views
from rest_framework import routers



urlpatterns = [
    path('CgmLoginAPI',CgmLoginAPI.as_view(),name="CgmLoginAPI"),
    path('DmLoginAPI',DmLoginAPI.as_view(),name="DmLoginAPI"),
    path('RmLoginAPI',RmLoginAPI.as_view(),name="RmLoginAPI"),
    path('CgmDashboard',views.CgmDashboard),



    path('logout', LogoutView.as_view(), name='knox_logout'),
    
    



    
]