from django.contrib import admin
from .models import (
    Institute,
    Administrator,
)


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    pass
