from django import forms

from autocomplete_light import shortcuts as autocomplete_light

from mariners_profile.models import MarinersProfile, Principal, PrincipalVesselType

class ApplicantsDataTables(autocomplete_light.ModelForm):
	search = forms.CharField(widget=autocomplete_light.TextWidget('ApplicantsAutocomplete', attrs={'placeholder':'Search Applicants', 'class':'form-control search-input', 'name': 'search' }))

	class Meta:
		model = MarinersProfile
		fields = ('search', )

class PrincipalSelectForm(forms.Form):
	principal = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control input-form'}), queryset=Principal.objects.filter(company_standard=1).order_by('principal'))

class DynamicPrincipalVesselTypeSelectForm(forms.Form):
	def __init__(self, principal, *args, **kwargs):
		super(DynamicPrincipalVesselTypeSelectForm, self).__init__(*args, **kwargs)
		try:
			principal = Principal.objects.get(principal__iexact=principal)
			# queryset script to return the selected many-to-many values
			principal_vessel_type = PrincipalVesselType.objects.get(principal=principal).vessel_type.all().order_by('vessel_type')
			self.fields['vessel_type'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control input-form'}), queryset=principal_vessel_type)
		except:
			pass