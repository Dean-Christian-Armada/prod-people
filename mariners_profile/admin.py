from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# from .models import Flags, TrainingCertificates, Colleges, Degree, HighSchools, Barangay, Municipality, Relationship, Sources, Specifics, Reasons, Rank, BirthPlace, VesselType, CivilStatus, VesselName, EngineType, ManningAgency, Principal, CauseOfDischarge, Status, Zip

from .models import *

# Register your models here.

class TrainingCertificatesResource(resources.ModelResource):
	class Meta:
		model = TrainingCertificates

class TrainingCertificatesImport(ImportExportModelAdmin):
	resource_class = TrainingCertificatesResource

class ReferrersPoolResource(resources.ModelResource):
	class Meta:
		model = ReferrersPool

class ReferrersPoolImport(ImportExportModelAdmin):
	resource_class = ReferrersPoolResource

class TrainingCertficatesAdmin(admin.ModelAdmin):
	list_display = ('trainings_certificates', 'get_departments', )

class RankAdmin(admin.ModelAdmin):
	list_filter = ('hiring', 'department')
	list_display = ('rank', 'hiring', 'order', 'department')
	ordering = ('order', )

class ReferrerAdmin(admin.ModelAdmin):
	list_per_page = 4000

admin.site.register(Evaluation)
admin.site.register(Zip)
admin.site.register(CurrentAddress)
admin.site.register(PermanentAddress)
admin.site.register(CivilStatus)
admin.site.register(PersonalData)
admin.site.register(Spouse)
admin.site.register(Colleges)
admin.site.register(Degree)
admin.site.register(College)
admin.site.register(HighSchools)
admin.site.register(HighSchool)
admin.site.register(Vocationals)
admin.site.register(Vocational)
admin.site.register(PrimarySchools)
admin.site.register(PrimarySchool)
admin.site.register(EmergencyContact)
admin.site.register(Barangay)
admin.site.register(Municipality)
admin.site.register(Relationship)
admin.site.register(VisaApplication)
admin.site.register(Detained)
admin.site.register(DisciplinaryAction)
admin.site.register(ChargedOffense)
admin.site.register(Termination)
admin.site.register(Passport)
admin.site.register(Sources)
admin.site.register(Specifics)
admin.site.register(Reasons)
admin.site.register(Rank, RankAdmin)
admin.site.register(COCRank)
admin.site.register(BirthPlace)
admin.site.register(VesselType)
# admin.site.register(Position)
admin.site.register(VesselName)
admin.site.register(EngineType)
admin.site.register(ManningAgency)
admin.site.register(Principal)
admin.site.register(CauseOfDischarge)
admin.site.register(SeaService)
admin.site.register(Sbook)
admin.site.register(COC)
admin.site.register(License)
admin.site.register(SRC)
admin.site.register(GOC)
admin.site.register(USVisa)
admin.site.register(SchengenVisa)
admin.site.register(YellowFever)
admin.site.register(Flags)
admin.site.register(FlagDocuments)
admin.site.register(FlagDocumentsDetailed)
admin.site.register(TrainingCenter)
admin.site.register(TrainingCertificates, TrainingCertficatesAdmin)
admin.site.register(TrainingCertificateDocuments)
admin.site.register(TrainingCertificateDocumentsDetailed)
admin.site.register(ReferrersPool, ReferrersPoolImport)
admin.site.register(Status)
admin.site.register(MarinersProfile)
admin.site.register(Departments)
admin.site.register(Reference)
admin.site.register(PrincipalVesselType)
admin.site.register(PassportPlaceIssued)
admin.site.register(SBookPlaceIssued)
admin.site.register(USVisaPlaceIssued)
admin.site.register(SchengenVisaPlaceIssued)
admin.site.register(YellowFeverPlaceIssued)
admin.site.register(LicensePlaceIssued)
admin.site.register(COCPlaceIssued)
admin.site.register(TradeArea)
admin.site.register(Dialect)
admin.site.register(English)
admin.site.register(LandEmployment)
admin.site.register(Beneficiary)
admin.site.register(Allotee)
admin.site.register(STCWEndorsement)
admin.site.register(TrainingPlaceIssued)
admin.site.register(Dependents)
admin.site.register(MarinerStatus)
admin.site.register(MarinerStatusComment)
admin.site.register(MarinerStatusHistory)
admin.site.register(NonConformingSeafarerReason)