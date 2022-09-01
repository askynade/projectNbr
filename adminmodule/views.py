# from types import NoneType
from django.shortcuts import render
from django.http import JsonResponse
from knox.models import AuthToken
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import generics,permissions
from django.contrib.auth.models import Group
from .serializers import InsertJobTypeSerializer,JobTypeSerializer,VerticalSerializer,ApplicantExistingViewSerializer,RmregisterSerializer,DmregisterSerializer,AdminSerializer,LoginSerializer,UserViewSerializer,BeneficarySerializer,CgmregisterSerializer
from database.models import *
from datetime import datetime
######################################3
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import openpyxl
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import filters

from django_filters.fields import CSVWidget
from django_filters import FilterSet,MultipleChoiceFilter
class ProductMultipleFilterBackend(FilterSet):
    muldistrict = MultipleChoiceFilter(
                 lookup_expr="icontains", 
                 field_name = "district",
                 widget=CSVWidget
            )
    class Meta:
        model = CustomUser
        fields = ('district',)

class ApplicantList(generics.ListAPIView):
    queryset = CustomUser.objects.filter(groups__name="beneficary")
    serializer_class = ApplicantExistingViewSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filter_class = ProductMultipleFilterBackend
    search_fields = ['district', 'taluka']
    filterset_fields = ['district','taluka','village','SchemeDetailsInfo__schemeType', 'SchemeDetailsInfo__Type']
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

@swagger_auto_schema(method='POST', request_body=InsertJobTypeSerializer)
@api_view(['Post'])
# @permission_classes((IsAuthenticated, ))
def InsertJobType(request):
    # comDet = EligibilityInfo.objects.get(user_id=request.user.id)
    serializer  = InsertJobTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)
@api_view(['Get'])
def VerticalWiseJobCount(request):
    data = {}
    JobCount = JobType.objects.all().values('vertical__VerticalName').annotate(total=Count('vertical__VerticalName'))
    data["JobCount"] = JobCount
    return Response(data)

@api_view(['Get'])
def VerticalList(request):
    # paginator = PageNumberPagination()
    # paginator.page_size = 10
    Vertical  =Verticals.objects.all()
    # pageResp = paginator.paginate_queryset(AllCompanyDetail,request)
    serializer = VerticalSerializer(Vertical,many=True)
    return Response(serializer.data)

class JobList(generics.ListAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
    filter_backends = [DjangoFilterBackend]
    # filter_class = ProductMultipleFilterBackend
    # search_fields = ['district', 'taluka']
    filterset_fields = ['vertical__VerticalName']


@api_view(['Get'])
def CgmList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    AllCompanyDetail  =CustomUser.objects.filter(groups__name="cgm")
    pageResp = paginator.paginate_queryset(AllCompanyDetail,request)
    serializer = UserViewSerializer(pageResp,many=True)
    return paginator.get_paginated_response(serializer.data)
    # return Response(serializer.data)

@api_view(['Get'])
def CgmDetailView(request,pk):
    # pagination = PageNumberPagination
    # pagination.page_size = 2
    comDet = CustomUser.objects.get(id=pk)
    # pageResp = pagination.pagination_queryset(AllCompanyDetail,request)
    serializer = UserViewSerializer(comDet,many=False)
    # return pagination.get_paginated.response(serializer.data)
    return Response(serializer.data)


@api_view(['Get'])
def RmList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    AllCompanyDetail  =CustomUser.objects.filter(groups__name="regionalManager")
    pageResp = paginator.paginate_queryset(AllCompanyDetail,request)
    serializer = RmregisterSerializer(pageResp,many=True)
    return paginator.get_paginated_response(serializer.data)
    # return Response(serializer.data)

@api_view(['Get'])
def RmDetailView(request,pk):
    # pagination = PageNumberPagination
    # pagination.page_size = 2
    comDet = CustomUser.objects.get(id=pk)
    # pageResp = pagination.pagination_queryset(AllCompanyDetail,request)
    serializer = RmregisterSerializer(comDet,many=False)
    # return pagination.get_paginated.response(serializer.data)
    return Response(serializer.data)


@api_view(['Get'])
def DmList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    AllCompanyDetail  =CustomUser.objects.filter(groups__name="districtManager")
    pageResp = paginator.paginate_queryset(AllCompanyDetail,request)
    serializer = DmregisterSerializer(pageResp,many=True)
    return paginator.get_paginated_response(serializer.data)
    # return Response(serializer.data)

@api_view(['Get'])
def DmDetailView(request,pk):
    # pagination = PageNumberPagination
    # pagination.page_size = 2
    comDet = CustomUser.objects.get(id=pk)
    # pageResp = pagination.pagination_queryset(AllCompanyDetail,request)
    serializer = DmregisterSerializer(comDet,many=False)
    # return pagination.get_paginated.response(serializer.data)
    return Response(serializer.data)


class AddCgmAPI(generics.GenericAPIView):
    serializer_class = CgmregisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            customuser = serializer.validated_data
            data = CgmregisterSerializer(customuser,context=self.get_serializer_context()).data
            # groupUser = CustomUser.objects.get(id = user.id)
            group = Group.objects.get(name='cgm')
            user.groups.add(group)
            return Response({
                "status":"success",
                "message":"Successfully Addedd CGM.",
                "data":data,
                })
        else:
            # print(serializer)
            # print(serializer.errors)

            return Response({
                "status":"error",
                "message":serializer.errors
             
                })


class AddRegionalManagerAPI(generics.GenericAPIView):
    serializer_class = RmregisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            customuser = serializer.validated_data
            data = RmregisterSerializer(customuser,context=self.get_serializer_context()).data
            # groupUser = CustomUser.objects.get(id = user.id)
            group = Group.objects.get(name='regionalManager')
            user.groups.add(group)
            return Response({
                "status":"success",
                "message":"Successfully Addedd Regional Manager.",
                "data":data,
                })
        else:
            # print(serializer)
            # print(serializer.errors)

            return Response({
                "status":"error",
                "message":serializer.errors
             
                })


class AddDistrictManagerAPI(generics.GenericAPIView):
    serializer_class = DmregisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            customuser = serializer.validated_data
            data = DmregisterSerializer(customuser,context=self.get_serializer_context()).data
            # groupUser = CustomUser.objects.get(id = user.id)
            group = Group.objects.get(name='districtManager')
            user.groups.add(group)
            return Response({
                "status":"success",
                "message":"Successfully Addedd District Manager.",
                "data":data,
                })
        else:
            # print(serializer)
            # print(serializer.errors)

            return Response({
                "status":"error",
                "message":serializer.errors
             
                })


class CgmUserListView(ViewSet):
    queryset = CustomUser.objects.filter(groups__name="cgm")

    def list(self, request):
        
        serializer = CgmregisterSerializer(self.queryset, many=True)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = CgmregisterSerializer(item)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })
        

class RMUserListView(ViewSet):
    queryset = CustomUser.objects.filter(groups__name="regionalManager")

    def list(self, request):
        
        serializer = RmregisterSerializer(self.queryset, many=True)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = RmregisterSerializer(item)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })

class DMUserListView(ViewSet):
    queryset = CustomUser.objects.filter(groups__name="districtManager")

    def list(self, request):
        
        serializer = DmregisterSerializer(self.queryset, many=True)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = DmregisterSerializer(item)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })
        
@swagger_auto_schema(method='PATCH', request_body=CgmregisterSerializer)
@api_view(['Patch'])
# @permission_classes((IsAuthenticated, ))
def CgmUpdateDetails(request,pk):
    comDet = CustomUser.objects.get(id=pk)
    serializer  = CgmregisterSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)
    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.queryset.get(pk=kwargs.get('pk'))
    #     serializer = self.serializer_class(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    

@swagger_auto_schema(method='PATCH', request_body=RmregisterSerializer)
@api_view(['Patch'])
# @permission_classes((IsAuthenticated, ))
def RmUpdateDetails(request,pk):
    comDet = CustomUser.objects.get(id=pk)
    serializer  = RmregisterSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@swagger_auto_schema(method='PATCH', request_body=DmregisterSerializer)
@api_view(['Patch'])
# @permission_classes((IsAuthenticated, ))
def DmUpdateDetails(request,pk):
    comDet = CustomUser.objects.get(id=pk)
    serializer  = DmregisterSerializer(instance = comDet,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


class BeneficaryRegisterations(APIView):
    serializer_class = BeneficarySerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        # import openpyxl
        password = request.data["password"]
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)
        
        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        # print(worksheet.columns)
        replacement = {}
        for row in worksheet.iter_rows(min_row=2,values_only=True):
            
            print(row,"**********************&&&&&&&&&&&&")
            if row[0] is not None:
                import random
                replacement["Name"] = row[0]
                replacement["username"] = row[1]
                replacement["district"] = row[2]
                replacement["password"] = password
                # print(replacement)
                tuser = row[0].lower()
                user = CustomUser.objects.create_user(
                uniqueId=str(random.random()),
                name = row[0],
                
                username = tuser.lower(),
                emailId = row[1],
                phoneNumber = row[2],
                dob = row[4],
                # district = int(row[2]),
                password = password,
                CasteName = row[5] ,
                SubCasteName = row[6],
                state = row[7],
                district = row[8],
                taluka = row[9]
                )
                user.set_password(request.data["password"])
                
                # CustomUser.objects.filter(id = user.id).update(district=int(row[2]))

                # user.update(district =int(row[2]) )

                user.save()
                username1=tuser.split(' ')[0]+"@"+str(user.id)
                CustomUser.objects.filter(id=user.id).update(username=username1)
                try:
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
                    
                    red = ResidentialInfo(user=user,address=row[3])
                    red.save()
                    
                    sd = SchemeDetails(user=user,schemeType=row[10],Type=row[11],LoanschemeName=row[12],LoansubSchemename=row[13],TrainingType=row[14],qualification=row[15],college=row[16],department=row[17])
                          
                    sd.save()
                except Exception as e:
                    print(e)
                group = Group.objects.get(name='beneficary')
                user.groups.add(group)
        return Response({
        "status":"Success",
        "Message":"Successfully Registered."
        
        
        })