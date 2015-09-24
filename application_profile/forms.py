from django import forms

import autocomplete_light

from mariners_profile.models import MarinersProfile

class ApplicantsDataTables(autocomplete_light.ModelForm):
	search = forms.CharField(widget=autocomplete_light.TextWidget('ApplicantsAutocomplete', attrs={'placeholder':'Search Applicants', 'class':'form-control search-input', 'name': 'search' }))

	class Meta:
		model = MarinersProfile
		fields = ('search', )