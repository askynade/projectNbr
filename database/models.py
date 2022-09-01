from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from .managers import CustomUserManager
# django.forms.fields.ImageField
# Create your models here.
from django.contrib.postgres.fields import JSONField
 
# class Profile(models.Model):
#     name = models.CharField(max_length=200)
#     preferences = JSONField()
 
#     def __str__(self):
#         return self.name
    
    
class Verticals(models.Model):
    VerticalName = models.CharField(max_length=500,blank=True,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    isActive=models.BooleanField(default=True)
    isDeleted=models.BooleanField(default=False)

    def __str__(self):
        return self.id

class JobType(models.Model):
    JobName = models.CharField(max_length=500,blank=True,null=True)
    vertical=models.ForeignKey(Verticals,on_delete=models.CASCADE,blank=True,null=True,related_name = 'nameOfJob')
    JobDescription=models.TextField(max_length=500,blank=True,null=True)
    TotalVacancy = models.CharField(max_length=10,blank=True,null=True)
    StartDate = models.DateTimeField(blank=True,null=True)
    EndDate = models.DateTimeField(blank=True,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    isActive=models.BooleanField(default=True)
    isDeleted=models.BooleanField(default=False)

    def __str__(self):
        return self.id


class FormSubHeading(models.Model):
    HeadingName = models.CharField(max_length=500,blank=True,null=True)
    jobType=models.ForeignKey(JobType,on_delete=models.CASCADE,blank=True,null=True,related_name = 'nameOfHeading')
    createdDate=models.DateTimeField(auto_now_add=True)
    isActive=models.BooleanField(default=True)
    isDeleted=models.BooleanField(default=False)

    def __str__(self):
        return self.id

class FormOptions(models.Model):
    OptionName = models.CharField(max_length=500,blank=True,null=True)
    FormSubHeading=models.ForeignKey(FormSubHeading,on_delete=models.CASCADE,blank=True,null=True,related_name = 'nameOfFormSubHeading')
    createdDate=models.DateTimeField(auto_now_add=True)
    isActive=models.BooleanField(default=True)
    isDeleted=models.BooleanField(default=False)

    def __str__(self):
        return self.id




class Caste(models.Model):
	casteName=models.CharField(max_length=255)
	createdDate=models.DateTimeField(auto_now_add=True)
	isActive=models.BooleanField(default=True)
	isDelete=models.BooleanField(default=False)

	def __unicode__(self):
		return self.id

class SubCaste(models.Model):
	subCasteName=models.CharField(max_length=255)
	createdDate=models.DateTimeField(auto_now_add=True)
	isActive=models.BooleanField(default=True)
	isDelete=models.BooleanField(default=False)
	caste=models.ForeignKey(Caste,on_delete=models.CASCADE,blank=True,null=True,related_name = 'nameOfCast')

	def __unicode__(self):
		return self.id

class State(models.Model):
	stateName=models.CharField(max_length=255)
	createdDate=models.DateTimeField(auto_now_add=True)
	isActive=models.BooleanField(default=True)
	isDelete=models.BooleanField(default=False)

	def __unicode__(self):
		return self.id

class District(models.Model):
	districtName=models.CharField(max_length=255)
	createdDate=models.DateTimeField(auto_now_add=True)
	isActive=models.BooleanField(default=True)
	isDelete=models.BooleanField(default=False)
	state=models.ForeignKey(State,on_delete=models.CASCADE,blank=True,null=True,related_name = 'state')

	def __unicode__(self):
		return self.id

class Taluka(models.Model):
	talukaName=models.CharField(max_length=255)
	createdDate=models.DateTimeField(auto_now_add=True)
	isActive=models.BooleanField(default=True)
	isDelete=models.BooleanField(default=False)
	district=models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True,related_name = 'district')

	def __unicode__(self):
		return self.id

class Village(models.Model):
	villageName=models.CharField(max_length=255)
	createdDate=models.DateTimeField(auto_now_add=True)
	isActive=models.BooleanField(default=True)
	isDelete=models.BooleanField(default=False)
	taluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,blank=True,null=True,related_name = 'taluka')

	def __unicode__(self):
		return self.id


