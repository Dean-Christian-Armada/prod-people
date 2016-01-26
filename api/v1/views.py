from django.contrib.auth.models import User

from . serializers import *
from mariners_profile.models import *
from login.models import Userlevel, UserProfile

from rest_framework import viewsets

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserlevelViewSet(viewsets.ModelViewSet):
    queryset = Userlevel.objects.all()
    serializer_class = UserlevelSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluations.objects.all()
    serializer_class = EvaluationsSerializer
    
class PersonReferenceViewSet(viewsets.ModelViewSet):
    queryset = PersonReference.objects.all()
    serializer_class = PersonReferenceSerializer
    
class BirthPlaceViewSet(viewsets.ModelViewSet):
    queryset = BirthPlace.objects.all()
    serializer_class = BirthPlaceSerializer
    
class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
    
class VesselNameViewSet(viewsets.ModelViewSet):
    queryset = VesselName.objects.all()
    serializer_class = VesselNameSerializer
    
class VesselTypeViewSet(viewsets.ModelViewSet):
    queryset = VesselType.objects.all()
    serializer_class = VesselTypeSerializer
    
class CivilStatusViewSet(viewsets.ModelViewSet):
    queryset = CivilStatus.objects.all()
    serializer_class = CivilStatusSerializer
    
class MarinerStatusViewSet(viewsets.ModelViewSet):
    queryset = MarinerStatus.objects.all()
    serializer_class = MarinerStatusSerializer
    
class CollegesViewSet(viewsets.ModelViewSet):
    queryset = Colleges.objects.all()
    serializer_class = CollegesSerializer
    
class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    
class HighSchoolsViewSet(viewsets.ModelViewSet):
    queryset = HighSchools.objects.all()
    serializer_class = HighSchoolsSerializer
    
class VocationalsViewSet(viewsets.ModelViewSet):
    queryset = Vocationals.objects.all()
    serializer_class = VocationalsSerializer
    
class PrimarySchoolsViewSet(viewsets.ModelViewSet):
    queryset = PrimarySchools.objects.all()
    serializer_class = PrimarySchoolsSerializer
    
class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    
class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer
    
class COCRankViewSet(viewsets.ModelViewSet):
    queryset = COCRank.objects.all()
    serializer_class = COCRankSerializer
    
class LandPositionViewSet(viewsets.ModelViewSet):
    queryset = LandPosition.objects.all()
    serializer_class = LandPositionSerializer
    
class EngineTypeViewSet(viewsets.ModelViewSet):
    queryset = EngineType.objects.all()
    serializer_class = EngineTypeSerializer
    
class ManningAgencyViewSet(viewsets.ModelViewSet):
    queryset = ManningAgency.objects.all()
    serializer_class = ManningAgencySerializer
    
