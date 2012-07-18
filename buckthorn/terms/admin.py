from django.contrib import admin
from django.forms import ModelForm

from terms.models import Term

class TermAdminForm(ModelForm):
    class Meta:
        model = Term

class TermAdmin(admin.ModelAdmin):
    form = TermAdminForm

admin.site.register(Term,TermAdmin)