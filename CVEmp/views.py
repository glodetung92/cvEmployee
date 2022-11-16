from django.shortcuts import render
from .models import Employee, Profile, projects, Education
from django.views.generic import ListView, CreateView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class EmployeeList(ListView):
	model = Employee
	template_name = 'employee/list_employee.html'
	context_object_name = 'Employees'
	paginate_by = 5


class EmployeeDetail(DetailView):
	model = Employee

	template_name = 'employee/detail_employee.html'

	def get(self, request,*args, **kwargs):
		emp = get_object_or_404(Employee, pk=kwargs['pk'])
		context = { 'emp': emp }
		return render(request, 'employee/detail_employee.html', context)


class EmployeeCreate(CreateView):
	model = Employee
	fields = "__all__"
	template_name = 'employee/employee_form.html'

	def get_success_url(self):
		return reverse('employee:employee_list')


class ProfileEmployee(DetailView):
	model = Profile
	template = 'employee/profile_employee.html'

	def get(self, request, *args, **kwargs):
		try:
			profile = Profile.objects.get(emp__pk=kwargs['pk'])
			context = { 'profile': profile }
			return render(request, 'employee/profile_employee.html', context)
		except ObjectDoesNotExist:
			return HttpResponseNotFound('<h1>Page not found</h1>')
