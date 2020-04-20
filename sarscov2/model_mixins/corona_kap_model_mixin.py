from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from edc_constants.choices import (
    TRUE_FALSE_DONT_KNOW,
    YES_NO,
    YES_NO_NA,
    YES_NO_UNKNOWN,
)
from edc_model import models as edc_models

from ..choices import (
    EMPLOYMENT_LEVELS,
    EMPLOYMENT_STATUS,
    HEALTH_INSURANCE,
    HEALTH_OPINION,
    LIKELIHOOD_SCALE,
    PROFESSIONS,
    WORRY_SCALE,
)


class CoronaKapDiseaseModelMixin(models.Model):

    # Disease burden
    hiv_pos = models.CharField(
        verbose_name=mark_safe("Does the patient have <u>HIV</u> infection?"),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    hiv_pos_year = models.IntegerField(
        verbose_name=mark_safe("What year did you <u>first test positive</u>?"),
        validators=[MinValueValidator(1950), MinValueValidator(2020)],
        null=True,
        blank=True,
    )

    hiv_pos_year = models.IntegerField(
        verbose_name=mark_safe("If Yes, what year did you first test positive?"),
        validators=[MinValueValidator(1950), MinValueValidator(2020)],
        null=True,
        blank=True,
    )

    hiv_year_started_art = models.IntegerField(
        verbose_name="If Yes, what year did you did you <u>start antiretroviral therapy</u>?",
        validators=[MinValueValidator(0)],
        help_text="in months",
        null=True,
        blank=True,
    )
    diabetic = models.CharField(
        verbose_name=mark_safe("Have you been diagnosed with <u>diabetes</u>?"),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    diabetic_dx_year = models.IntegerField(
        verbose_name=mark_safe(
            "If Yes, what year did you first learn you had <u>diabetes</u>?"
        ),
        validators=[MinValueValidator(1950), MinValueValidator(2020)],
        null=True,
        blank=True,
    )

    diabetic_on_meds = models.CharField(
        verbose_name=mark_safe(
            "If Yes, are you taking medications to control your <u>diabetes</u>?"
        ),
        max_length=25,
        choices=YES_NO_NA,
    )

    hypertensive = models.CharField(
        verbose_name=mark_safe("Have you been diagnosed with <u>hypertension</u>?"),
        max_length=25,
        choices=YES_NO_UNKNOWN,
    )

    hypertensive_dx_year = models.IntegerField(
        verbose_name=mark_safe(
            "If Yes, what year did you first learn you had <u>hypertension</u>?"
        ),
        validators=[MinValueValidator(1950), MinValueValidator(2020)],
        null=True,
        blank=True,
    )
    hypertensive_on_meds = models.CharField(
        verbose_name=mark_safe(
            "If Yes, are you taking medications to control your <u>hypertension</u>?"
        ),
        max_length=25,
        choices=YES_NO_NA,
    )

    weight = edc_models.WeightField(null=True, blank=True)

    height = edc_models.HeightField(null=True, blank=True)

    sys_blood_pressure = edc_models.SystolicPressureField(null=True, blank=True)

    dia_blood_pressure = edc_models.DiastolicPressureField(null=True, blank=True)

    class Meta:
        abstract = True


class CoronaKapModelMixin(models.Model):

    # PART2
    married = models.CharField(
        verbose_name="Are you currently married?", max_length=25, choices=YES_NO,
    )

    employment_status = models.CharField(
        verbose_name="Are you employed?", max_length=25, choices=EMPLOYMENT_STATUS,
    )

    shared_housing_one = models.IntegerField(
        verbose_name="How many people live together in your dwelling?",
    )

    shared_housing_two = models.IntegerField(
        verbose_name=(
            "In a typical month, how many different people "
            "spend more than one night at your current dwelling?"
        ),
    )

    employment = models.CharField(
        verbose_name="What type of employment are you involved in?",
        max_length=25,
        choices=PROFESSIONS,
    )

    employment_other = edc_models.OtherCharField(null=True, blank=True)

    education = models.CharField(
        verbose_name="What is your highest completed education level?",
        max_length=25,
        choices=EMPLOYMENT_LEVELS,
    )

    health_insurance = models.CharField(
        verbose_name="How are you covered for your health care expenses?",
        max_length=25,
        choices=HEALTH_INSURANCE,
    )

    health_insurance_other = edc_models.OtherCharField(null=True, blank=True)

    personal_health_opinion = models.CharField(
        verbose_name="In your opinion, what is your health like?",
        max_length=25,
        choices=HEALTH_OPINION,
    )

    # PART3
    perceived_threat = models.IntegerField(
        verbose_name=(
            "On a scale from 1-10, how serious of a public "
            "health threat is coronavirus?"
        ),
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="On a scale from 1-10",
    )

    corona_concern = models.CharField(
        verbose_name="How worried are you about getting coronavirus?",
        max_length=25,
        choices=WORRY_SCALE,
    )

    personal_infection_likelihood = models.CharField(
        verbose_name=(
            "How likely do you think it is that <u>you</u> "
            "will get sick from coronavirus?"
        ),
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )

    family_infection_likelihood = models.CharField(
        verbose_name=(
            "How likely do you think it is that <u>someone in your family</u> "
            "will get sick from coronavirus?"
        ),
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )

    perc_die = models.IntegerField(
        verbose_name=(
            "Out of every 100 people who get infected with "
            "coronavirus, how many do you think <u>will die</u>?"
        ),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="On a scale from 0-100",
    )

    perc_mild_symptom = models.IntegerField(
        verbose_name=(
            "Out of every 100 people who get infected with coronavirus, "
            "how many do you think <u>will have only mild symptoms</u>?"
        ),
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="On a scale from 0-100",
    )

    # PART 4
    spread_droplets = models.CharField(
        verbose_name=(
            "Coronavirus spreads by droplets from cough and sneezes "
            "from people infected with coronavirus"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    spread_touch = models.CharField(
        verbose_name="Coronavirus can spread by people touching each other",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    spread_sick = models.CharField(
        verbose_name="People can transmit coronavirus when they are sick ",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    spread_asymptomatic = models.CharField(
        verbose_name=(
            "People can transmit coronavirus even when they do not appear to be sick"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    severity_age = models.CharField(
        verbose_name="Coronavirus is more severe in older people than children",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    severity_hiv = models.CharField(
        verbose_name="Coronavirus is more severe in people with <u>HIV infection</u>",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    severity_diabetes_hypertension = models.CharField(
        verbose_name=(
            "Coronavirus is more severe "
            "in people with <u>diabetes</u> and/or <u>hypertension</u>"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    hot_climate = models.CharField(
        verbose_name="Coronavirus does not survive in the hot climate",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    lives_on_materials = models.CharField(
        verbose_name="Coronavirus can live on clothes, plastics, cardboard for a day or more",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    spread_touch2 = models.CharField(
        verbose_name=(
            "You can catch coronavirus if you touch an infected "
            "area and then touch your face or eyes"
        ),
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    # PART 5
    symptoms_fever = models.CharField(
        verbose_name="Fever", max_length=25, choices=TRUE_FALSE_DONT_KNOW,
    )
    symptoms_headache = models.CharField(
        verbose_name="Headache", max_length=25, choices=TRUE_FALSE_DONT_KNOW,
    )

    symptoms_dry_cough = models.CharField(
        verbose_name="Dry persistant cough",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    symptoms_body_aches = models.CharField(
        verbose_name="Body aches", max_length=25, choices=TRUE_FALSE_DONT_KNOW,
    )

    symptoms_smell = models.CharField(
        verbose_name="Loss of taste and smell",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    symptoms_breathing = models.CharField(
        verbose_name="Fast or difficult breathing",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    know_other_symptoms = models.CharField(
        verbose_name="Do you know of any other symptoms of coronavirus?",
        max_length=25,
        choices=YES_NO,
    )
    symptoms_other = models.TextField(
        verbose_name="Please list any other symptoms of coronavirus that you are aware of:",
        max_length=250,
        null=True,
        blank=True,
    )

    # PART 6
    hot_drinks = models.CharField(
        verbose_name="Drink warm water or hot drinks like tea or coffee",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    alcohol = models.CharField(
        verbose_name="Drink alcohol, spirits, etc",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    wash_hands = models.CharField(
        verbose_name="Wash hands with soap and warm water",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    hand_sanitizer = models.CharField(
        verbose_name="Use hand sanitisers with alcohol",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    avoid_crowds = models.CharField(
        verbose_name="Avoid crowded places such as markets and public transport",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )
    face_masks = models.CharField(
        verbose_name="Wear a face mask", max_length=25, choices=TRUE_FALSE_DONT_KNOW,
    )
    stay_indoors = models.CharField(
        verbose_name="Stay indoors", max_length=25, choices=TRUE_FALSE_DONT_KNOW,
    )
    social_distance = models.CharField(
        verbose_name="Keep at least a 2 metre distance from people",
        max_length=25,
        choices=TRUE_FALSE_DONT_KNOW,
    )

    # PART 7
    stay_home = models.CharField(
        verbose_name="Stay at home and avoid people",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )
    visit_clinic = models.CharField(
        verbose_name="Go to the nearest health facility",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )
    call_nurse = models.CharField(
        verbose_name="Call your nurse and tell them you are sick",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )
    take_meds = models.CharField(
        verbose_name="Take medicines like chloroquine",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )
    stop_chronic_meds = models.CharField(
        verbose_name="Stop taking your chronic disease medicines",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
        help_text="For example, medicines for diabetes, hypertension and/or HIV",
    )

    visit_religious = models.CharField(
        verbose_name="Go to a religious leader instead of a doctor",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )

    visit_traditional = models.CharField(
        verbose_name="Go to a traditional healer instead of a doctor",
        max_length=25,
        choices=LIKELIHOOD_SCALE,
    )

    class Meta:
        abstract = True
