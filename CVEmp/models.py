from django.db import models

# Create your models here.
class Employee(models.Model):
	emp_name = models.CharField(max_length=100, unique=True)
	emp_code = models.CharField(max_length=50, unique=True)
	emp_position = models.CharField(max_length=255)

	class Meta:
		ordering = ('emp_name', 'emp_code')

	def __str__(self):
		return self.emp_name

class Profile(models.Model):
	address = models.CharField(max_length=500)
	phone = models.CharField(max_length=12)
	email = models.EmailField(max_length=100)
	birth = models.DateField()
	skills = models.CharField(max_length=500, blank=True, null=True)

	emp = models.ForeignKey(Employee, related_name="employee", on_delete=models.CASCADE)

	def __str__(self):
		return self.email


class projects(models.Model):
	project_name = models.CharField(max_length=500)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	emp = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Education(models.Model):
	edu_name = models.CharField(max_length=255)
	period = models.CharField(max_length=255)

	emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
