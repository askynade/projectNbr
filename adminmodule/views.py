from django.shortcuts import render
from django.http import JsonResponse
from knox.models import AuthToken
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import generics,permissions
from django.contrib.auth.models import Group
from .serializers import AdminSerializer,LoginSerializer,UserViewSerializer
from database.models import *
from datetime import datetime

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class AdminLoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customuser = serializer.validated_data
            _, token = AuthToken.objects.create(customuser)
            CustomUser.objects.filter(id=customuser.id).update(updatedDate=datetime.now())

            status = CustomUser.objects.filter(id=customuser.id)
            print(status)

            data = AdminSerializer(customuser,context=self.get_serializer_context()).data
            groups=customuser.groups.values_list('name',flat = True)
            print(groups)
            data.pop('groups')
            data.pop('user_permissions')
            data["user_group"] = groups
  
            return Response({
                "data":data,
                "token":token
                })
        else:

            return Response({
                "status":"error",
                "message":serializer.errors["non_field_errors"][0]
             
                })


class UserListView(ViewSet):
    queryset = CustomUser.objects.all()

    def list(self, request):
        
        serializer = UserViewSerializer(self.queryset, many=True)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = UserViewSerializer(item)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })
        
    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.queryset.get(pk=kwargs.get('pk'))
    #     serializer = self.serializer_class(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)