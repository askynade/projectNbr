from rest_framework import serializers
from database.models import CustomUser,SchemeDetails,PersonalInformation,IncomeAndDomicileInfo,EligibilityInfo,BankInformation,ResidentialInfo,QualificationInfo,OtherInfo
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
  
class SchemeDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SchemeDetails
  
		# fields = "__all__" 
		exclude = ('user',)
#user Serializer
class UserSerializer(serializers.ModelSerializer):

	casteCertificateimage = serializers.ImageField(allow_null=True)
	safaiKarmchariCertificateimage = serializers.ImageField(allow_null=True)

	class Meta:
		model = CustomUser
		# fields = ("id","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","safaiKarmchariId","state","district","taluka","village")
		fields = ("id","name","username","phoneNumber","address","dob","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","havesafaiKarmchariId","safaiKarmchariId","state","district","taluka","village")

		# fields = ("id","uniqueId","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","caste","subCaste","casteCertificate","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo","SchemeDetailsInfo")
        # fields = ("id","uniqueId","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificate","safaiKarmchariCertificate","safaiKarmchariId","state","district","taluka","village")



class UpdateUserSerializer(serializers.ModelSerializer):

	casteCertificateimage = serializers.ImageField(required=False,allow_empty_file=True,allow_null=True)
	safaiKarmchariCertificateimage = serializers.ImageField(required=False,allow_empty_file=True,allow_null=True)

	class Meta:
		model = CustomUser
		# fields = ("id","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","safaiKarmchariId","state","district","taluka","village")
		fields = ("name","username","phoneNumber","address","dob","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","havesafaiKarmchariId","safaiKarmchariId","state","district","taluka","village")
        # fields ="__all__"


class UserViewSerializer(serializers.ModelSerializer):
	UserPersonalInfo = PersonalInformationSerializer(many=True)
	CustomUserIncomeAndDomicileInfo = IncomeAndDomicileInfoSerializer(many=True)
	CustomUsereligibilityInfo = EligibilityInfoSerializer(many=True)
	CustomUserBankInfo = BankInformationSerializer(many=True)
	CustomUserResidentialInfo = ResidentialInfoSerializer(many=True)
	CustomUserQualificationInfo = QualificationInfoSerializer(many=True)
	CustomUserOtherInfo = OtherInfoSerializer(many=True)
	class Meta:
		model = CustomUser
		fields = ("id","name","username","emailId","phoneNumber","address","dob","isDelete","createdDate","updatedDate","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo")


# Register Serializer

class RegisterSerializer(serializers.ModelSerializer):
	# UserPersonalInfo = PersonalInformationSerializer()
	# CustomUserIncomeAndDomicileInfo = IncomeAndDomicileInfoSerializer()
	# CustomUsereligibilityInfo = EligibilityInfoSerializer()
	# CustomUserBankInfo = BankInformationSerializer()
	# CustomUserResidentialInfo = ResidentialInfoSerializer()
	# CustomUserQualificationInfo = QualificationInfoSerializer()
	# CustomUserOtherInfo = OtherInfoSerializer()
	casteCertificateimage = serializers.ImageField(required=False,allow_empty_file=True,allow_null=True)
	safaiKarmchariCertificateimage = serializers.ImageField(required=False,allow_empty_file=True,allow_null=True)

	class Meta:
		model = CustomUser
		fields = ("name","username","password","phoneNumber","address","dob","aadharLastDigits","haveCasteCertificate","CasteName","SubCasteName","casteCertificateimage","safaiKarmchariCertificateimage","havesafaiKarmchariId","safaiKarmchariId","state","district","taluka","village")

		# fields = ("uniqueId","name","username","password","emailId","phoneNumber","address","dob","isDelete","aadharLastDigits","haveCasteCertificate","caste","subCaste","casteCertificate","safaiKarmchariId","state","district","taluka","village","UserPersonalInfo","CustomUserIncomeAndDomicileInfo","CustomUsereligibilityInfo","CustomUserBankInfo","CustomUserResidentialInfo","CustomUserQualificationInfo","CustomUserOtherInfo")
		extra_kwargs = {'password':{'write_only':True}}
	def create(self,validated_data):
		# customuser = CustomUser.objects.create_user(username = validated_data['username'],password =validated_data['password'],name=validated_data['name'],phoneNumber= validated_data["phoneNumber"],address=validated_data["address"],dob=validated_data["dob"],aadharLastDigits=validated_data["aadharLastDigits"],haveCasteCertificate=validated_data["haveCasteCertificate"],CasteName=validated_data["CasteName"],SubCasteName=validated_data["SubCasteName"],casteCertificateimage=validated_data["casteCertificateimage"],safaiKarmchariCertificateimage=validated_data["safaiKarmchariCertificateimage"],havesafaiKarmchariId=validated_data["havesafaiKarmchariId"],safaiKarmchariId=validated_data["safaiKarmchariId"],state = validated_data["state"],district = validated_data["district"],taluka=validated_data["taluka"],village = validated_data["village"])
		customuser = CustomUser.objects.create_user(**validated_data)

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
