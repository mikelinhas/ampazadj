from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import Company

from django.contrib.auth.models import Group


admin.site.site_header = "Ampaza Admin Site"
admin.site.site_title = "AMPAZA"


class CompanyResource(resources.ModelResource):
	class Meta:
		model = Company

class CompanyAdmin(ImportExportModelAdmin):
	resource_class = CompanyResource

admin.site.register(Company, CompanyAdmin)
admin.site.unregister(Group)


