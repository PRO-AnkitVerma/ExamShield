from django.contrib import admin

# Register your models here.
from subject.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
