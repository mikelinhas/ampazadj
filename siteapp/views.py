from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


from .models import Company


links = ["Home",
		 "Nav1",
		 "Nav2"]

def index(request):

	return redirect('home')


def home(request):

	companies = list(Company.objects.all())
	template = loader.get_template('siteapp/home.html')
	context = {'links': links, 
				'active_link': "Home",
				'companies': companies}
	return HttpResponse(template.render(context, request))


def company(request, company_id):

	company = Company.objects.get(id=company_id)
	template = loader.get_template('siteapp/company.html')
	context = {'links': links, 
				'active_link': "Home",
				'company': company}
	return HttpResponse(template.render(context, request))


def financial_report(request, company_id, fr_id):

	company = Company.objects.get(id=company_id)
	template = loader.get_template('siteapp/financial_report.html')
	context = {'links': links, 
				'active_link': "Home",
				'company': company,
				}
	return HttpResponse(template.render(context, request))




def nav1(request):

	template = loader.get_template('siteapp/nav1.html')
	context = {'links': links, 'active_link': "Nav1"}
	return HttpResponse(template.render(context, request))	



def nav2(request):

	template = loader.get_template('siteapp/nav2.html')
	context = {'links': links, 'active_link': "Nav2"}
	return HttpResponse(template.render(context, request))	