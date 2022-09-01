from rest_framework import serializers
from database.models import FormOptions,FormSubHeading,JobType,Verticals,CustomUser,SchemeDetails,PersonalInformation,IncomeAndDomicileInfo,EligibilityInfo,BankInformation,ResidentialInfo,QualificationInfo,OtherInfo
from django.http import JsonResponse
from django.contrib.auth import authenticate

  
class VerticalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Verticals
		fields = "__all__"

class FormOptionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormOptions
		fields = "__all__"
class FormSubHeadingSerializer(serializers.ModelSerializer):
	nameOfFormSubHeading = FormOptionsSerializer(many=True)
	class Meta:
		model = FormSubHeading
		fields = ('HeadingName','jobType','isActive','isDeleted','nameOfFormSubHeading')
class InsertJobTypeSerializer(serializers.ModelSerializer):
	# nameOfHeading = FormSubHeadingSerializer(many=True)
	class Meta:
		model = JobType
		fields = ('JobName','vertical','JobDescription','TotalVacancy','StartDate','EndDate','isActive','isDeleted')


class JobTypeSerializer(serializers.ModelSerializer):
	nameOfHeading = FormSubHeadingSerializer(many=True)
	class Meta:
		model = JobType
		fields = ('JobName','vertical','JobDescription','TotalVacancy','StartDate','EndDate','isActive','isDeleted','nameOfHeading')

class FormSubHeadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormSubHeading
		fields = "__all__"

class FormOptionsSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormOptions
		fields = "__all__"
class PersonalInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalInformation
		fields = "__all__"

class IncomeAndDomicileInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = IncomeAndDomicileInfo
		fields = "__all__"

class EligibilityInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = EligibilityInfo
		fields = "__all__"
  
class BankInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = BankInformation
		fields = "__all__"
  
class ResidentialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResidentialInfo
		fields = "__all__"
  
class QualificationInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = QualificationInfo
		fields = "__all__"
  
class QualificationInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = QualificationInfo
		fields = "__all__"
 
class OtherInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = OtherInfo
		fields = "__all__"  
class SchemeDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchemeDetails
		fields = "__all__"


class AppPersonalInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalInformation
		fields = "__all__"
  

class AppIncomeAndDomicileInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = IncomeAndDomicileInfo
		fields = "__all__"

class AppEligibilityInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = EligibilityInfo
		fields = "__all__"
  
class AppBankInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = BankInformation
		fields = "__all__"
  
class AppResidentialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResidentialInfo
		fields = "__all__"
  
class AppQualificationInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = QualificationInfo
		fields = "__all__"
  

 
class AppOtherInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = OtherInfo
		fields = "__all__"  
class AppSchemeDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchemeDetails
		fields = "__all__"


class ApplicantExistingViewSerializer(serializers.ModelSerializer):
	UserPersonalInfo = AppPersonalInformationSerializer(many=True)
	CustomUserIncomeAndDomicileInfo = AppIncomeAndDomicileInfoSerializer(many=True)
	CustomUsereligibilityInfo = AppEligibilityInfoSerializer(many=True)
	CustomUserBankInfo = AppBankInformationSerializer(many=True)
	CustomUserResidentialInfo = AppResidentialInfoSerializer(many=True)
	CustomUserQualificationInfo = AppQualificationInfoSerializer(many=True)
	CustomUserOtherInfo = AppOtherInfoSerializer(many=True)
	SchemeDetailsInfo = AppSchemeDetailsSerializer(many=True)
	class Meta:
		model = CustomUser
		fields = ("id","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo","SchemeDetailsInfo")

  
class UserViewSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		fields = ("id","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","safaiKarmchariId","state","district","taluka","village")

        # fields = ("id","uniqueId","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","caste","subCaste","casteCertificate","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo","SchemeDetailsInfo")


#user Serializer
class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = "__all__"


# CGM Register Serializer

class CgmregisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','email','departmenName','designation','password')
		extra_kwargs = {'password':{'write_only':True}}
		
	def create(self,validated_data):
		print(validated_data,"*(*(*(*(")
		customuser = CustomUser.objects.create_user(username=validated_data['username'],name=validated_data['name'],email=validated_data["email"],departmenName=validated_data["departmenName"],designation=validated_data["designation"],password=validated_data['password'])
		return customuser



class RmregisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','email','departmenName','designation','password','rmDistricts')
		extra_kwargs = {'password':{'write_only':True}}
		
	def create(self,validated_data):
		print(validated_data,"*(*(*(*(")
		customuser = CustomUser.objects.create_user(username=validated_data['username'],name=validated_data['name'],rmDistricts=validated_data['rmDistricts'],email=validated_data["email"],departmenName=validated_data["departmenName"],designation=validated_data["designation"],password=validated_data['password'])
		return customuser

class DmregisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','email','departmenName','designation','password','dmDistrict')
		extra_kwargs = {'password':{'write_only':True}}
		
	def create(self,validated_data):
		print(validated_data,"*(*(*(*(")
		customuser = CustomUser.objects.create_user(username=validated_data['username'],name=validated_data['name'],dmDistrict=validated_data['dmDistrict'],email=validated_data["email"],departmenName=validated_data["departmenName"],designation=validated_data["designation"],password=validated_data['password'])
		return customuser

#login Serializer
class LoginSerializer(serializers.Serializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','password')

	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self,data):
		customuser = authenticate(**data)
		if data["username"] =="":
			msg = "Please enter username."
			raise serializers.ValidationError(msg)
		if data["password"] =="":
			msg = "Please enter password."
			raise serializers.ValidationError(msg)
		if customuser and customuser.is_active:
			return customuser
		raise serializers.ValidationError("Incorrect Credentials")


class BeneficarySerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','district','password')
		extra_kwargs = {'password':{'write_only':True}}
		
	def create(self,validated_data):
		print(validated_data,"*(*(*(*(1")
		customuser = CustomUser.objects.create_user(name =validated_data['name'],district =validated_data['district'],username =validated_data['username'],password=validated_data['password'])
		return customuser