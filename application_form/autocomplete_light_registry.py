from django.db.models import Q

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
autocomplete_light.register(ReferrerAutocomplete, attrs={'placeholder': '',})

class FlagsAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Flags.objects.filter(company_standard=1)
      )

    search_fields = (
      ('flags'), 
      )

    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(FlagsAutocomplete, attrs={'placeholder': '',})

class CollegeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Colleges.objects.filter(company_standard=1)
      )

    search_fields = (
      ('college_name'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(CollegeAutocomplete, attrs={'placeholder': '',})

class DegreeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Degree.objects.filter(company_standard=1)
      )

    search_fields = (
      ('degree'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(DegreeAutocomplete, attrs={'placeholder': '',})

class VesselTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselType.objects.filter(company_standard=1)
      )

    search_fields = (
      ('vessel_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(VesselTypeAutocomplete, attrs={'placeholder': '',})

class PreferredVesselTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselType.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('vessel_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(PreferredVesselTypeAutocomplete, attrs={'placeholder': '',})

class EngineTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      EngineType.objects.filter(company_standard=1)
      )

    search_fields = (
      ('engine_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(EngineTypeAutocomplete, attrs={'placeholder': '',})

class ManningAgencyAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      ManningAgency.objects.filter(company_standard=1)
      )

    search_fields = (
      ('manning_agency'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManningAgencyAutocomplete, attrs={'placeholder': '',})

class RankAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Rank.objects.filter(company_standard=1)
      )

    search_fields = (
      ('rank'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(RankAutocomplete, attrs={'placeholder': '',})

class COCRankAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      COCRank.objects.filter(company_standard=1)
      )

    search_fields = (
      ('coc_rank'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(COCRankAutocomplete, attrs={'placeholder': '',})

class RelationshipAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Relationship.objects.filter(company_standard=1)
      )

    search_fields = (
      ('relationship'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(RelationshipAutocomplete, attrs={'placeholder': '',})

class BarangayAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Barangay.objects.filter(company_standard=1)
      )

    search_fields = (
      ('barangay'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(BarangayAutocomplete, attrs={'placeholder': '',})

class MunicipalityAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Municipality.objects.filter(company_standard=1)
      )

    search_fields = (
      ('municipality'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(MunicipalityAutocomplete, attrs={'placeholder': '',})

class LandPositionAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      LandPosition.objects.filter(company_standard=1)
      )

    search_fields = (
      ('land_position'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(LandPositionAutocomplete, attrs={'placeholder': '',})

class BankAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Bank.objects.filter(company_standard=1)
      )

    search_fields = (
      ('bank'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(BankAutocomplete, attrs={'placeholder': '',})

class PassportPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      PassportPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('passport_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(PassportPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class SBookPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      SBookPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('sbook_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(SBookPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class USVisaPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      USVisaPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('us_visa_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(USVisaPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class SchengenVisaPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      SchengenVisaPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('schengen_visa_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(SchengenVisaPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class YellowFeverPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      YellowFeverPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('yellow_fever_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(YellowFeverPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class LicensePlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      LicensePlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('license_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(LicensePlaceIssuedAutocomplete, attrs={'placeholder': '',})

class COCPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      COCPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('coc_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(COCPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class TrainingPlaceIssuedAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      TrainingPlaceIssued.objects.filter(company_standard=1)
      )

    search_fields = (
      ('training_place'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(TrainingPlaceIssuedAutocomplete, attrs={'placeholder': '',})

class TrainingCenterAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      TrainingCenter.objects.filter(company_standard=1)
      )

    search_fields = (
      ('training_center'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(TrainingCenterAutocomplete, attrs={'placeholder': '',})

class TradeAreaAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      TradeArea.objects.filter()
      )

    search_fields = (
      ('trade_area'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(TradeAreaAutocomplete, attrs={'placeholder': '',})

class ManshipVesselNameAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselName.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('vessel_name'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipVesselNameAutocomplete, attrs={'placeholder': '',})

class ManshipVesselTypeAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      VesselType.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('vessel_type'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipVesselTypeAutocomplete, attrs={'placeholder': '',})

class ManshipPrincipalAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Principal.objects.filter(manship_standard=True).filter(~Q(principal__iexact="manship"))
      )

    search_fields = (
      ('principal'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipPrincipalAutocomplete, attrs={'placeholder': '',})

class ManshipFlagsAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Flags.objects.filter(manship_standard=1)
      )

    search_fields = (
      ('flags'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(ManshipFlagsAutocomplete, attrs={'placeholder': '',})

class DialectAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    choices = (
      Dialect.objects.filter()
      )

    search_fields = (
      ('dialect'), 
      )
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
autocomplete_light.register(DialectAutocomplete, attrs={'placeholder': '',})