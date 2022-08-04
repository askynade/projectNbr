from rest_framework import serializers
from database.models import CustomUser,PersonalInformation,IncomeAndDomicileInfo,EligibilityInfo,BankInformation,ResidentialInfo,QualificationInfo,OtherInfo
from django.http import JsonResponse
from django.contrib.auth import authenticate


class PersonalInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = PersonalInformation
		# fields = "__all__"
		exclude = ('user',)
  

class IncomeAndDomicileInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = IncomeAndDomicileInfo
		# fields = "__all__"
		exclude = ('user',)

class EligibilityInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = EligibilityInfo
		# fields = "__all__"
		exclude = ('user',)
  
class BankInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = BankInformation
		# fields = "__all__"
		exclude = ('user',)
	# def validate_bankAccountNo(self, data):
	# 	# print(data["UserPersonalInfo"]["name"],"###################$$$$$$$$$$$")
	# 	if data:
	# 		msg = "Must include username and bankAccountNo"
	# 		raise serializers.ValidationError(msg)

	# 	return data
  
class ResidentialInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ResidentialInfo
		# fields = "__all__"
		exclude = ('user',)

  
class QualificationInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = QualificationInfo
		# fields = "__all__"
		exclude = ('user',)
 
class OtherInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = OtherInfo
		# fields = "__all__"  
		exclude = ('user',)

#user Serializer
class UserSerializer(serializers.ModelSerializer):
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
        
# Register Serializer

class RegisterSerializer(serializers.ModelSerializer):
	UserPersonalInfo = PersonalInformationSerializer()
	CustomUserIncomeAndDomicileInfo = IncomeAndDomicileInfoSerializer()
	CustomUsereligibilityInfo = EligibilityInfoSerializer()
	CustomUserBankInfo = BankInformationSerializer()
	CustomUserResidentialInfo = ResidentialInfoSerializer()
	CustomUserQualificationInfo = QualificationInfoSerializer()
	CustomUserOtherInfo = OtherInfoSerializer()
	class Meta:
		model = CustomUser
		fields = ("uniqueId","name","username","password","emailId","phoneNumber","address","dob","isDelete","aadharLastDigits","haveCasteCertificate","caste","subCaste","casteCertificate","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo")
		extra_kwargs = {'password':{'write_only':True}}
	def create(self,validated_data):
		UserPersonalInfo_data = validated_data.pop('UserPersonalInfo')
		CustomUserIncomeAndDomicileInfo_data = validated_data.pop('CustomUserIncomeAndDomicileInfo')
		CustomUsereligibilityInfo_data = validated_data.pop('CustomUsereligibilityInfo')
		CustomUserBankInfo_data = validated_data.pop('CustomUserBankInfo')
		CustomUserResidentialInfo_data = validated_data.pop('CustomUserResidentialInfo')
		CustomUserQualificationInfo_data = validated_data.pop('CustomUserQualificationInfo')
		CustomUserOtherInfo_data = validated_data.pop('CustomUserOtherInfo')
		customuser = CustomUser.objects.create_user(uniqueId = validated_data['uniqueId'],username = validated_data['username'],password =validated_data['password'],name=validated_data['name'],emailId=validated_data["emailId"],phoneNumber= validated_data["phoneNumber"],address=validated_data["address"],dob=validated_data["dob"],isDelete=validated_data["isDelete"],aadharLastDigits=validated_data["aadharLastDigits"],haveCasteCertificate=validated_data["haveCasteCertificate"],caste=validated_data["caste"],subCaste=validated_data["subCaste"] ,casteCertificate = validated_data["casteCertificate"],safaiKarmchariId = validated_data["safaiKarmchariId"],state = validated_data["state"],district = validated_data["district"],taluka=validated_data["taluka"],village = validated_data["village"])
		PersonalInformation.objects.create(user=customuser, **UserPersonalInfo_data)
		IncomeAndDomicileInfo.objects.create(user=customuser, **CustomUserIncomeAndDomicileInfo_data)
		EligibilityInfo.objects.create(user=customuser, **CustomUsereligibilityInfo_data)
		ResidentialInfo.objects.create(user=customuser, **CustomUserResidentialInfo_data)

		BankInformation.objects.create(user=customuser, **CustomUserBankInfo_data)
		QualificationInfo.objects.create(user=customuser, **CustomUserQualificationInfo_data)
		OtherInfo.objects.create(user=customuser, **CustomUserOtherInfo_data)

		# return customuser
		return customuser

	def validate(self, data):
		if data["name"]=="":
			msg = "Must include username and bankAccountNo"
			raise serializers.ValidationError(msg)
		if data["username"]=="":
			msg = "Must include username and username"
			raise serializers.ValidationError(msg)
		return data


#login Serializer
class UserLoginSerializer(serializers.Serializer):
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