class CauseOfDischargeViewSet(viewsets.ModelViewSet):
    queryset = CauseOfDischarge.objects.all()
    serializer_class = CauseOfDischargeSerializer
    
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    
class MunicipalityViewSet(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    
class BarangayViewSet(viewsets.ModelViewSet):
    queryset = Barangay.objects.all()
    serializer_class = BarangaySerializer
    
class SourcesViewSet(viewsets.ModelViewSet):
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializer
    
class SpecificsViewSet(viewsets.ModelViewSet):
    queryset = Specifics.objects.all()
    serializer_class = SpecificsSerializer
    
class ReasonsViewSet(viewsets.ModelViewSet):
    queryset = Reasons.objects.all()
    serializer_class = ReasonsSerializer
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
class EnglishViewSet(viewsets.ModelViewSet):
    queryset = English.objects.all()
    serializer_class = EnglishSerializer
    
class DialectViewSet(viewsets.ModelViewSet):
    queryset = Dialect.objects.all()
    serializer_class = DialectSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    
class PassportPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = PassportPlaceIssued.objects.all()
    serializer_class = PassportPlaceIssuedSerializer
    
class SBookPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = SBookPlaceIssued.objects.all()
    serializer_class = SBookPlaceIssuedSerializer
    
class USVisaPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = USVisaPlaceIssued.objects.all()
    serializer_class = USVisaPlaceIssuedSerializer
    
class SchengenVisaPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = SchengenVisaPlaceIssued.objects.all()
    serializer_class = SchengenVisaPlaceIssuedSerializer
    
class YellowFeverPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = YellowFeverPlaceIssued.objects.all()
    serializer_class = YellowFeverPlaceIssuedSerializer
    
class LicensePlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = LicensePlaceIssued.objects.all()
    serializer_class = LicensePlaceIssuedSerializer
    
class COCPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = COCPlaceIssued.objects.all()
    serializer_class = COCPlaceIssuedSerializer
    
class TrainingPlaceIssuedViewSet(viewsets.ModelViewSet):
    queryset = TrainingPlaceIssued.objects.all()
    serializer_class = TrainingPlaceIssuedSerializer
    
class IssuingAuthorityViewSet(viewsets.ModelViewSet):
    queryset = IssuingAuthority.objects.all()
    serializer_class = IssuingAuthoritySerializer
    
class ZipViewSet(viewsets.ModelViewSet):
    queryset = Zip.objects.all()
    serializer_class = ZipSerializer
    
class FlagsViewSet(viewsets.ModelViewSet):
    queryset = Flags.objects.all()
    serializer_class = FlagsSerializer
    
class TrainingCertificatesViewSet(viewsets.ModelViewSet):
    queryset = TrainingCertificates.objects.all()
    serializer_class = TrainingCertificatesSerializer
    
class PrincipalViewSet(viewsets.ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer
    
class TrainingCenterViewSet(viewsets.ModelViewSet):
    queryset = TrainingCenter.objects.all()
    serializer_class = TrainingCenterSerializer
    
class TradeAreaViewSet(viewsets.ModelViewSet):
    queryset = TradeArea.objects.all()
    serializer_class = TradeAreaSerializer
    
class PropulsionViewSet(viewsets.ModelViewSet):
    queryset = Propulsion.objects.all()
    serializer_class = PropulsionSerializer
    
class CurrentAddressViewSet(viewsets.ModelViewSet):
    queryset = CurrentAddress.objects.all()
    serializer_class = CurrentAddressSerializer
    
class PermanentAddressViewSet(viewsets.ModelViewSet):
    queryset = PermanentAddress.objects.all()
    serializer_class = PermanentAddressSerializer
    
class PersonalDataViewSet(viewsets.ModelViewSet):
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer
    
class SpouseViewSet(viewsets.ModelViewSet):
    queryset = Spouse.objects.all()
    serializer_class = SpouseSerializer
    
# class CollegeViewSet(viewsets.ModelViewSet):
#     queryset = College.objects.all()
#     serializer_class = CollegeSerializer
    
# class HighSchoolViewSet(viewsets.ModelViewSet):
#     queryset = HighSchool.objects.all()
#     serializer_class = HighSchoolSerializer
    
# class VocationalViewSet(viewsets.ModelViewSet):
#     queryset = Vocational.objects.all()
#     serializer_class = VocationalSerializer
    
# class PrimarySchoolViewSet(viewsets.ModelViewSet):
#     queryset = PrimarySchool.objects.all()
#     serializer_class = PrimarySchoolSerializer
    
# class EmergencyContactViewSet(viewsets.ModelViewSet):
#     queryset = EmergencyContact.objects.all()
#     serializer_class = EmergencyContactSerializer
    
# class VisaApplicationViewSet(viewsets.ModelViewSet):
#     queryset = VisaApplication.objects.all()
#     serializer_class = VisaApplicationSerializer
    
# class DetainedViewSet(viewsets.ModelViewSet):
#     queryset = Detained.objects.all()
#     serializer_class = DetainedSerializer
    
# class DisciplinaryActionViewSet(viewsets.ModelViewSet):
#     queryset = DisciplinaryAction.objects.all()
#     serializer_class = DisciplinaryActionSerializer
    
# class ChargedOffenseViewSet(viewsets.ModelViewSet):
#     queryset = ChargedOffense.objects.all()
#     serializer_class = ChargedOffenseSerializer
    
# class TerminationViewSet(viewsets.ModelViewSet):
#     queryset = Termination.objects.all()
#     serializer_class = TerminationSerializer
    
# class PassportViewSet(viewsets.ModelViewSet):
#     queryset = Passport.objects.all()
#     serializer_class = PassportSerializer
    
# class SbookViewSet(viewsets.ModelViewSet):
#     queryset = Sbook.objects.all()
#     serializer_class = SbookSerializer
    
# class COCViewSet(viewsets.ModelViewSet):
#     queryset = COC.objects.all()
#     serializer_class = COCSerializer
    
# class LicenseViewSet(viewsets.ModelViewSet):
#     queryset = License.objects.all()
#     serializer_class = LicenseSerializer
    
# class NTCLicenseViewSet(viewsets.ModelViewSet):
#     queryset = NTCLicense.objects.all()
#     serializer_class = NTCLicenseSerializer
    
# class SRCViewSet(viewsets.ModelViewSet):
#     queryset = SRC.objects.all()
#     serializer_class = SRCSerializer
    
# class STCWEndorsementViewSet(viewsets.ModelViewSet):
#     queryset = STCWEndorsement.objects.all()
#     serializer_class = STCWEndorsementSerializer
    
# class STCWCertificateViewSet(viewsets.ModelViewSet):
#     queryset = STCWCertificate.objects.all()
#     serializer_class = STCWCertificateSerializer
    
# class GOCViewSet(viewsets.ModelViewSet):
#     queryset = GOC.objects.all()
#     serializer_class = GOCSerializer
    
# class USVisaViewSet(viewsets.ModelViewSet):
#     queryset = USVisa.objects.all()
#     serializer_class = USVisaSerializer
    
# class SchengenVisaViewSet(viewsets.ModelViewSet):
#     queryset = SchengenVisa.objects.all()
#     serializer_class = SchengenVisaSerializer
    
# class YellowFeverViewSet(viewsets.ModelViewSet):
#     queryset = YellowFever.objects.all()
#     serializer_class = YellowFeverSerializer
    
# class FlagDocumentsViewSet(viewsets.ModelViewSet):
#     queryset = FlagDocuments.objects.all()
#     serializer_class = FlagDocumentsSerializer
    
# class FlagDocumentsDetailedViewSet(viewsets.ModelViewSet):
#     queryset = FlagDocumentsDetailed.objects.all()
#     serializer_class = FlagDocumentsDetailedSerializer
    
# class TrainingCertificateDocumentsViewSet(viewsets.ModelViewSet):
#     queryset = TrainingCertificateDocuments.objects.all()
#     serializer_class = TrainingCertificateDocumentsSerializer
    
# class TrainingCertificateDocumentsDetailedViewSet(viewsets.ModelViewSet):
#     queryset = TrainingCertificateDocumentsDetailed.objects.all()
#     serializer_class = TrainingCertificateDocumentsDetailedSerializer
    
# class PrincipalVesselTypeViewSet(viewsets.ModelViewSet):
#     queryset = PrincipalVesselType.objects.all()
#     serializer_class = PrincipalVesselTypeSerializer
    
# class SeaServiceViewSet(viewsets.ModelViewSet):
#     queryset = SeaService.objects.all()
#     serializer_class = SeaServiceSerializer
    
# class ReferrersPoolViewSet(viewsets.ModelViewSet):
#     queryset = ReferrersPool.objects.all()
#     serializer_class = ReferrersPoolSerializer
    
# class MarinersProfileViewSet(viewsets.ModelViewSet):
#     queryset = MarinersProfile.objects.all()
#     serializer_class = MarinersProfileSerializer
    
# class MarinerStatusHistoryViewSet(viewsets.ModelViewSet):
#     queryset = MarinerStatusHistory.objects.all()
#     serializer_class = MarinerStatusHistorySerializer
    
# class ReferenceViewSet(viewsets.ModelViewSet):
#     queryset = Reference.objects.all()
#     serializer_class = ReferenceSerializer
    
# class EvaluationViewSet(viewsets.ModelViewSet):
#     queryset = Evaluation.objects.all()
#     serializer_class = EvaluationSerializer
    
# class DependentsViewSet(viewsets.ModelViewSet):
#     queryset = Dependents.objects.all()
#     serializer_class = DependentsSerializer
    
# class LandEmploymentViewSet(viewsets.ModelViewSet):
#     queryset = LandEmployment.objects.all()
#     serializer_class = LandEmploymentSerializer
    
# class BeneficiaryViewSet(viewsets.ModelViewSet):
#     queryset = Beneficiary.objects.all()
#     serializer_class = BeneficiarySerializer
    
# class AlloteeViewSet(viewsets.ModelViewSet):
#     queryset = Allotee.objects.all()
#     serializer_class = AlloteeSerializer
#     