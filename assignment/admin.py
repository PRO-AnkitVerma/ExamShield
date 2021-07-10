from django.contrib import admin
from .models import Assignment, AssignmentInstance


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(AssignmentInstance)
class AssignmentInstanceAdmin(admin.ModelAdmin):
    pass
