from edc_constants.constants import YES
from edc_form_validators.form_validator import FormValidator


class CoronaKapFormValidator(FormValidator):
    def clean(self):
        self.required_if(YES, field="hiv_pos", field_required="hiv_pos_year")
        self.required_if(YES, field="hiv_pos", field_required="hiv_year_started_art")
        self.required_if(YES, field="hiv_pos", field_required="hiv_missed_doses")
        self.required_if(YES, field="diabetic", field_required="diabetic_dx_year")
        self.applicable_if(YES, field="diabetic", field_applicable="diabetes_on_meds")
        self.required_if(YES, field="diabetic", field_required="diabetic_missed_doses")
        self.required_if(
            YES, field="hypertensive", field_required="hypertensive_dx_year"
        )
        self.applicable_if(
            YES, field="hypertensive", field_applicable="hypertensive_on_meds"
        )
        self.required_if(
            YES, field="hypertensive", field_required="hypertensive_missed_doses"
        )
        self.validate_other_specify(field="employment")
        self.validate_other_specify(field="health_insurance")
        self.required_if(
            YES, field="know_other_symptoms", field_required="symptoms_other"
        )