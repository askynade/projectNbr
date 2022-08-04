from knox.views import LogoutView
from django.urls import path,include
from .views import *
from rest_framework import routers
# from adminmodule import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('UserListView', UserListView)

urlpatterns = [
    
    path('adminLoginAPI',AdminLoginAPI.as_view(),name="adminLogin"),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    path('', include(router.urls))

]