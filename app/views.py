from django.shortcuts import render
from app.models import BaseClass
from django.views.geneic import ListView, TemplateView, View 

# Create your views here.
class AboutMe(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello!!!")

class UsersListView(ListView):
	model = BaseClass
	template_name = "users_list.html"

class AboutApp(TemplateView):
	template_name = 'about_app.html'

	def get_context_data(self, **kwargs):
		context = super(AboutApp, self).get_context_data(**kwargs)
		context['last objects'] = BaseClass.objects.all()
		return context

