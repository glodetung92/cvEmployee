from django.shortcuts import render
from .models import Employee, Profile, projects, Education
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer, ProfileSerializer
from django.contrib import messages

# Show list all employees 
class EmployeeList(ListView):
	model = Employee
	template_name = 'employee/list_employee.html'
	context_object_name = 'Employees'
	paginate_by = 5

# Show employee detail
class EmployeeDetail(DetailView):
	model = Employee

	template_name = 'employee/detail_employee.html'

	def get(self, request,*args, **kwargs):
		emp = get_object_or_404(Employee, pk=kwargs['pk'])
		context = { 'emp': emp }
		return render(request, 'employee/detail_employee.html', context)


# Add new employee
class EmployeeCreate(CreateView):
	model = Employee
	fields = "__all__"
	template_name = 'employee/employee_form.html'

	def get_success_url(self):
		return reverse('employee:employee_list')

# Show profile of employee
class ProfileEmployee(DetailView):
	model = Profile
	template = 'employee/profile_employee.html'

	def get(self, request, *args, **kwargs):
		try:
			profile = Profile.objects.get(emp__pk=kwargs['pk'])
			context = { 'profile': profile }
			return render(request, 'employee/profile_employee.html', context)
		except ObjectDoesNotExist:
			return HttpResponseNotFound('<h1 style="color:red">Page not found</h1><h4>This employee has no profile yet</h4>')


# Delete employee
class EmployeeRemove(DeleteView):
	model = Employee
	success_url = reverse_lazy('employee:employee_list')


# Update employee
class EmployeeUpdate(UpdateView):
	model = Employee
	fields = "__all__"

	template_name_suffix = '_update_form'

	def get_success_url(self):
		return reverse('employee:employee_list')

# Show education of employee
class EducationEmployee(DetailView):
	model = Education
	template = 'employee/education.html'

	def get(self, request, *args, **kwargs):
		education = Education.objects.filter(emp__pk=kwargs['pk'])
		if education.count() > 0:
			context = { 'education': education }
			return render(request, 'employee/education.html', context)
		else:
			return HttpResponseNotFound('<h1 style="color:red">Page not found</h1><h4>This employee has no profile yet</h4>')


# Show project of employee
class ProjectEmployee(DetailView):
	model = projects
	template = 'employee/project.html'

	def get(self, request, *args, **kwargs):
		project = projects.objects.filter(emp__pk=kwargs['pk'])
		if project.count() > 0:
			context = {'project': project}
			return render (request, 'employee/project.html', context)
		else:
			return HttpResponseNotFound('<h1 style="color:red">Page not found</h1><h4>This employee has no profile yet</h4>')

class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

	def get_permissions(self):
		if self.action == 'list':
			return [permissions.AllowAny()]

		return [permissions.IsAuthenticated()]

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permissions = [permissions.IsAuthenticated()]


