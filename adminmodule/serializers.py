from rest_framework import serializers
from database.models import CustomUser,PersonalInformation,IncomeAndDomicileInfo,EligibilityInfo,BankInformation,ResidentialInfo,QualificationInfo,OtherInfo
from django.http import JsonResponse
from django.contrib.auth import authenticate


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

class UserViewSerializer(serializers.ModelSerializer):
    UserPersonalInfo = PersonalInformationSerializer()
    CustomUserIncomeAndDomicileInfo = IncomeAndDomicileInfoSerializer()
    CustomUsereligibilityInfo = EligibilityInfoSerializer()
    CustomUserBankInfo = BankInformationSerializer()
    CustomUserResidentialInfo = ResidentialInfoSerializer()
    CustomUserQualificationInfo = QualificationInfoSerializer()
    CustomUserOtherInfo = OtherInfoSerializer()
    class Meta:
        model = CustomUser
        fields = ("id","uniqueId","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","caste","subCaste","casteCertificate","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo")


#user Serializer
class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = "__all__"

#Register Serializer

# class RegisterSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = CustomUser
# 		fields = ('id','phone','name','email','password','address','photo_proof_name','photo_proof_no','photo_proof_img')
# 		extra_kwargs = {'password':{'write_only':True}}
		
# 	def create(self,validated_data):
# 		print(validated_data,"*(*(*(*(")
# 		customuser = CustomUser.objects.create_user(address = validated_data['address'],photo_proof_name = validated_data['photo_proof_name'],photo_proof_no = validated_data['photo_proof_no'],phone =validated_data['phone'],name=validated_data['name'],email=validated_data["email"],password=validated_data['password'])
# 		return customuser

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
