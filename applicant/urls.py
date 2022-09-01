from knox.views import LogoutView
from django.urls import path,include
from .views import *
from . import views
from rest_framework import routers



urlpatterns = [
    path('userlogin',LoginAPI.as_view(),name="userlogin"),
    path('useregister',UserRegisterAPI.as_view(),name="useregister"),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    
    
    path('UpdateUserDetails/<str:pk>/',views.UpdateUserDetails),
    path('ApplicantDetailView',views.ApplicantDetailView),



    path('UpdatePersonalInformation',views.UpdatePersonalInformation),
    path('UpdateIncomeAndDomicileInfo',views.UpdateIncomeAndDomicileInfo),
    path('UpdateEligibilityInfo',views.UpdateEligibilityInfo),
    path('UpdateBankInformation',views.UpdateBankInformation),
    path('UpdateResidentialInfo',views.UpdateResidentialInfo),
    path('UpdateQualificationInfo',views.UpdateQualificationInfo),
    path('UpdateOtherInfo',views.UpdateOtherInfo),
    path('UpdateSchemeDetails',views.UpdateSchemeDetails),


    
]