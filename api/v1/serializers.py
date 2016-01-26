from django.contrib.auth.models import User

from mariners_profile.models import *
from login.models import Userlevel, UserProfile

from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', )

class UserlevelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Userlevel
		fields = ('userlevel', )

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('code_regex', 'user', 'userlevel', 'code', 'first_name', 'middle_name', 'last_name', 'nick_name', 'picture', 'slug', 'departmental_email')

class EvaluationsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Evaluations
		fields = ('evaluations', )
		
class PersonReferenceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PersonReference
		fields = ('person_reference', )
		
class BirthPlaceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BirthPlace
		fields = ('birth_place', )
		
class NationalitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Nationality
		fields = ('nationality', )
		
class VesselNameSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = VesselName
		fields = ('vessel_name', )
		
class VesselTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = VesselType
		fields = ('vessel_type', )
		
class CivilStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CivilStatus
		fields = ('civil_status', )
		
class MarinerStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MarinerStatus
		fields = ('mariner_status', )
		
class CollegesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Colleges
		fields = ('college_name', )
		
class DegreeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Degree
		fields = ('degree', )
		
class HighSchoolsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = HighSchools
		fields = ('highschool_name', )
		
class VocationalsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vocationals
		fields = ('vocational_name', )
		
class PrimarySchoolsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PrimarySchools
		fields = ('primaryschool_name', )
		
class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Relationship
		fields = ('relationship', )
		
class RankSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rank
		fields = ('rank', )
		
class COCRankSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = COCRank
		fields = ('coc_rank', )
		
class LandPositionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LandPosition
		fields = ('land_position', )
		
class EngineTypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = EngineType
		fields = ('engine_type', )
		
class ManningAgencySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ManningAgency
		fields = ('manning_agency', )
		
class CauseOfDischargeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CauseOfDischarge
		fields = ('cause_of_discharge', )
		
class RegionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Region
		fields = ('region', )
		
class MunicipalitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Municipality
		fields = ('municipality', )
		
class BarangaySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Barangay
		fields = ('barangay', )
		
class SourcesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sources
		fields = ('source', )
		
class SpecificsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Specifics
		fields = ('specific', )
		
class ReasonsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Reasons
		fields = ('reason', )
		
class StatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Status
		fields = ('status', )
		
class EnglishSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = English
		fields = ('english', )
		
class DialectSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dialect
		fields = ('dialect', )
		
class BankSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Bank
		fields = ('bank', )
		
class BranchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Branch
		fields = ('branch', )
		
class PassportPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PassportPlaceIssued
		fields = ('passport_place', )
		
class SBookPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SBookPlaceIssued
		fields = ('sbook_place', )
		
class USVisaPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = USVisaPlaceIssued
		fields = ('us_visa_place', )
		
class SchengenVisaPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SchengenVisaPlaceIssued
		fields = ('schengen_visa_place', )
		
class YellowFeverPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = YellowFeverPlaceIssued
		fields = ('yellow_fever_place', )
		
class LicensePlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LicensePlaceIssued
		fields = ('license_place', )
		
class COCPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = COCPlaceIssued
		fields = ('coc_place', )
		
class TrainingPlaceIssuedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TrainingPlaceIssued
		fields = ('training_place', )
		
class IssuingAuthoritySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = IssuingAuthority
		fields = ('issuing_authority', )
		
class ZipSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Zip
		fields = ('zip', )
		
class FlagsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Flags
		fields = ('flags', )
		
class TrainingCertificatesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TrainingCertificates
		fields = ('trainings_certificates', )
		
class PrincipalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Principal
		fields = ('principal', )
		
class TrainingCenterSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TrainingCenter
		fields = ('training_center', )
		
class TradeAreaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TradeArea
		fields = ('trade_area', )
		
class PropulsionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Propulsion
		fields = ('propulsion', )
		
class CurrentAddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CurrentAddress
		fields = ('current_zip', 'current_unit', 'current_street')
		
class PermanentAddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PermanentAddress
		fields = ('permanent_zip', 'permanent_unit', 'permanent_street')
		
class PersonalDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PersonalData
		fields = ('current_address', 'permanent_address', 'dialect', 'english', 'nationality', )
		
class SpouseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Spouse
		fields = ('user', 'spouse_first_name', 'spouse_middle_name', 'spouse_last_name', 'married_date', 'birthdate', 'spouse_contact', 'spouse_working')
		
# class CollegeSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = College
# 		fields = ('username', )
		
# class HighSchoolSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = HighSchool
# 		fields = ('username', )
		
# class VocationalSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Vocational
# 		fields = ('username', )
		
# class PrimarySchoolSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = PrimarySchool
# 		fields = ('username', )
		
# class EmergencyContactSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = EmergencyContact
# 		fields = ('username', )
		
# class VisaApplicationSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = VisaApplication
# 		fields = ('username', )
		
# class DetainedSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Detained
# 		fields = ('username', )
		
# class DisciplinaryActionSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = DisciplinaryAction
# 		fields = ('username', )
		
# class ChargedOffenseSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = ChargedOffense
# 		fields = ('username', )
		
# class TerminationSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Termination
# 		fields = ('username', )
		
# class PassportSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Passport
# 		fields = ('username', )
		
# class SbookSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Sbook
# 		fields = ('username', )
		
# class COCSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = COC
# 		fields = ('username', )
		
# class LicenseSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = License
# 		fields = ('username', )
		
# class NTCLicenseSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = NTCLicense
# 		fields = ('username', )
		
# class SRCSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = SRC
# 		fields = ('username', )
		
# class STCWEndorsementSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = STCWEndorsement
# 		fields = ('username', )
		
# class STCWCertificateSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = STCWCertificate
# 		fields = ('username', )
		
# class GOCSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = GOC
# 		fields = ('username', )
		
# class USVisaSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = USVisa
# 		fields = ('username', )
		
# class SchengenVisaSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = SchengenVisa
# 		fields = ('username', )
		
# class YellowFeverSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = YellowFever
# 		fields = ('username', )
		
# class FlagDocumentsSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = FlagDocuments
# 		fields = ('username', )
		
# class FlagDocumentsDetailedSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = FlagDocumentsDetailed
# 		fields = ('username', )
		
# class TrainingCertificateDocumentsSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = TrainingCertificateDocuments
# 		fields = ('username', )
		
# class TrainingCertificateDocumentsDetailedSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = TrainingCertificateDocumentsDetailed
# 		fields = ('username', )
		
# class PrincipalVesselTypeSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = PrincipalVesselType
# 		fields = ('username', )
		
# class SeaServiceSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = SeaService
# 		fields = ('username', )
		
# class ReferrersPoolSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = ReferrersPool
# 		fields = ('username', )
		
# class MarinersProfileSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = MarinersProfile
# 		fields = ('username', )
		
# class MarinerStatusHistorySerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = MarinerStatusHistory
# 		fields = ('username', )
		
# class ReferenceSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Reference
# 		fields = ('username', )
		
# class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Evaluation
# 		fields = ('username', )
		
# class DependentsSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Dependents
# 		fields = ('username', )
		
# class LandEmploymentSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = LandEmployment
# 		fields = ('username', )
		
# class BeneficiarySerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Beneficiary
# 		fields = ('username', )
		
# class AlloteeSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Allotee
# 		fields = ('username', )
# 		