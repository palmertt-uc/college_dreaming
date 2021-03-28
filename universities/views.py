from django.shortcuts import render, get_object_or_404
from .serializers import InstitutionsSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
from .filters import InstitutionFilter, UserFilter
from users.models import Profile
from .models import Institutions, Crime, Zipcodes, Cities, Admissions, Completionrates, Costs, \
    Institutiontypes, Majors, Programs, Undergraduates
import logging


# Create your views here.
class QuizView(ListView):
    model = Institutions
    template_name = 'universities/quiz.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_queryset(self):
        costs = self.request.GET.get('costs')
        state = self.request.GET.get('state')
        actMath = self.request.GET.get("mathACT")
        actScience = self.request.GET.get("scienceACT")
        actReading = self.request.GET.get("readingACT")
        actWriting = self.request.GET.get("writingACT")
        satMath = self.request.GET.get("mathSAT")
        satReading = self.request.GET.get("readingSAT")
        satWriting = self.request.GET.get("writingSAT")

        query_dict = {
            "contLowCosts":(Q(costs__tuition_in_state__lte=2500) & ~Q(zipcodeid__cityid__state=state)) | (Q(costs__tuition_out_of_state__lte=2500) & ~Q(zipcodeid__cityid__state=state)),
            "contMedCosts":(Q(costs__tuition_in_state__lte=10000) & ~Q(zipcodeid__cityid__state=state)) | (Q(costs__tuition_out_of_state__lte=10000) & ~Q(zipcodeid__cityid__state=state)),
            "contHighCosts":(Q(costs__tuition_in_state__gte=0) & ~Q(zipcodeid__cityid__state=state)) | (Q(costs__tuition_out_of_state__gte=0) & ~Q(zipcodeid__cityid__state=state)),
            "contLowSelectivity":(Q(admissions__admission_rate_overall__gte=.7) | Q(admissions__admission_rate_overall=0)),
            "contMedSelectivity":(Q(admissions__admission_rate_overall__gte=.5) | Q(admissions__admission_rate_overall=0)),
            "contHighSelectivity":(Q(admissions__admission_rate_overall__lte=.5) & ~Q(admissions__admission_rate_overall=0)),
            "contNoPrefInstitution":Q(institutiontypes__gte=0),
            "contNoneInstitution":(Q(institutiontypes__hbcu=0) & (Q(institutiontypes__pbi=0)) & Q(institutiontypes__annhi=0) & Q(institutiontypes__tribal=0) & Q(institutiontypes__aanapii=0) & Q(institutiontypes__hsi=0) & Q(institutiontypes__nanti=0)
                                   & Q(institutiontypes__menonly=0) & Q(institutiontypes__womenonly=0) & Q(institutiontypes__relaffil=0)),
            "contHBInstitution":Q(institutiontypes__hbcu=1),
            "contHBInstitution": Q(institutiontypes__pbi=1),
            "contHBInstitution": Q(institutiontypes__annhi=1),
            "contNAInstitution":Q(institutiontypes__tribal=1),
            "contAAPIInstitution":Q(institutiontypes__aanapii=1),
            "contHBInstitution": Q(institutiontypes__hsi=1),
            "contHBInstitution": Q(institutiontypes__nanti=1),
            "contMenInstitution":Q(institutiontypes__menonly=1),
            "contWomenInstitution":Q(institutiontypes__womenonly=1),
            "contHBInstitution": Q(institutiontypes__relaffil=1),
            "contPublic":Q(costs__avg_net_price_public__gt=0),
            "contPrivate":Q(costs__avg_net_price_private__gt=0),
            "contNoPrefType":(Q(costs__avg_net_price_public__gt=0) | Q(costs__avg_net_price_private__gt=0)),
            "contSmallSize":Q(undergraduates__enrollment_degree_seeking__lte=250),
            "contMedSize":(Q(undergraduates__enrollment_degree_seeking__gte=500) & Q(undergraduates__enrollment_degree_seeking__lte=2000)),
            "contLargeSize":Q(undergraduates__enrollment_degree_seeking__gte=2000),
            "contNoPrefSize":Q(undergraduates__enrollment_degree_seeking__gte=0),
            "contNoPrefGradRate":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contAvgGradRate_white":Q(completionrates__completion_rate_4yr_150_white__gte=.5),
            "contHighGradRate_white":Q(completionrates__completion_rate_4yr_150_white__gte=.7),
            "contAvgGradRate_black": Q(completionrates__completion_rate_4yr_150_black__gte=.5),
            "contHighGradRate_black": Q(completionrates__completion_rate_4yr_150_black__gte=.7),
            "contAvgGradRate_asian": Q(completionrates__completion_rate_4yr_150_asian__gte=.5),
            "contHighGradRate_asian": Q(completionrates__completion_rate_4yr_150_asian__gte=.7),
            "contAvgGradRate_hispanic": Q(completionrates__completion_rate_4yr_150_hispanic__gte=.5),
            "contHighGradRate_hispanic": Q(completionrates__completion_rate_4yr_150_hispanic__gte=.7),
            "contAvgGradRate_aian": Q(completionrates__completion_rate_4yr_150_aian__gte=.5),
            "contHighGradRate_aian": Q(completionrates__completion_rate_4yr_150_aian__gte=.7),
            "contAvgGradRate_nhpi": Q(completionrates__completion_rate_4yr_150_nhpi__gte=.5),
            "contHighGradRate_nhpi": Q(completionrates__completion_rate_4yr_150_nhpi__gte=.7),
            "contAvgGradRate_2ormore": Q(completionrates__completion_rate_4yr_150_2ormore__gte=.5),
            "contHighGradRate_2ormore": Q(completionrates__completion_rate_4yr_150_2ormore__gte=.7),
            "contAvgGradRate_none": Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contHighGradRate_none": Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contNoPrefHousingCosts": (Q(zipcodeid__hpi__gte=-50) | Q(zipcodeid__hpi='null')),
            "contLowHousingCosts":(Q(zipcodeid__hpi__lte=300) | Q(zipcodeid__hpi='null')),
            "contMedHousingCosts":(Q(zipcodeid__hpi__lte=-450) | Q(zipcodeid__hpi='null')),
            "contNoPrefEarnings":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contEarnings":(Q(earnings__fiveyear50pct__gte=41340) & Q(earnings__degree_level = 5)),
            "contNoPrefCrime":(~Q(zipcodeid__cityid__crimeid=-1)),
            "contViolentCrime":(Q(zipcodeid__cityid__crimeid__violentcrimes__lte=325) | Q(zipcodeid__cityid__crimeid='null')),
            "contPropertyCrime":(Q(zipcodeid__cityid__crimeid__propertycrimes__lte=2225) | Q(zipcodeid__cityid__crimeid='null')),
            "contBothCrime":((Q(zipcodeid__cityid__crimeid__violentcrimes__lte=325) | Q(zipcodeid__cityid__crimeid='null')) & (Q(zipcodeid__cityid__crimeid__propertycrimes__lte=2225) | Q(zipcodeid__cityid__crimeid='null'))),
            "contNoPrefCommunity":~Q(locale=-1),
            "contRuralCommunity":(Q(locale=31) | Q(locale=32) | Q(locale=33) | Q(locale=41) | Q(locale=42) | Q(locale=43)),
            "contSuburbanCommunity":(Q(locale=13) | Q(locale=21) | Q(locale=22) | Q(locale=23)),
            "contUrbanCommunity":(Q(locale=12) | Q(locale=11)),
            "contRuralSuburbanCommunity":((Q(locale=31) | Q(locale=32) | Q(locale=33) | Q(locale=41) | Q(locale=42) | Q(locale=43)) | (Q(locale=13) | Q(locale=21) | Q(locale=22) | Q(locale=23))),
            "contRuralUrbanCommunity":((Q(locale=12) | Q(locale=11)) | (Q(locale=31) | Q(locale=32) | Q(locale=33) | Q(locale=41) | Q(locale=42) | Q(locale=43))),
            "contSuburbanUrbanCommunity":((Q(locale=12) | Q(locale=11)) | (Q(locale=13) | Q(locale=21) | Q(locale=22) | Q(locale=23))),
            "contNoPrefSummers":Q(climateid__maxtemp__gte=0),
            "contCoolSummers":Q(climateid__maxtemp__lte=60),
            "contWarmSummers":(Q(climateid__maxtemp__lte=80) & Q(climateid__maxtemp__gte=60)),
            "contHotSummers":Q(climateid__maxtemp__gte=80),
            "contNoPrefWinters":Q(climateid__mintemp__lte=100),
            "contColdWinters":Q(climateid__mintemp__lte=0),
            "contCoolWinters":(Q(climateid__mintemp__lte=60) & Q(climateid__mintemp__gte=40)),
            "contWarmWinters":Q(climateid__mintemp__gte=60),
            "contNoPrefSnow":(Q(climateid__snow__gte=0) | Q(climateid__snow='null')),
            "contNoSnow":(Q(climateid__snow__lte=10) | Q(climateid__snow='null')),
            "contSomeSnow":((Q(climateid__snow__gte=20) & Q(climateid__snow__lte=40))| Q(climateid__snow='null')),
            "contLotsOfSnow":(Q(climateid__snow__gte=40) | Q(climateid__snow='null')),
            "contNoPrefSunny":(Q(climateid__sunlight__gte=0) | Q(climateid__sunlight='null')),
            "contSunny":(Q(climateid__sunlight__lte=10) | Q(climateid__sunlight='null')),
            "actMath":((Q(admissions__act_scores_25th_percentile_math__lte=actMath) & Q(admissions__act_scores_75th_percentile_math__gte=actMath)) | Q(admissions__act_scores_75th_percentile_math__gte=0)),
            "actReading": ((Q(admissions__act_scores_25th_percentile_english__lte=actReading) & Q(admissions__act_scores_75th_percentile_english__gte=actReading)) | Q(admissions__act_scores_75th_percentile_english__gte=0)),
            "actWriting": ((Q(admissions__act_scores_25th_percentile_writing__lte=actWriting) & Q(admissions__act_scores_75th_percentile_writing__gte=actWriting)) | Q(admissions__act_scores_25th_percentile_writing__lte=0)),
            "actScience": Q(zipcodeid__gte=0),
            "satMath": ((Q(admissions__sat_scores_25th_percentile_math__lte=satMath) & Q(admissions__sat_scores_75th_percentile_math__gte=satMath)) | Q(admissions__sat_scores_75th_percentile_math__gte=0) | Q(admissions__sat_scores_25th_percentile_math__lte=0)),
            "satReading": ((Q(admissions__sat_scores_25th_percentile_critical_reading__lte=satReading) & Q(admissions__sat_scores_75th_percentile_critical_reading__gte=satReading)) | Q(admissions__sat_scores_25th_percentile_critical_reading__lte=0)),
            "satWriting": ((Q(admissions__sat_scores_25th_percentile_writing__lte=satWriting) & Q(admissions__sat_scores_75th_percentile_writing__gte=satWriting)) | Q(admissions__sat_scores_25th_percentile_writing__lte=0)),
            None:Q(zipcodeid__gte=0)
        }
        filters = Q()

        if costs is not None:
            selectivity = self.request.GET.get('selectivity')
            special = self.request.GET.get('special')
            institution_type = self.request.GET.get('type')
            size = self.request.GET.get('size')
            grad_rate = str(self.request.GET.get('gradRate') + self.request.GET.get('ethnicity'))
            housing_costs = self.request.GET.get('housing_costs')
            earnings = self.request.GET.get('earnings')
            crime = self.request.GET.get('crime')
            community = self.request.GET.get('community')
            summers = self.request.GET.get('summers')
            winters = self.request.GET.get('winters')
            snowy = self.request.GET.get('snowy')
            sunny = self.request.GET.get('sunny')
            business_program = self.request.GET.get('business_major')
            science_math_program = self.request.GET.get('science_math')
            engineering_technology = self.request.GET.get('engineering_technology')
            literature_language = self.request.GET.get('literature_language')
            arts_other = self.request.GET.get('arts_other')
            social_science = self.request.GET.get('social_science')

            business_filters = (Q(majors__business_marketing__gte=business_program) |
                                Q(majors__resources__gte=business_program) |
                                Q(majors__transportation__gte=business_program) |
                                Q(majors__construction__gte=business_program))
            science_math_filters = (Q(majors__health__gte=science_math_program) |
                                    Q(majors__mathematics__gte=science_math_program) |
                                    Q(majors__biological__gte=science_math_program) |
                                    Q(majors__family_consumer_science__gte=science_math_program) |
                                    Q(majors__physical_science__gte=science_math_program) |
                                    Q(majors__agriculture__gte=science_math_program))
            engineering_technology_filters = (Q(majors__engineering__gte=engineering_technology) |
                                              Q(majors__engineering_technology__gte=engineering_technology) |
                                              Q(majors__communications_technology__gte=engineering_technology) |
                                              Q(majors__mechanic_repair_technology__gte=engineering_technology) |
                                              Q(majors__science_technology__gte=engineering_technology))
            literature_language_filters = (Q(majors__philosophy_religious__gte=literature_language) |
                                           Q(majors__theology_religious_vocation__gte=literature_language) |
                                           Q(majors__library__gte=literature_language) |
                                           Q(majors__history__gte=literature_language) |
                                           Q(majors__english__gte=literature_language) |
                                           Q(majors__communication__gte=literature_language) |
                                           Q(majors__language__gte=literature_language))
            arts_other_filters = (Q(majors__architecture__gte=arts_other) |
                                  Q(majors__visual_performing__gte=arts_other) |
                                  Q(majors__personal_culinary__gte=arts_other) |
                                  Q(majors__multidiscipline__gte=arts_other) |
                                  Q(majors__military__gte=arts_other) |
                                  Q(majors__parks_recreation_fitness__gte=arts_other))
            social_science_filters = (Q(majors__social_science__gte=social_science) |
                                      Q(majors__public_administration_social_service__gte=social_science) |
                                      Q(majors__ethnic_cultural_gender__gte=social_science) |
                                      Q(majors__psychology__gte=social_science) |
                                      Q(majors__education__gte=social_science) |
                                      Q(majors__legal__gte=social_science) |
                                      Q(majors__humanities__gte=social_science) |
                                      Q(majors__security_law_enforcement__gte=social_science))
            if actMath != None & actMath != "":
                filters |= query_dict["actMath"]
            if actScience != None & actScience != "":
                filters |= query_dict["actScience"]
            if actWriting != None & actWriting != "":
                filters |= query_dict["actWriting"]
            if actReading != None & actReading != "":
                filters |= query_dict["actReading"]
            if actMath != None & actMath != "":
                filters |= query_dict["satMath"]
            if actReading != None & actReading != "":
                filters |= query_dict["satReading"]
            if actWriting != None & actWriting != "":
                filters |= query_dict["satWriting"]

            filters |= query_dict[costs]
            filters |= query_dict[selectivity]
            filters |= query_dict[special]
            filters != query_dict[institution_type]
            filters |= query_dict[size]
            filters |= query_dict[grad_rate]
            filters |= query_dict[housing_costs]
            filters |= query_dict[earnings]
            filters |= query_dict[crime]
            filters |= query_dict[community]
            filters |= query_dict[summers]
            filters |= query_dict[winters]
            filters |= query_dict[snowy]
            filters |= query_dict[sunny]
            filters |= query_dict[costs]

            filters |= business_filters
            filters |= science_math_filters
            filters |= engineering_technology_filters
            filters |= literature_language_filters
            filters |= arts_other_filters
            filters |= social_science_filters

        return self.model.objects.filter(filters)


