from django.contrib import admin
from ATES import models

class EvaluationPostAdmin(admin.ModelAdmin):
    list_display = ('timestamp','teacherevaluation')

admin.site.register(models.EvaluationPost,EvaluationPostAdmin)
admin.site.register(models.TeacherInformationPost)

