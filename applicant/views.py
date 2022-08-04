from django.shortcuts import render
from django.http import JsonResponse
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import generics,permissions
from django.contrib.auth.models import Group
from applicant.serializers import UserSerializer,UserLoginSerializer,RegisterSerializer
from database.models import *
from datetime import datetime
# Create your views here.
class LoginAPI(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customuser = serializer.validated_data
            _, token = AuthToken.objects.create(customuser)
            CustomUser.objects.filter(id=customuser.id).update(updatedDate=datetime.now())
            status = CustomUser.objects.filter(id=customuser.id)
            data = UserSerializer(customuser,context=self.get_serializer_context()).data
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
            


# Create your views here.
class UserRegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            customuser = serializer.validated_data
            data = UserSerializer(customuser,context=self.get_serializer_context()).data


            return Response({
                "status":"success",
                "message":"Successfully Registered.Otp send on your Registered Mobile Number please verify it.",
                "data":{"uniqueId":data["uniqueId"]},
                })
        else:
            # print(serializer)
            # print(serializer.errors)

            return Response({
                "status":"error",
                "message":serializer.errors["non_field_errors"][0]
             
                })


