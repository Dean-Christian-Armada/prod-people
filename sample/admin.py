from django.contrib import admin
from .models import  *


# Register your models here.
# admin.site.register(Person)
admin.site.register(M2MApplicationFormFlagDocuments)
admin.site.register(M2MApplicationFormTrainingCertificateDocuments)
admin.site.register(M2MFlagDocumentsDetailed)
admin.site.register(M2MTrainingCertificateDocumentsDetailed)
admin.site.register(M2MPrincipalVesselType)
admin.site.register(M2MMarinerStatusHistoryPermission)