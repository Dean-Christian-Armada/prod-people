from mariners_profile.models import ReferrersPool, Flags, Colleges, Degree, VesselType, EngineType, ManningAgency

import autocomplete_light


class ReferrerAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    search_fields = ['^name', ]
    model = ReferrersPool
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ReferrerAutocomplete)

class FlagsAutocomplete(autocomplete_light.AutocompleteModelTemplate):
	# search_fields = ['^flags', ]
	# model = Flags
	choices = (
    	Flags.objects.filter(company_standard=1)
    	)

   	search_fields = (
   		('flags'), 
   		)

	autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(FlagsAutocomplete)

class CollegeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Colleges.objects.filter(company_standard=1)
      )

    search_fields = (
      ('college_name'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(CollegeAutocomplete)

class DegreeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Degree.objects.filter(company_standard=1)
      )

    search_fields = (
      ('degree'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(DegreeAutocomplete)

class VesselTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselType.objects.filter(company_standard=1)
      )

    search_fields = (
      ('vessel_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(VesselTypeAutocomplete)

class EngineTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      EngineType.objects.filter(company_standard=1)
      )

    search_fields = (
      ('engine_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(EngineTypeAutocomplete)

class ManningAgencyAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      ManningAgency.objects.filter(company_standard=1)
      )

    search_fields = (
      ('manning_agency'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManningAgencyAutocomplete)