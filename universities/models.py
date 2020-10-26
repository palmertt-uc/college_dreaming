from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Institutions(models.Model):
    institutionid = models.AutoField(db_column='InstitutionId', primary_key=True)  # Field name made lowercase.
    unitid = models.CharField(db_column='UNITID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opeid = models.CharField(db_column='OPEID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opeid6 = models.CharField(db_column='OPEID6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    instname = models.CharField(db_column='InstName', max_length=200)  # Field name made lowercase.
    accredagency = models.CharField(db_column='AccredAgency', max_length=200)  # Field name made lowercase.
    insturl = models.CharField(db_column='InstURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pricecalcurl = models.CharField(db_column='PriceCalcURL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statefips = models.CharField(db_column='StateFIPS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    maincampus = models.TextField(db_column='MainCampus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    numberofbranches = models.CharField(db_column='NumberOfBranches', max_length=2, blank=True, null=True)  # Field name made lowercase.
    predominantdegrees = models.CharField(db_column='PredominantDegrees', max_length=1, blank=True, null=True)  # Field name made lowercase.
    highestdegree = models.CharField(db_column='HighestDegree', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ownership = models.CharField(db_column='Ownership', max_length=1, blank=True, null=True)  # Field name made lowercase.
    distanceonly = models.TextField(db_column='DistanceOnly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(db_column='Locale', max_length=10, blank=True, null=True)  # Field name made lowercase.
    zipcodeid = models.ForeignKey('Zipcodes', models.DO_NOTHING, db_column='ZipCodeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Institutions'

    def __str__(self):
        return self.instname


class Admissions(models.Model):
    admissionid = models.AutoField(db_column='AdmissionId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    admission_rate_overall = models.FloatField(blank=True, null=True)
    admission_rate_by_ope_id = models.FloatField(blank=True, null=True)
    sat_scores_25th_percentile_critical_reading = models.FloatField(blank=True, null=True)
    sat_scores_75th_percentile_critical_reading = models.FloatField(blank=True, null=True)
    sat_scores_25th_percentile_math = models.FloatField(blank=True, null=True)
    sat_scores_75th_percentile_math = models.FloatField(blank=True, null=True)
    sat_scores_25th_percentile_writing = models.FloatField(blank=True, null=True)
    sat_scores_75th_percentile_writing = models.FloatField(blank=True, null=True)
    sat_scores_midpoint_critical_reading = models.FloatField(blank=True, null=True)
    sat_scores_midpoint_math = models.FloatField(blank=True, null=True)
    sat_scores_midpoint_writing = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_cumulative = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_cumulative = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_english = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_english = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_math = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_math = models.FloatField(blank=True, null=True)
    act_scores_25th_percentile_writing = models.FloatField(blank=True, null=True)
    act_scores_75th_percentile_writing = models.FloatField(blank=True, null=True)
    act_scores_midpoint_cumulative = models.FloatField(blank=True, null=True)
    act_scores_midpoint_english = models.FloatField(blank=True, null=True)
    act_scores_midpoint_math = models.FloatField(blank=True, null=True)
    act_scores_midpoint_writing = models.FloatField(blank=True, null=True)
    sat_scores_average_overall = models.FloatField(blank=True, null=True)
    sat_scores_average_by_ope_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Admissions'

    def __str__(self):
        return self.institutionid.instname + ' - Admission'


class Cities(models.Model):
    cityid = models.AutoField(db_column='CityId', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cities'

    def __str__(self):
        return self.city + ", " + self.state


class Zipcodes(models.Model):
    zipcodeid = models.AutoField(db_column='ZipCodeId', primary_key=True)  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='CityId')  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZipCodes'

    def __str__(self):
        return self.cityid.city + ' - Zipcode'


class Completionrates(models.Model):
    completionrateid = models.AutoField(db_column='CompletionRateId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    completion_rate_4yr_150_white = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_black = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_hispanic = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_asian = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_aian = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_nhpi = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_2ormore = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_nonresident_alien = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150_race_unknown = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_white = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_black = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_hispanic = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_asian = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_aian = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_nhpi = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_2ormore = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_nonresident_alien = models.FloatField(blank=True, null=True)
    completion_rate_l4yr_150_race_unknown = models.FloatField(blank=True, null=True)
    completion_rate_4yr_200nt = models.FloatField(blank=True, null=True)
    completion_rate_less_than_4yr_200nt = models.FloatField(blank=True, null=True)
    completion_rate_4yr_150nt = models.FloatField(blank=True, null=True)
    completion_rate_less_than_4yr_150 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CompletionRates'

    def __str__(self):
        return self.institutionid.instname + ' - Completion Rate'


class Costs(models.Model):
    costsid = models.AutoField(db_column='CostsId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    avg_net_price_public = models.FloatField(blank=True, null=True)
    avg_net_price_private = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_0_to_30000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_30001_to_48000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_48001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_75001_to_110000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_110001_to_plus = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_0_to_30000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_30001_to_48000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_48001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_75001_to_110000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_110001_to_plus = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_0_to_48000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_0_to_48000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_30001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_30001_to_75000 = models.FloatField(blank=True, null=True)
    net_price_public_by_income_level_75000_to_plus = models.FloatField(blank=True, null=True)
    net_price_private_by_income_level_75000_to_plus = models.FloatField(blank=True, null=True)
    attendance_academic_year = models.FloatField(blank=True, null=True)
    attendance_program_year = models.FloatField(blank=True, null=True)
    tuition_in_state = models.FloatField(blank=True, null=True)
    tuition_out_of_state = models.FloatField(blank=True, null=True)
    tuition_program_year = models.FloatField(blank=True, null=True)
    instructional_expenditure_per_fte = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Costs'

    def __str__(self):
        return self.institutionid.instname + ' - Cost'


class Institutiontypes(models.Model):
    institutiontypeid = models.AutoField(db_column='InstitutionTypeId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey('Institutions', models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    ccbasic = models.IntegerField(db_column='CCBASIC', blank=True, null=True)  # Field name made lowercase.
    ccugprof = models.IntegerField(db_column='CCUGPROF', blank=True, null=True)  # Field name made lowercase.
    ccsizset = models.IntegerField(db_column='CCSIZSET', blank=True, null=True)  # Field name made lowercase.
    hbcu = models.TextField(db_column='HBCU', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pbi = models.TextField(db_column='PBI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    annhi = models.TextField(db_column='ANNHI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tribal = models.TextField(db_column='TRIBAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aanapii = models.TextField(db_column='AANAPII', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hsi = models.TextField(db_column='HSI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nanti = models.TextField(db_column='NANTI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    menonly = models.TextField(db_column='MENONLY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    womenonly = models.TextField(db_column='WOMENONLY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relaffil = models.IntegerField(db_column='RELAFFIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstitutionTypes'

    def __str__(self):
        return self.institutionid.instname + ' - Institution Type'


class Majors(models.Model):
    majorid = models.AutoField(db_column='MajorId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institutions, models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    agriculture = models.FloatField(blank=True, null=True)
    resources = models.FloatField(blank=True, null=True)
    architecture = models.FloatField(blank=True, null=True)
    ethnic_cultural_gender = models.FloatField(blank=True, null=True)
    communication = models.FloatField(blank=True, null=True)
    communications_technology = models.FloatField(blank=True, null=True)
    computer = models.FloatField(blank=True, null=True)
    personal_culinary = models.FloatField(blank=True, null=True)
    education = models.FloatField(blank=True, null=True)
    engineering = models.FloatField(blank=True, null=True)
    engineering_technology = models.FloatField(blank=True, null=True)
    language = models.FloatField(blank=True, null=True)
    family_consumer_science = models.FloatField(blank=True, null=True)
    legal = models.FloatField(blank=True, null=True)
    english = models.FloatField(blank=True, null=True)
    humanities = models.FloatField(blank=True, null=True)
    library = models.FloatField(blank=True, null=True)
    biological = models.FloatField(blank=True, null=True)
    mathematics = models.FloatField(blank=True, null=True)
    military = models.FloatField(blank=True, null=True)
    multidiscipline = models.FloatField(blank=True, null=True)
    parks_recreation_fitness = models.FloatField(blank=True, null=True)
    philosophy_religious = models.FloatField(blank=True, null=True)
    theology_religious_vocation = models.FloatField(blank=True, null=True)
    physical_science = models.FloatField(blank=True, null=True)
    science_technology = models.FloatField(blank=True, null=True)
    psychology = models.FloatField(blank=True, null=True)
    security_law_enforcement = models.FloatField(blank=True, null=True)
    public_administration_social_service = models.FloatField(blank=True, null=True)
    social_science = models.FloatField(blank=True, null=True)
    construction = models.FloatField(blank=True, null=True)
    mechanic_repair_technology = models.FloatField(blank=True, null=True)
    precision_production = models.FloatField(blank=True, null=True)
    transportation = models.FloatField(blank=True, null=True)
    visual_performing = models.FloatField(blank=True, null=True)
    health = models.FloatField(blank=True, null=True)
    business_marketing = models.FloatField(blank=True, null=True)
    history = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Majors'

    def __str__(self):
        return self.institutionid.instname + ' - Majors'


class Programs(models.Model):
    programsid = models.AutoField(db_column='ProgramsId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institutions, models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    program_certificate_lt_1_yr_agriculture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_agriculture = models.IntegerField(blank=True, null=True)
    program_assoc_agriculture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_agriculture = models.IntegerField(blank=True, null=True)
    program_bachelors_agriculture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_resources = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_resources = models.IntegerField(blank=True, null=True)
    program_assoc_resources = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_resources = models.IntegerField(blank=True, null=True)
    program_bachelors_resources = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_architecture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_architecture = models.IntegerField(blank=True, null=True)
    program_assoc_architecture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_architecture = models.IntegerField(blank=True, null=True)
    program_bachelors_architecture = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_assoc_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_bachelors_ethnic_cultural_gender = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_communication = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_communication = models.IntegerField(blank=True, null=True)
    program_assoc_communication = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_communication = models.IntegerField(blank=True, null=True)
    program_bachelors_communication = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_communications_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_communications_technology = models.IntegerField(blank=True, null=True)
    program_assoc_communications_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_communications_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_communications_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_computer = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_computer = models.IntegerField(blank=True, null=True)
    program_assoc_computer = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_computer = models.IntegerField(blank=True, null=True)
    program_bachelors_computer = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_personal_culinary = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_personal_culinary = models.IntegerField(blank=True, null=True)
    program_assoc_personal_culinary = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_personal_culinary = models.IntegerField(blank=True, null=True)
    program_bachelors_personal_culinary = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_education = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_education = models.IntegerField(blank=True, null=True)
    program_assoc_education = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_education = models.IntegerField(blank=True, null=True)
    program_bachelors_education = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_engineering = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_engineering = models.IntegerField(blank=True, null=True)
    program_assoc_engineering = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_engineering = models.IntegerField(blank=True, null=True)
    program_bachelors_engineering = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_engineering_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_engineering_technology = models.IntegerField(blank=True, null=True)
    program_assoc_engineering_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_engineering_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_engineering_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_language = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_language = models.IntegerField(blank=True, null=True)
    program_assoc_language = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_language = models.IntegerField(blank=True, null=True)
    program_bachelors_language = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_assoc_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_bachelors_family_consumer_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_legal = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_legal = models.IntegerField(blank=True, null=True)
    program_assoc_legal = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_legal = models.IntegerField(blank=True, null=True)
    program_bachelors_legal = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_english = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_english = models.IntegerField(blank=True, null=True)
    program_assoc_english = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_english = models.IntegerField(blank=True, null=True)
    program_bachelors_english = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_humanities = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_humanities = models.IntegerField(blank=True, null=True)
    program_assoc_humanities = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_humanities = models.IntegerField(blank=True, null=True)
    program_bachelors_humanities = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_library = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_library = models.IntegerField(blank=True, null=True)
    program_assoc_library = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_library = models.IntegerField(blank=True, null=True)
    program_bachelors_library = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_biological = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_biological = models.IntegerField(blank=True, null=True)
    program_assoc_biological = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_biological = models.IntegerField(blank=True, null=True)
    program_bachelors_biological = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_mathematics = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_mathematics = models.IntegerField(blank=True, null=True)
    program_assoc_mathematics = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_mathematics = models.IntegerField(blank=True, null=True)
    program_bachelors_mathematics = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_military = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_military = models.IntegerField(blank=True, null=True)
    program_assoc_military = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_military = models.IntegerField(blank=True, null=True)
    program_bachelors_military = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_multidiscipline = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_multidiscipline = models.IntegerField(blank=True, null=True)
    program_assoc_multidiscipline = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_multidiscipline = models.IntegerField(blank=True, null=True)
    program_bachelors_multidiscipline = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_assoc_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_bachelors_parks_recreation_fitness = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_assoc_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_bachelors_philosophy_religious = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_assoc_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_bachelors_theology_religious_vocation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_physical_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_physical_science = models.IntegerField(blank=True, null=True)
    program_assoc_physical_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_physical_science = models.IntegerField(blank=True, null=True)
    program_bachelors_physical_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_science_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_science_technology = models.IntegerField(blank=True, null=True)
    program_assoc_science_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_science_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_science_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_psychology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_psychology = models.IntegerField(blank=True, null=True)
    program_assoc_psychology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_psychology = models.IntegerField(blank=True, null=True)
    program_bachelors_psychology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_assoc_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_bachelors_security_law_enforcement = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_assoc_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_bachelors_public_administration_social_service = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_social_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_social_science = models.IntegerField(blank=True, null=True)
    program_assoc_social_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_social_science = models.IntegerField(blank=True, null=True)
    program_bachelors_social_science = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_construction = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_construction = models.IntegerField(blank=True, null=True)
    program_assoc_construction = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_construction = models.IntegerField(blank=True, null=True)
    program_bachelors_construction = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_assoc_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_bachelors_mechanic_repair_technology = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_precision_production = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_precision_production = models.IntegerField(blank=True, null=True)
    program_assoc_precision_production = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_precision_production = models.IntegerField(blank=True, null=True)
    program_bachelors_precision_production = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_transportation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_transportation = models.IntegerField(blank=True, null=True)
    program_assoc_transportation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_transportation = models.IntegerField(blank=True, null=True)
    program_bachelors_transportation = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_visual_performing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_visual_performing = models.IntegerField(blank=True, null=True)
    program_assoc_visual_performing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_visual_performing = models.IntegerField(blank=True, null=True)
    program_bachelors_visual_performing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_health = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_health = models.IntegerField(blank=True, null=True)
    program_assoc_health = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_health = models.IntegerField(blank=True, null=True)
    program_bachelors_health = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_business_marketing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_business_marketing = models.IntegerField(blank=True, null=True)
    program_assoc_business_marketing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_business_marketing = models.IntegerField(blank=True, null=True)
    program_bachelors_business_marketing = models.IntegerField(blank=True, null=True)
    program_certificate_lt_1_yr_history = models.IntegerField(blank=True, null=True)
    program_certificate_lt_2_yr_history = models.IntegerField(blank=True, null=True)
    program_assoc_history = models.IntegerField(blank=True, null=True)
    program_certificate_lt_4_yr_history = models.IntegerField(blank=True, null=True)
    program_bachelors_history = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Programs'

    def __str__(self):
        return self.institutionid.instname + ' - ProgramID'


class Undergraduates(models.Model):
    undergraduateid = models.AutoField(db_column='UndergraduateId', primary_key=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institutions, models.DO_NOTHING, db_column='InstitutionId')  # Field name made lowercase.
    enrollment_degree_seeking = models.FloatField(blank=True, null=True)
    demographics_white = models.FloatField(blank=True, null=True)
    demographics_black = models.FloatField(blank=True, null=True)
    demographics_hispanic = models.FloatField(blank=True, null=True)
    demographics_ai_an = models.FloatField(blank=True, null=True)
    demographics_asian = models.FloatField(blank=True, null=True)
    demographics_nhpi = models.FloatField(blank=True, null=True)
    demographics_multiracial = models.FloatField(blank=True, null=True)
    demographics_non_resident_alien = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Undergraduates'

    def __str__(self):
        return self.institutionid.instname + ' - Undergraduates'
