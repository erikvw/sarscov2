from copy import copy

from django.contrib import admin
from django_audit_fields import ModelAdminAuditFieldsMixin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_form_label import FormLabelModelAdminMixin
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminInstitutionMixin,
    SimpleHistoryAdmin,
    TemplatesModelAdminMixin,
)
from edc_model_admin.base_model_admin_redirect_mixin import BaseModelAdminRedirectMixin

from django.urls import reverse
from import_export.admin import ExportActionMixin
from django_audit_fields import AUDIT_MODEL_FIELDS

from ..admin_site import sarscov2_admin
from ..forms import CoronaKapForm
from ..models import CoronaKap
from .modeladmin_mixin import CoronaKapModelAdminMixin

audit_fields = copy(AUDIT_MODEL_FIELDS)
audit_fields.remove("id")


@admin.register(CoronaKap, site=sarscov2_admin)
class CoronaKapAdmin(
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
    form = CoronaKapForm

    show_object_tools = True

    redirect_url_name = None  # "sarscov2_admin:index"

    list_filter = ("crf_status", "report_datetime", *audit_fields)

    # add_form_template = "admin/change_form.html"
    # change_form_template = "admin/change_form.html"
    # change_list_template = "admin/change_list.html"

    def redirect_url(self, request, obj, post_url_continue=None):
        if self.redirect_url_name:
            return reverse(self.redirect_url_name)
        return None
