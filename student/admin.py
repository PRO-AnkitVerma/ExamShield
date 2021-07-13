from django.contrib import admin

# Register your models here.
from student.models import student


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    pass
