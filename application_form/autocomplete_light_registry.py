from mariners_profile.models import *
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

class LandPositionAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      LandPosition.objects.filter(company_standard=1)
      )

    search_fields = (
      ('land_position'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(LandPositionAutocomplete)

class BankAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Bank.objects.filter(company_standard=1)
      )

    search_fields = (
      ('bank'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(BankAutocomplete)

class PassportPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      PassportPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('passport_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(PassportPlaceIssuedAutocomplete)

class SBookPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      SBookPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('sbook_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(SBookPlaceIssuedAutocomplete)

class USVisaPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      USVisaPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('us_visa_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(USVisaPlaceIssuedAutocomplete)

class SchengenVisaPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      SchengenVisaPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('schengen_visa_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(SchengenVisaPlaceIssuedAutocomplete)

class YellowFeverPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      YellowFeverPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('yellow_fever_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(YellowFeverPlaceIssuedAutocomplete)

class LicensePlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      LicensePlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('license_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(LicensePlaceIssuedAutocomplete)

class COCPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      COCPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('coc_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(COCPlaceIssuedAutocomplete)

class TrainingPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      TrainingPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('training_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(TrainingPlaceIssuedAutocomplete)

class TrainingCenterAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      TrainingCenter.objects.filter(company_standard=1)
      )

    search_fields = (
      ('training_center'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(TrainingCenterAutocomplete)

class TradeAreaAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      TradeArea.objects.filter()
      )

    search_fields = (
      ('trade_area'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(TradeAreaAutocomplete)

class ManshipVesselNameAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselName.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('vessel_name'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipVesselNameAutocomplete)

class ManshipVesselTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselType.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('vessel_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipVesselTypeAutocomplete)

class ManshipPrincipalAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Principal.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('principal'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipPrincipalAutocomplete)

class ManshipFlagsAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Flags.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('flags'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipFlagsAutocomplete)