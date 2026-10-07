from django.contrib import admin
from .models import Department, Program, Subject, Teacher, HomePage, ExchangeProgram

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department')

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'coordinator', 'coordinator_contacts')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'credits', 'semester')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'position', 'department')

class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university_name','country', 'languages', 'places', 'deadline', 'description')

# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(HomePage)
admin.site.register(ExchangeProgram, ExchangeProgramAdmin)
