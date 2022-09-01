from django.shortcuts import render
from django.http import JsonResponse
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework import generics,permissions
from django.contrib.auth.models import Group
from applicant.serializers import *
from database.models import *
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser,MultiPartParser,FileUploadParser,FormParser
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
            


# Create your views here.
class UserRegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    parser_classes = [MultiPartParser]

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            customuser = serializer.validated_data
            data = UserSerializer(customuser,context=self.get_serializer_context()).data
            red1 = PersonalInformation(user=user)
            red1.save()
            
            red2 = IncomeAndDomicileInfo(user=user)
            red2.save()
            
            red3 = EligibilityInfo(user=user)
            red3.save()
            
            red4 = BankInformation(user=user)
            red4.save()
            
            red5 = QualificationInfo(user=user)
            red5.save()
            
            red6 = OtherInfo(user=user)
            red6.save()
            
            red = ResidentialInfo(user=user)
            red.save()
            # groupUser = CustomUser.objects.get(id = customuser.id)
            group = Group.objects.get(name='beneficary')
            user.groups.add(group)
            return Response({
                "status":"success",
                "message":"Successfully Registered.",
                "data":data,
                })
        else:
            # print(serializer)
            # print(serializer.errors)

            return Response({
                "status":"error",
                "message":serializer.errors
             
                })



@permission_classes((IsAuthenticated, ))
@api_view(['Get'])
def ApplicantDetailView(request):
    # pagination = PageNumberPagination
    # pagination.page_size = 2
    comDet = CustomUser.objects.get(id=request.user.id)
    # pageResp = pagination.pagination_queryset(AllCompanyDetail,request)
    serializer = UserViewSerializer(comDet,many=False)
    # return pagination.get_paginated.response(serializer.data)
    return Response(serializer.data)

@swagger_auto_schema(method='PATCH', request_body=UpdateUserSerializer)
@api_view(['Patch'])
@parser_classes((MultiPartParser,))
@permission_classes((IsAuthenticated, ))
def UpdateUserDetails(request):
    comDet = CustomUser.objects.get(id=request.user.id)
    serializer  = UpdateUserSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@swagger_auto_schema(method='PATCH', request_body=PersonalInformationSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdatePersonalInformation(request):
    comDet = PersonalInformation.objects.get(user__id=request.user.id)
    serializer  = PersonalInformationSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        # CustomUser.objects.filter(id=request.user.id).update(name=request.data["name"],emailId=request.data["emailId"])
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@swagger_auto_schema(method='PATCH', request_body=IncomeAndDomicileInfoSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateIncomeAndDomicileInfo(request):
    comDet = IncomeAndDomicileInfo.objects.get(user_id=request.user.id)
    serializer  = IncomeAndDomicileInfoSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@swagger_auto_schema(method='PATCH', request_body=EligibilityInfoSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateEligibilityInfo(request):
    comDet = EligibilityInfo.objects.get(user_id=request.user.id)
    serializer  = EligibilityInfoSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@swagger_auto_schema(method='PATCH', request_body=BankInformationSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateBankInformation(request):
    comDet = BankInformation.objects.get(user_id=request.user.id)
    serializer  = BankInformationSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@swagger_auto_schema(method='PATCH', request_body=ResidentialInfoSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateResidentialInfo(request):
    comDet = ResidentialInfo.objects.get(user_id=request.user.id)
    serializer  = ResidentialInfoSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        dtemp = serializer.save()
        return Response(dtemp.data)

    else:
        return Response(serializer.errors)


@swagger_auto_schema(method='PATCH', request_body=QualificationInfoSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateQualificationInfo(request):
    comDet = QualificationInfo.objects.get(user_id=request.user.id)
    serializer  = QualificationInfoSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@swagger_auto_schema(method='PATCH', request_body=OtherInfoSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateOtherInfo(request):
    comDet = OtherInfo.objects.get(user_id=request.user.id)
    serializer  = OtherInfoSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@swagger_auto_schema(method='PATCH', request_body=SchemeDetailsSerializer)
@api_view(['Patch'])
@permission_classes((IsAuthenticated, ))
def UpdateSchemeDetails(request,pk):
    comDet = SchemeDetails.objects.get(id=pk)
    serializer  = SchemeDetailsSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)