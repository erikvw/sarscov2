from copy import copy
from django.conf import settings
from django.contrib import admin
from django.urls import reverse
from django_audit_fields import AUDIT_MODEL_FIELDS
from django_audit_fields import ModelAdminAuditFieldsMixin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_dashboard import url_names
from edc_form_label import FormLabelModelAdminMixin
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminInstitutionMixin,
    SimpleHistoryAdmin,
    TemplatesModelAdminMixin,
)
from edc_model_admin.base_model_admin_redirect_mixin import BaseModelAdminRedirectMixin
from import_export.admin import ExportActionMixin

from ..admin_site import sarscov2_admin
from ..forms import CoronavirusKapForm
from ..models import CoronavirusKap
from .modeladmin_mixin import CoronaKapModelAdminMixin

audit_fields = copy(AUDIT_MODEL_FIELDS)
audit_fields.remove("id")


@admin.register(CoronavirusKap, site=sarscov2_admin)
class CoronavirusKapAdmin(
    ExportActionMixin,
    TemplatesModelAdminMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminRevisionMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminInstitutionMixin,
    CoronaKapModelAdminMixin,
    FormLabelModelAdminMixin,
    BaseModelAdminRedirectMixin,
    SimpleHistoryAdmin,
):
    form = CoronavirusKapForm

    show_object_tools = True

    redirect_url_name = getattr(settings, "SARSCOV2_REDIRECT_URL_NAME", None)

    list_filter = ("crf_status", "report_datetime", *audit_fields)

    # add_form_template = "admin/change_form.html"
    # change_form_template = "admin/change_form.html"
    # change_list_template = "admin/change_list.html"

    def redirect_url(self, request, obj, post_url_continue=None):
        if self.redirect_url_name:
            redirect_url = url_names.get(self.redirect_url_name)
            return reverse(redirect_url)
        return None
