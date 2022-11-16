from django.urls import path
from .views import EmployeeList, EmployeeCreate, EmployeeDetail, ProfileEmployee

app_name = 'employee'

urlpatterns = [
	path('', EmployeeList.as_view(), name="employee_list"),
	path('create/', EmployeeCreate.as_view(), name="employee_create"),
	path('<int:pk>', EmployeeDetail.as_view(), name="employee_detail"),

	#----------------------------------------------------------
	path('profile/<int:pk>', ProfileEmployee.as_view(), name="employee_profile")
]
