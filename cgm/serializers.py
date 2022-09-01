from rest_framework import serializers
from database.models import CustomUser,SchemeDetails,PersonalInformation,IncomeAndDomicileInfo,EligibilityInfo,BankInformation,ResidentialInfo,QualificationInfo,OtherInfo
from django.http import JsonResponse
from django.contrib.auth import authenticate

class CgmSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','email','departmenName','designation',)


class RmSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','email','departmenName','designation','password','rmDistricts')


class DmSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','username','name','email','departmenName','designation','password','dmDistrict')
#CGM login Serializer
class CgmLoginSerializer(serializers.Serializer):
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