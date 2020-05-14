from django import forms
from edc_form_validators import FormValidatorMixin
from edc_sites.forms import SiteModelFormMixin

from ..models import CoronaKap
from .coronavirus_kap_form_validator import CoronaKapFormValidator


class CoronaKapForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = CoronaKapFormValidator

    class Meta:
        model = CoronaKap
        fields = "__all__"
