from django.contrib import admin

# Register your models here.
from faculty.models import faculty


@admin.register(faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass
