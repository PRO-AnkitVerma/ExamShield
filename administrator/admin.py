from django.contrib import admin
from .models import (
    Institute,
    Administrator, StudentInfo, FacultyInfo,
)


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass


@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    pass
@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    pass
