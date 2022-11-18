from rest_framework.serializers import ModelSerializer
from .models import Employee, Profile


class EmployeeSerializer(ModelSerializer):
	class Meta:
		model = Employee
		fields = ['id', 'emp_name', 'emp_code', 'emp_position', 'emp_img']


class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile
		fields = ['address', 'phone', 'email', 'birth', 'skills']
