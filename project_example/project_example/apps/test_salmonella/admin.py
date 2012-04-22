from django.contrib import admin

from salmonella.admin import SalmonellaMixin

from .models import SalmonellaTest


class SalmonellaTestAdmin(SalmonellaMixin, admin.ModelAdmin):
    raw_id_fields = ('rawid_fk', 'rawid_fk_limited', 'rawid_many')
    salmonella_fields = ('salmonella_fk', 'salmonella_fk_limited', 'salmonella_many')


admin.site.register(SalmonellaTest, SalmonellaTestAdmin)