class CustomUser(AbstractUser):
	uniqueId=models.CharField(max_length=255,blank=True,null=True)
	name=models.CharField(max_length=300,blank=True,null=True)
	departmenName=models.CharField(max_length=300,blank=True,null=True)
	designation=models.CharField(max_length=300,blank=True,null=True)
	username=models.CharField(max_length=255,unique=True)
	emailId=models.EmailField(max_length=255,blank=True,null=True)
	phoneNumber=models.CharField(max_length=20,blank=True,null=True)
	address=models.TextField(max_length=500,blank=True,null=True)
	rmDistricts = models.JSONField(null=True,blank=True)
	dmDistrict = models.CharField(max_length=100,blank=True,null=True)
	dob=models.DateField(blank=True,null=True)
	isDelete=models.BooleanField(default=False)
	createdDate=models.DateTimeField(auto_now_add=True)
	updatedDate=models.DateTimeField(auto_now=True)
	aadharLastDigits=models.CharField(max_length=15,blank=True,null=True)
	haveCasteCertificate=models.BooleanField(default=False)
	CasteName=models.CharField(max_length=50,blank=True,null=True)
	SubCasteName=models.CharField(max_length=50,blank=True,null=True)
	# phoneNumber=models.CharField(max_length=20,blank=True,null=True)
	casteCertificateimage= models.ImageField(blank=True,null=True,upload_to ='casteCertificateimages/',default='')
	havesafaiKarmchariId=models.BooleanField(default=False)

	safaiKarmchariId=models.CharField(max_length=100,blank=True,null=True)
	safaiKarmchariCertificateimage= models.ImageField(blank=True,null=True,upload_to ='safaiKarmchariCertificateimages/',default='')
	state=models.CharField(max_length=50,blank=True,null=True)
	district=models.CharField(max_length=50,blank=True,null=True)
	taluka=models.CharField(max_length=50,blank=True,null=True)
	village=models.CharField(max_length=50,blank=True,null=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []
	objects = CustomUserManager()
	def __unicode__(self):
		return self.id
    
class BeneficaryJobApplication(models.Model):
    candidate=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'candidateJob')
    vertical=models.ForeignKey(Verticals,on_delete=models.CASCADE,blank=True,null=True,related_name = 'candidateVertical')
    job=models.ForeignKey(JobType,on_delete=models.CASCADE,blank=True,null=True,related_name = 'candidateJobType')
    formFields = models.JSONField()
    OptionName = models.CharField(max_length=500,blank=True,null=True)
    JobApplicationStatus=models.BooleanField(default=False)
    ApplicationCheckedBy = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'ApplicationCheckedBy')
    ApplicationCheckDate = models.DateTimeField(blank=True,null=True)
    CgmRemarks = models.CharField(max_length=500,blank=True,null=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    isActive=models.BooleanField(default=True)
    isDeleted=models.BooleanField(default=False)

    def __str__(self):
        return self.id
class Otp(models.Model):
    otp = models.CharField(max_length=4,blank=True,null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    expiryDate = models.DateTimeField(blank=True,null=True)
    otpVerifyed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.id

class PersonalInformation(models.Model):
	genderChoices=(
    ('M', 'Male'),
    ('F', 'Female'),
    ('T','Transgender'))
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'UserPersonalInfo')
	name=models.CharField(max_length=300,blank=True,null=True)
	dob=models.DateField(blank=True,null=True)
	emailId=models.EmailField(max_length=255,blank=True,null=True)
	phoneNumber=models.CharField(max_length=20,blank=True,null=True)
	gender=models.CharField(choices=genderChoices,max_length=128,blank=True,null=True)
	age=models.IntegerField(blank=True,null=True)
	nameAsSsc=models.CharField(max_length=300,blank=True,null=True)
	parentMobile=models.CharField(max_length=20,blank=True,null=True)
	maritalStatus=models.BooleanField(blank=True,null=True)
	photo=models.CharField(max_length=100,blank=True,null=True)

	languages=models.CharField(max_length=500,blank=True,null=True)
	caste=models.CharField(max_length=50,blank=True,null=True)
	subCaste=models.CharField(max_length=50,blank=True,null=True)

	# caste=models.ForeignKey(Caste,on_delete=models.CASCADE,blank=True,null=True,related_name = 'PearsonalInfoCaste')
	# subCaste=models.ForeignKey(SubCaste,on_delete=models.CASCADE,blank=True,null=True,related_name = 'PearsonalInfoSubcaste')
	haveCasteCertificate=models.BooleanField(blank=True,null=True)
	isCasteCertificateFromAaple=models.BooleanField(blank=True,null=True)
	casteCertificate=models.CharField(max_length=100,blank=True,null=True)###,blank=True,null=True
	casteCertificateNumber=models.CharField(max_length=50,blank=True,null=True)
	issueAuthority=models.CharField(max_length=100,blank=True,null=True)
	district=models.CharField(max_length=100,blank=True,null=True)
	issueDate=models.DateField(blank=True,null=True)

	def __unicode__(self):
		return self.id

class IncomeAndDomicileInfo(models.Model):
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CustomUserIncomeAndDomicileInfo')
	familyIncome=models.CharField(max_length=20,blank=True,null=True)
	haveIncomeCertificate=models.BooleanField(blank=True,null=True)
	isIncomeCertificateFromAaple=models.BooleanField(blank=True,null=True)
	incomeCertificateNumber=models.CharField(max_length=50,blank=True,null=True)
	issueAuthority=models.CharField(max_length=100,blank=True,null=True)
	incomeCertificate=models.CharField(max_length=100,blank=True,null=True)###	
	issueDate=models.DateField(blank=True,null=True)
	issueDateOfDomicile=models.DateField(blank=True,null=True)

	def __unicode__(self):
		return self.id

class EligibilityInfo(models.Model):
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CustomUsereligibilityInfo')
	isSalaried=models.BooleanField(blank=True,null=True)
	jobType=models.CharField(max_length=100,blank=True,null=True)
	isDisability=models.BooleanField(blank=True,null=True)
	disability=models.CharField(max_length=100,blank=True,null=True)
	haveDisabilityCertificate=models.BooleanField(blank=True,null=True)
	havePidNo=models.BooleanField(blank=True,null=True)
	disabilityCertificateNumber=models.CharField(max_length=50,blank=True,null=True)
	issueAuthority=models.CharField(max_length=100,blank=True,null=True)
	disabilityCertificate=models.CharField(max_length=100,blank=True,null=True)###
	issueDate=models.DateField(blank=True,null=True)
	isAadharLinkedWithBankOrYuvaOrJandhan=models.BooleanField(blank=True,null=True)
	doesAccountHaveLimitOfWithOrDepo=models.BooleanField(blank=True,null=True)

	def __unicode__(self):
		return self.id

class BankInformation(models.Model):
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CustomUserBankInfo')
	bankAccountNo=models.CharField(max_length=50,blank=True,null=True)
	ifscCode=models.CharField(max_length=50,blank=True,null=True)
	branchName=models.CharField(max_length=150,blank=True,null=True)
	bankName=models.CharField(max_length=150,blank=True,null=True)
	haveDisabilityCertificate=models.BooleanField(blank=True,null=True)
	havePidNo=models.BooleanField(blank=True,null=True)
	disabilityCertificateNumber=models.CharField(max_length=50,blank=True,null=True)
	issueAuthority=models.CharField(max_length=100,blank=True,null=True)
	disabilityCertificate=models.CharField(max_length=100,blank=True,null=True)###
	issueDate=models.DateField(blank=True,null=True)
	isAadharLinkedWithBankOrYuvaOrJandhan=models.BooleanField(blank=True,null=True)
	doesAccountHaveLimitOfWithOrDepo=models.BooleanField(blank=True,null=True)

	def __unicode__(self):
		return self.id

class ResidentialInfo(models.Model):
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CustomUserResidentialInfo')
	state=models.ForeignKey(State,on_delete=models.CASCADE,blank=True,null=True,related_name = 'ResidentialState')
	district=models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True,related_name = 'ResidentialDistrict')
	taluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,blank=True,null=True,related_name = 'ResidentialTaluka')
	village=models.ForeignKey(Village,on_delete=models.CASCADE,blank=True,null=True,related_name = 'ResidentialVillage')
	pinCode=models.CharField(max_length=50,blank=True,null=True)
	address=models.TextField(max_length=500,blank=True,null=True)
	isAddressSameAsPermanent=models.BooleanField(blank=True,null=True)
	correspondenceAddress=models.TextField(max_length=500,blank=True,null=True)
	correspondenceState=models.ForeignKey(State,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CorrespondenceState')
	correspondenceDistrict=models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CorrespondenceDistrict')
	correspondenceTaluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CorrespondenceTaluka')
	correspondenceVillage=models.ForeignKey(Village,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CorrespondenceVillage')
	correspondencePinCode=models.CharField(max_length=50,blank=True,null=True)

	def __unicode__(self):
		return self.id

class QualificationInfo(models.Model):
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CustomUserQualificationInfo')
	qualificationLevel=models.CharField(max_length=100,blank=True,null=True)
	stream=models.CharField(max_length=100,blank=True,null=True)
	completed=models.BooleanField(blank=True,null=True)
	instituteState=models.ForeignKey(State,on_delete=models.CASCADE,blank=True,null=True,related_name = 'InstituteState')
	instituteDistrict=models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True,related_name = 'InstituteDistrict')
	instituteTaluka=models.ForeignKey(Taluka,on_delete=models.CASCADE,blank=True,null=True,related_name = 'InstituteTaluka')
	collegeSchoolName=models.CharField(max_length=150,blank=True,null=True)
	course=models.CharField(max_length=100,blank=True,null=True)
	boardUniversity=models.CharField(max_length=100,blank=True,null=True)
	mode=models.CharField(max_length=100,blank=True,null=True)
	# admissionYear=models.year_field(blank=True,null=True)
	admissionYear=models.IntegerField(blank=True,null=True)
	passingYear=models.IntegerField(blank=True,null=True)
 
 
	result=models.CharField(max_length=10,blank=True,null=True)
	percentage=models.CharField(max_length=10,blank=True,null=True)
	attempts=models.CharField(max_length=10,blank=True,null=True)
	marksheets=models.CharField(max_length=100,blank=True,null=True)###
	wasAnyGap=models.BooleanField(blank=True,null=True)
	howMuchYear=models.CharField(max_length=10,blank=True,null=True)
	resume=models.CharField(max_length=100,blank=True,null=True)###

	def __unicode__(self):
		return self.id

class OtherInfo(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'CustomUserOtherInfo')
    isFatherAlive=models.BooleanField(blank=True,null=True)
    fatherName=models.CharField(max_length=200,blank=True,null=True)
    isFatherSalaried=models.BooleanField(blank=True,null=True)
    fatherOccupation=models.CharField(max_length=100,blank=True,null=True)
    isMotherAlive=models.BooleanField(blank=True,null=True)
    motherName=models.CharField(max_length=200,blank=True,null=True)
    isMotherSalaried=models.BooleanField(blank=True,null=True)
    motherOccupation=models.CharField(max_length=200,blank=True,null=True)
    readyToRelocateInMaharashtra=models.BooleanField(blank=True,null=True)
    district1=models.CharField(max_length=200,blank=True,null=True)
    district2=models.CharField(max_length=200,blank=True,null=True)
    district3=models.CharField(max_length=200,blank=True,null=True)
    wheatherStayInCity=models.BooleanField(blank=True,null=True)
    wheatherStayInRural=models.BooleanField(blank=True,null=True)

    def __unicode__(self):
        return self.id



class SchemeDetails(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name = 'SchemeDetailsInfo')
    schemeType = models.CharField(max_length=150,blank=True,null=True)
    Type = models.CharField(max_length=150,blank=True,null=True)
    LoanschemeName = models.CharField(max_length=150,blank=True,null=True)
    LoansubSchemename = models.CharField(max_length=150,blank=True,null=True)
    TrainingType = models.CharField(max_length=150,blank=True,null=True)
    qualification = models.CharField(max_length=150,blank=True,null=True)
    college = models.CharField(max_length=150,blank=True,null=True)
    department = models.CharField(max_length=150,blank=True,null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.id


