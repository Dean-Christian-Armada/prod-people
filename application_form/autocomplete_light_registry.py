from mariners_profile.models import ReferrersPool, Flags

import autocomplete_light


class ReferrerAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    search_fields = ['^name', ]
    model = ReferrersPool
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'

class FlagAutocomplete(autocomplete_light.AutocompleteModelTemplate):
	# search_fields = ['^flags', ]
	# model = Flags
	choices = (
    	Flags.objects.filter(company_standard=1)
    	)

   	search_fields = (
   		('flags'), 
   		)

	autocomplete_template = 'autocomplete_template.html'

autocomplete_light.register(ReferrerAutocomplete)
autocomplete_light.register(FlagAutocomplete)