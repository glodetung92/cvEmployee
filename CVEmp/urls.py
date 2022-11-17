from django.urls import path
from .views import EmployeeList, EmployeeCreate, EmployeeDetail, ProfileEmployee, EmployeeRemove, EmployeeUpdate,EducationEmployee, ProjectEmployee

app_name = 'employee'

urlpatterns = [
	# Employee
	path('', EmployeeList.as_view(), name="employee_list"),
	path('create/', EmployeeCreate.as_view(), name="employee_create"),
	path('<int:pk>', EmployeeDetail.as_view(), name="employee_detail"),
	path('delete/<int:pk>', EmployeeRemove.as_view(), name="employee_remove"),
	path('update/<int:pk>', EmployeeUpdate.as_view(), name="employee_update"),

	#Profile
	path('profile/<int:pk>', ProfileEmployee.as_view(), name="employee_profile"),


	# Project
	path('project/<int:pk>', ProjectEmployee.as_view(), name="employee_project"),


	#Education
	path('education/<int:pk>', EducationEmployee.as_view(), name="employee_education"),
]
