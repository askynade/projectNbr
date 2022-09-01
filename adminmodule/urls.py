from knox.views import LogoutView
from django.urls import path,include
from .views import *
from . import views
from rest_framework import routers
# from adminmodule import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('UserListView', UserListView),
# router.register('ApplicantList', ApplicantList),
# router.register('RMUserListView', RMUserListView),
# router.register('DMUserListView', DMUserListView),
# router.register('CgmUserListView', CgmUserListView)



urlpatterns = [
    
    path('adminLoginAPI',AdminLoginAPI.as_view(),name="adminLogin"),
    
    path('AddCgmAPI',AddCgmAPI.as_view(),name="AddCgmAPI"),
    path('AddRegionalManagerAPI',AddRegionalManagerAPI.as_view(),name="AddRegionalManagerAPI"),
    path('AddDistrictManagerAPI',AddDistrictManagerAPI.as_view(),name="AddDistrictManagerAPI"),
    path('ApplicantList',ApplicantList.as_view(),name="ApplicantList"),
    
    path('VerticalWiseJobCount',views.VerticalWiseJobCount),

    path('InsertJobType',views.InsertJobType),

    path('JobList',JobList.as_view(),name="JobList"),

    path('VerticalList',views.VerticalList),

    path('CgmUpdateDetails/<str:pk>/',views.CgmUpdateDetails),
    path('RmUpdateDetails/<str:pk>/',views.RmUpdateDetails),
    path('DmUpdateDetails/<str:pk>/',views.DmUpdateDetails),


    path('CgmList',views.CgmList),
    path('CgmDetailView/<str:pk>/',views.CgmDetailView),


    path('RmList',views.RmList),
    path('RmDetailView/<str:pk>/',views.RmDetailView),


    path('DmList',views.DmList),
    path('DmDetailView/<str:pk>/',views.DmDetailView),


    path('logout', LogoutView.as_view(), name='knox_logout'),
    path('', include(router.urls)),
    path('BeneficaryRegisterations',BeneficaryRegisterations.as_view()),

]