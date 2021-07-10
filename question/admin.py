from django.contrib import admin

# Register your models here.
from question.models import Course, Question, Result


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Question)
class Questiondmin(admin.ModelAdmin):
    pass
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass
