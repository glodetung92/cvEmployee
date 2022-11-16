from django.contrib import admin
from .models import Employee, Profile, projects, Education

# Register your models here.
admin.site.register(Employee)
admin.site.register(Profile)
admin.site.register(projects)
admin.site.register(Education)
