from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import *

# Register your models here.
# class TrainingCertificatesResource(resources.ModelResource):
# 	class Meta:
# 		model = TrainingCertificates

# class TrainingCertificatesImport(ImportExportModelAdmin):
# 	resource_class = TrainingCertificatesResource

# class FlagsResource(resources.ModelResource):
# 	class Meta:
# 		model = Flags

# class FlagsImport(ImportExportModelAdmin):
# 	resource_class = FlagsResource

admin.site.register(ApplicationFormPersonalData)
admin.site.register(ApplicationFormCurrentAddress)
admin.site.register(ApplicationFormPermanentAddress)
admin.site.register(ApplicationFormSpouse)
admin.site.register(ApplicationFormCollege)
admin.site.register(ApplicationFormHighSchool)
admin.site.register(ApplicationFormEmergencyContact)
admin.site.register(ApplicationFormVisaApplication)
admin.site.register(ApplicationFormDetained)
admin.site.register(ApplicationFormDisciplinaryAction)
admin.site.register(ApplicationFormPassport)
admin.site.register(ApplicationFormSbook)
admin.site.register(ApplicationFormCOC)
admin.site.register(ApplicationFormLicense)
admin.site.register(ApplicationFormSRC)
admin.site.register(ApplicationFormGOC)
admin.site.register(ApplicationFormUSVisa)
admin.site.register(ApplicationFormSchengenVisa)
admin.site.register(ApplicationFormYellowFever)
admin.site.register(ApplicationFormFlagDocuments)
admin.site.register(ApplicationFormTrainingCertificateDocuments)
admin.site.register(ApplicationFormSeaService)
admin.site.register(Essay)
admin.site.register(AppSource)
admin.site.register(ApplicationForm)