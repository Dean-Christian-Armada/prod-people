from mariners_profile.models import ReferrersPool, Flags, Colleges, Degree, VesselType, EngineType, ManningAgency, Rank, COCRank, Relationship, Barangay, Municipality
import autocomplete_light


class ReferrerAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    # search_fields = ['^name', ]
    # model = ReferrersPool
    choices = (
      ReferrersPool.objects.filter()
      )

    search_fields = (
      ('name'), 
      )
    # Template that removes the "Results not Found"
    # autocomplete_template = 'autocomplete_template.html'
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

class RankAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Rank.objects.filter(company_standard=1)
      )

    search_fields = (
      ('rank'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(RankAutocomplete)

class COCRankAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      COCRank.objects.filter(company_standard=1)
      )

    search_fields = (
      ('coc_rank'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(COCRankAutocomplete)

class RelationshipAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Relationship.objects.filter(company_standard=1)
      )

    search_fields = (
      ('relationship'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(RelationshipAutocomplete)

class BarangayAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Barangay.objects.filter(company_standard=1)
      )

    search_fields = (
      ('barangay'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(BarangayAutocomplete)

class MunicipalityAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Municipality.objects.filter(company_standard=1)
      )

    search_fields = (
      ('municipality'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(MunicipalityAutocomplete)