from django.contrib import admin

from dates.models import Michaelmas, Year, Hilary, Trinity

class MichaelmasInline(admin.StackedInline):
    model = Michaelmas

class HilaryInline(admin.TabularInline):
    model = Hilary

class TrinityInline(admin.options.InlineModelAdmin):
    model = Trinity
    template = 'one_to_one.html'

class YearAdmin(admin.ModelAdmin):
    inlines = [
        MichaelmasInline,
        HilaryInline,
        TrinityInline,
    ]

admin.site.register(Year,YearAdmin)