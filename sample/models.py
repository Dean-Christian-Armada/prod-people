# from django.db import models

# from application_form.models import ApplicationFormFlagDocuments, ApplicationFormTrainingCertificateDocuments
# from mariners_profile.models import FlagDocumentsDetailed, TrainingCertificateDocumentsDetailed, PrincipalVesselType, MarinerStatusHistoryPermission

# Create your models here.
# class Person(models.Model):
# 	name = models.CharField(max_length=100, default=None)

# class M2MApplicationFormFlagDocuments(ApplicationFormFlagDocuments):
# 	class Meta:
# 		verbose_name_plural = "Application Form Flag Documents"
# 		proxy = True

# class M2MApplicationFormTrainingCertificateDocuments(ApplicationFormTrainingCertificateDocuments):
# 	class Meta:
# 		verbose_name_plural = "Application Form Training Certificate Documents"
# 		proxy = True

# class M2MFlagDocumentsDetailed(FlagDocumentsDetailed):
# 	class Meta:
# 		verbose_name_plural = "Flag Documents with Details of a Mariner"
# 		proxy = True

# class M2MTrainingCertificateDocumentsDetailed(TrainingCertificateDocumentsDetailed):
# 	class Meta:
# 		verbose_name_plural = "Training Certificate Documents with Details of a Mariner"
# 		proxy = True

# class M2MPrincipalVesselType(PrincipalVesselType):
# 	class Meta:
# 		verbose_name_plural = "Many to Many relation between a principal and vessel type"
# 		proxy = True

# class M2MMarinerStatusHistoryPermission(MarinerStatusHistoryPermission):
# 	class Meta:
# 		verbose_name_plural = "Mariner's Principal Change Acknowledgement Approval Flag"
# 		proxy = True