class UniversityListView(ListView):
    model = Institutions
    template_name = 'universities/universities.html'
    context_object_name = 'universities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institution_filter'] = InstitutionFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return InstitutionFilter(self.request.GET, queryset=queryset).qs


class UniversityDetailView(DetailView):
    model = Institutions

    def get_context_data(self, **kwargs):
        university = get_object_or_404(Institutions, pk=self.kwargs.get('pk'))
        favorited = bool
        university_costs = Costs.objects.all()
        university_admissions = Admissions.objects.all()
        university_undergraduates = Undergraduates.objects.all()
        university_completion_rate = Completionrates.objects.all()
        university_majors = Majors.objects.all()
        university_institutions = Institutions.objects.all()
        costs = {}
        admissions = {}
        undergraduates = {}
        completion = {}
        majors = {}
        institutions = {}

        for institution_dictionary in university_institutions:
            if university.institutionid == institution_dictionary.institutionid:
                institutions['latitude'] = str(institution_dictionary.latitude) + '</script>&amp;'
                institutions['longitude'] = str(institution_dictionary.longitude) + '</script>&amp;'
                institutions['instname'] = str(institution_dictionary.instname) + '</script>&amp;'

        for cost in university_costs:
            if university.institutionid == cost.costsid:
                costs['inStateTuition'] = str(cost.tuition_in_state) + '</script>&amp;'
                costs['outStateTuition'] = str(cost.tuition_out_of_state) + '</script>&amp;'

        for admission in university_admissions:
            if university.institutionid == admission.admissionid:
                admissions['actScore'] = str(admission.act_scores_midpoint_cumulative) + '</script>&amp;'
                admissions['satScore'] = str(admission.sat_scores_average_overall) + '</script>&amp;'
                admissions['admissionRate'] = str(admission.admission_rate_overall) + '</script>&amp;'

        for undergrads in university_undergraduates:
            if university.institutionid == undergrads.undergraduateid:
                undergraduates['caucasian'] = str(undergrads.demographics_white) + '</script>&amp;'
                undergraduates['africanAmerican'] = str(undergrads.demographics_black) + '</script>&amp;'
                undergraduates['hispanic'] = str(undergrads.demographics_hispanic) + '</script>&amp;'
                undergraduates['pacificIslander'] = str(undergrads.demographics_nhpi) + '</script>&amp;'
                undergraduates['multiRacial'] = str(undergrads.demographics_multiracial) + '</script>&amp;'
                undergraduates['nonResident'] = str(undergrads.demographics_non_resident_alien) + '</script>&amp;'
                undergraduates['asian'] = str(undergrads.demographics_asian) + '</script>&amp;'
                undergraduates['aian'] = str(undergrads.demographics_ai_an) + '</script>&amp;'

        for completion_rates in university_completion_rate:
            if university.institutionid == completion_rates.completionrateid:
                completion['whiteCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_white) + '</script>&amp;'
                completion['blackCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_black) + '</script>&amp;'
                completion['hispanicCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_hispanic) + '</script>&amp;'
                completion['asianCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_asian) + '</script>&amp;'
                completion['aianCompletionRate'] = str(completion_rates.completion_rate_4yr_150_aian) + '</script>&amp;'
                completion['pacificIslanderCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_nhpi) + '</script>&amp;'
                completion['multiRacialCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_2ormore) + '</script>&amp;'
                completion['nonResidentCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_nonresident_alien) + '</script>&amp;'
                completion['otherCompletionRate'] = str(
                    completion_rates.completion_rate_4yr_150_race_unknown) + '</script>&amp;'

        for major in university_majors:
            if university.institutionid == major.majorid:
                majors['agriculture'] = str(major.agriculture) + '</script>&amp;'
                majors['resources'] = str(major.resources) + '</script>&amp;'
                majors['architecture'] = str(major.architecture) + '</script>&amp;'
                majors['ethnicCulturalGender'] = str(major.ethnic_cultural_gender) + '</script>&amp;'
                majors['communication'] = str(major.communication) + '</script>&amp;'
                majors['communicationsTechnology'] = str(major.communications_technology) + '</script>&amp;'
                majors['computer'] = str(major.computer) + '</script>&amp;'
                majors['personalCulinary'] = str(major.personal_culinary) + '</script>&amp;'
                majors['education'] = str(major.education) + '</script>&amp;'
                majors['engineering'] = str(major.engineering) + '</script>&amp;'
                majors['engineeringTechnology'] = str(major.engineering_technology) + '</script>&amp;'
                majors['language'] = str(major.language) + '</script>&amp;'
                majors['familyConsumerScience'] = str(major.family_consumer_science) + '</script>&amp;'
                majors['legal'] = str(major.legal) + '</script>&amp;'
                majors['english'] = str(major.english) + '</script>&amp;'
                majors['humanities'] = str(major.humanities) + '</script>&amp;'
                majors['library'] = str(major.library) + '</script>&amp;'
                majors['biological'] = str(major.biological) + '</script>&amp;'
                majors['mathematics'] = str(major.mathematics) + '</script>&amp;'
                majors['military'] = str(major.military) + '</script>&amp;'
                majors['multiDiscipline'] = str(major.multidiscipline) + '</script>&amp;'
                majors['parksRecreationFitness'] = str(major.parks_recreation_fitness) + '</script>&amp;'
                majors['philosophyReligious'] = str(major.philosophy_religious) + '</script>&amp;'
                majors['theologyReligiousVocation'] = str(major.theology_religious_vocation) + '</script>&amp;'
                majors['physicalScience'] = str(major.physical_science) + '</script>&amp;'
                majors['scienceTechnology'] = str(major.science_technology) + '</script>&amp;'
                majors['psychology'] = str(major.psychology) + '</script>&amp;'
                majors['securityLawEnforcement'] = str(major.security_law_enforcement) + '</script>&amp;'
                majors['publicAdministration'] = str(major.public_administration_social_service) + '</script>&amp;'
                majors['socialScience'] = str(major.social_science) + '</script>&amp;'
                majors['construction'] = str(major.construction) + '</script>&amp;'
                majors['mechanicRepairTechnology'] = str(major.mechanic_repair_technology) + '</script>&amp;'
                majors['precisionProduction'] = str(major.precision_production) + '</script>&amp;'
                majors['transportation'] = str(major.transportation) + '</script>&amp;'
                majors['visualPerforming'] = str(major.visual_performing) + '</script>&amp;'
                majors['health'] = str(major.health) + '</script>&amp;'
                majors['businessMarketing'] = str(major.business_marketing) + '</script>&amp;'
                majors['history'] = str(major.history) + '</script>&amp;'

        if university.favorite.filter(id=self.request.user.id).exists():
            favorited = True

        context = super().get_context_data(**kwargs)
        context['admissions'] = admissions
        context['costs'] = costs
        context['institution_type'] = Institutiontypes.objects.all()
        context['majors'] = majors
        context['completion_rates'] = completion
        context['university_costs'] = university_costs
        context['undergraduates'] = undergraduates
        context['favorite'] = favorited
        context['university_admissions'] = university_admissions
        context['university_undergrads'] = university_undergraduates
        context['university_majors'] = university_majors
        context['university_institutions'] = institutions
        return context


def about(request):
    return render(request, 'universities/about.html')


def contact(request):
    return render(request, 'universities/contact.html')


@api_view(['GET'])
def institutionsList(request):
    print('cincinnati')
    query = request.GET.get('query')
    institutions = Institutions.objects.filter(instname__icontains=query)[:5]
    serializer = InstitutionsSerializer(institutions, many=True)
    return Response(serializer.data)


class UsersListView(ListView):
    model = Profile
    template_name = 'universities/user_list.html'
    context_object_name = 'profile'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_filter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return UserFilter(self.request.GET, queryset=queryset).qs


class UserDetailView(DetailView):
    model = Profile


class SearchResultsView(ListView):
    model = Institutions
    template_name = 'universities/search_results.html'
    context_object_name = 'universities'
    paginate_by = 26

    def get_queryset(self):
        query_dict = {
            "contLowCosts":(Q(costs__tuition_in_state__lte=5000) & Q(zipcodeid__cityid__state='OH')) | (Q(costs__tuition_out_of_state__lte=5000) & ~Q(zipcodeid__cityid__state='OH')),
            "contMedCosts":(Q(costs__tuition_in_state__lte=10000) & Q(zipcodeid__cityid__state='OH')) | (Q(costs__tuition_out_of_state__lte=10000) & ~Q(zipcodeid__cityid__state='OH')),
            "contHighCosts":(Q(costs__tuition_in_state__gte=0) & Q(zipcodeid__cityid__state='OH')) | (Q(costs__tuition_out_of_state__gte=0) & ~Q(zipcodeid__cityid__state='OH')),
            "contLowSelectivity":Q(admissions__admission_rate_overall__gte=.7),
            "contMedSelectivity":Q(admissions__admission_rate_overall__gte=.5),
            "contHighSelectivity":Q(admissions__admission_rate_overall__gte=0),
            "contNoPrefInstitution":Q(institutiontypes__gte=0),
            "contNoneInstitution":(Q(institutiontypes__hbcu=0) & (Q(institutiontypes__pbi=0)) & Q(institutiontypes__annhi=0) & Q(institutiontypes__tribal=0) & Q(institutiontypes__aanapii=0) & Q(institutiontypes__hsi=0) & Q(institutiontypes__nanti=0)
                                   & Q(institutiontypes__menonly=0) & Q(institutiontypes__womenonly=0) & Q(institutiontypes__relaffil=0)),
            "contHBInstitution":Q(institutiontypes__hbcu=1),
            "contNAInstitution":Q(institutiontypes__tribal=1),
            "contAAPIInstitution":Q(institutiontypes__aanapii=1),
            "contMenInstitution":Q(institutiontypes__menonly=1),
            "contWomenInstitution":Q(institutiontypes__womenonly=1),
            "contPublic":Q(costs__avg_net_price_public__gt=0),
            "contPrivate":Q(costs__avg_net_price_private__gt=0),
            "contNoPrefType":(Q(costs__avg_net_price_public__gt=0) | Q(costs__avg_net_price_private__gt=0)),
            "contSmallSize":Q(undergraduates__enrollment_degree_seeking__lte=1000),
            "contMedSize":(Q(undergraduates__enrollment_degree_seeking__gte=1000) & Q(undergraduates__enrollment_degree_seeking__lte=10000)),
            "contLargeSize":Q(undergraduates__enrollment_degree_seeking__gte=10000),
            "contNoPrefSize":Q(undergraduates__enrollment_degree_seeking__gte=0),
            "contNoPrefGradRate":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contAvgGradRate":Q(completionrates__completion_rate_4yr_150_white__gte=.5),
            "contHighGradRate":Q(completionrates__completion_rate_4yr_150_white__gte=.8),
            "contNoPrefHousingCosts":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contLowHousingCosts":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contMedHousingCosts":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contNoPrefJobs":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contEntryJobs":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contMyFieldJobs":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contBothJobs":Q(completionrates__completion_rate_4yr_150_white__gte=0),
            "contNoPrefCrime":(~Q(zipcodeid__cityid__crimeid=-1)),
            "contViolentCrime":(Q(zipcodeid__cityid__crimeid__violentCrimes__lte=100) | Q(zipcodeid__cityid__crimeid='null')),
            "contPropertyCrime":(Q(zipcodeid__cityid__crimeid__propertyCrimes__lte=100) | Q(zipcodeid__cityid__crimeid='null')),
            "contBothCrime":((Q(zipcodeid__cityid__crimeid__violentCrimes__lte=100) | Q(zipcodeid__cityid__crimeid='null')) & (Q(zipcodeid__cityid__crimeid__propertycrimes__lte=100) | Q(zipcodeid__cityid__crimeid='null'))),
            "contNoPrefCommunity":~Q(locale=-1),
            "contRuralCommunity":Q(locale=12),
            "contSuburbanCommunity":Q(locale=12),
            "contUrbanCommunity":Q(locale=12),
            "contRuralSuburbanCommunity":(Q(locale=12) | Q(locale=12)),
            "contRuralUrbanCommunity":(Q(locale=12) | Q(locale=12)),
            "contSuburbanUrbanCommunity":(Q(locale=12) | Q(locale=12)),
            "contNoPrefSummers":Q(climateid__maxtemp__gte=0),
            "contCoolSummers":Q(climateidd__maxtemp__lte=60),
            "contWarmSummers":(Q(climateid__maxtemp__lte=80) & Q(climateid__maxtemp__gte=60)),
            "contHotSummers":Q(climateid__maxtemp__gte=80),
            "contNoPrefWinters":Q(climateid__mintemp__lte=100),
            "contColdWinters":Q(climateid__mintemp__lte=0),
            "contCoolWinters":(Q(climateid__mintemp__lte=60) & Q(climateid__mintemp__gte=40)),
            "contWarmWinters":Q(climateid__mintemp__gte=60),
            "contNoPrefSnow":Q(climateid__maxtemp__gte=0),
            "contNoSnow":Q(climateid__maxtemp__gte=0),
            "contSomeSnow":Q(climateid__maxtemp__gte=0),
            "contLotsOfSnow":Q(climateid__maxtemp__gte=0),
            "contNoPrefSunny":Q(climateid__maxtemp__gte=0),
            "contSunny":Q(climateid__maxtemp__gte=0),
            None: Q(zipcodeid__gte=0)
        }
        filters = Q(zipcodeid__gte=0)

        costs = self.request.GET.get('costs')
        selectivity = self.request.GET.get('selectivity')
        special = self.request.GET.get('special')
        institution_type = self.request.GET.get('type')
        size = self.request.GET.get('size')
        grad_rate = self.request.GET.get('gradRate')
        housing_costs = self.request.GET.get('housing_costs')
        job_availability = self.request.GET.get('job_availability')
        crime = self.request.GET.get('crime')
        community = self.request.GET.get('community')
        summers = self.request.GET.get('summers')
        winters = self.request.GET.get('winters')
        snowy = self.request.GET.get('snowy')
        sunny = self.request.GET.get('sunny')
        logger = logging.getLogger(__name__)
        filters &= query_dict[costs]
        filters &= query_dict[selectivity]
        filters &= query_dict[special]
        filters &= query_dict[institution_type]
        filters &= query_dict[size]
        filters &= query_dict[grad_rate]
        filters &= query_dict[housing_costs]
        filters &= query_dict[job_availability]
        filters &= query_dict[crime]
        filters &= query_dict[community]
        filters &= query_dict[summers]
        filters &= query_dict[winters]
        filters &= query_dict[snowy]
        filters &= query_dict[sunny]
        filters &= query_dict[costs]

        logger.warning(str(filters.children[5]))
        return self.model.objects.filter(filters)



class UniversitySearchResultView(ListView):
    model = Institutions
    template_name = 'universities/university_search_results.html'
    context_object_name = 'universities'
    paginate_by = 26

    def get_queryset(self):
        queryset = super().get_queryset()
        return InstitutionFilter(self.request.GET, queryset=queryset).qs
