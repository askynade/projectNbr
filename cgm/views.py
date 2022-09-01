
from django.shortcuts import render
from django.http import JsonResponse
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import generics,permissions
from django.contrib.auth.models import Group
from cgm.serializers import *
from database.models import *
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# Create your views here.


class CgmLoginAPI(generics.GenericAPIView):
    serializer_class = CgmLoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customuser = serializer.validated_data
            _, token = AuthToken.objects.create(customuser)
            CustomUser.objects.filter(id=customuser.id).update(updatedDate=datetime.now())
            status = CustomUser.objects.filter(id=customuser.id)
            data = CgmSerializer(customuser,context=self.get_serializer_context()).data
            # data = CustomUser.objects.select_related().filter(id=customuser.id).values()
            groups=customuser.groups.values_list('name',flat = True)
            print(groups)
            data["user_group"] = groups
  
            return Response({
                "status":"success",
                "message" : "Login Successfully.",
                "data":data,
                "token":token
                })
        else:
            return Response({
                "status":"error",
                "message":serializer.errors["non_field_errors"][0]
             
                })



class RmLoginAPI(generics.GenericAPIView):
    serializer_class = CgmLoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customuser = serializer.validated_data
            _, token = AuthToken.objects.create(customuser)
            CustomUser.objects.filter(id=customuser.id).update(updatedDate=datetime.now())
            status = CustomUser.objects.filter(id=customuser.id)
            data = RmSerializer(customuser,context=self.get_serializer_context()).data
            # data = CustomUser.objects.select_related().filter(id=customuser.id).values()
            groups=customuser.groups.values_list('name',flat = True)
            print(groups)
            data["user_group"] = groups
  
            return Response({
                "status":"success",
                "message" : "Login Successfully. ",
                "data":data,
                "token":token
                })
        else:
            return Response({
                "status":"error",
                "message":serializer.errors["non_field_errors"][0]
             
                })



class DmLoginAPI(generics.GenericAPIView):
    serializer_class = CgmLoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customuser = serializer.validated_data
            _, token = AuthToken.objects.create(customuser)
            CustomUser.objects.filter(id=customuser.id).update(updatedDate=datetime.now())
            status = CustomUser.objects.filter(id=customuser.id)
            data = DmSerializer(customuser,context=self.get_serializer_context()).data
            # data = CustomUser.objects.select_related().filter(id=customuser.id).values()
            groups=customuser.groups.values_list('name',flat = True)
            print(groups)
            data["user_group"] = groups
  
            return Response({
                "status":"success",
                "message" : "Login Successfully. ",
                "data":data,
                "token":token
                })
        else:
            return Response({
                "status":"error",
                "message":serializer.errors["non_field_errors"][0]
             
                })

@permission_classes((IsAuthenticated, ))
@api_view(['Get'])
def CgmDashboard(request):
    data={}
    VerticalBeneficaryCount  =BeneficaryJobApplication.objects.filter(vertical__VerticalName = request.user.departmenName).count()
    ApprovedCount  =BeneficaryJobApplication.objects.filter(vertical__VerticalName = request.user.departmenName,JobApplicationStatus=True).count()
    data["VerticalBeneficaryCount"] = VerticalBeneficaryCount
    data["ApprovedCount"] = ApprovedCount
    return Response(data)