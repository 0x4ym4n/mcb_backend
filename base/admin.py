from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from base.models import *


class PageAdmin(ImportExportModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        self.search_fields = [field.name for field in model._meta.fields if field.name != "id"]
        self.skip_diff = True
        self.force_init_instance = True
        super(PageAdmin, self).__init__(model, admin_site)


