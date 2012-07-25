from django.contrib import admin

from core.models import Michaelmas, Year, Hilary, Trinity, Student, Lecturer, LectureSeries, Course, Module

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
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(LectureSeries)
admin.site.register(Course)
admin.site.register(Module)