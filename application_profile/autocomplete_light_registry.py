from django.db.models import Q

from mariners_profile.models import MarinersProfile, Flags
from login.models import UserProfile

import autocomplete_light


class ApplicantsAutocomplete(autocomplete_light.AutocompleteModelTemplate):

	applicants_profile = MarinersProfile.objects.filter(status=0).values('user')
	choices = (
    	UserProfile.objects.filter(id__in=applicants_profile)
    	)
	search_fields = (
   		('first_name'),
   		('middle_name'),
   		('last_name'), 
   		)
	autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ApplicantsAutocomplete, attrs={'placeholder': '',})

class MarinersAutocomplete(autocomplete_light.AutocompleteModelTemplate):
  mariners_profile = MarinersProfile.objects.filter(status=1).values('user')
  choices = (
    	UserProfile.objects.filter(id__in=mariners_profile)
    	)
  search_fields = (
   		('first_name'),
   		('middle_name'),
   		('last_name'), 
      ('code'), 
   		)
  autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(MarinersAutocomplete, attrs={'placeholder': '',})