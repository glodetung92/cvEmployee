from django.contrib import admin
from .models import Employee, Profile, projects, Education


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ("emp_name", "emp_code", "emp_position")


class ProfileAdmin(admin.ModelAdmin):
	list_display = ("address", "phone", "email", "birth")


class EducationAdmin(admin.ModelAdmin):
	list_display = ("edu_name", "period")


class ProjectAdmin(admin.ModelAdmin):
	list_display = ("emp", "project_name", "created_date")



# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(projects, ProjectAdmin)
admin.site.register(Education, EducationAdmin)
