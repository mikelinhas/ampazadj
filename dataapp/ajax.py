from django.http import HttpResponse
from django.http import JsonResponse

from siteapp.models import Company

import http.client
import json

import os
import dotenv 

# .env:
dotenv.load_dotenv()

# DEFAULT IS DEV
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

api_url = API_URL

def getallcompanies(request):
	companies = list(Company.objects.all().values())
	return JsonResponse(companies, safe=False)


def getcompanyinfo(request):
	company = list(Company.objects.all().values())[0]
	return JsonResponse(company)


def getcompanyfinancial(request, company_id):
	company = Company.objects.get(id=company_id)
	conn = http.client.HTTPSConnection(api_url)
	conn.request("GET", "/stock/v2/get-financials?symbol=" + company.api_key, headers=headers)
	res = conn.getresponse()
	data = res.read()
	financials = json.loads(data.decode("utf-8"))
	return JsonResponse({"financialinfo": financials})


def getcompanysummary(request, company_id):
	company = Company.objects.get(id=company_id)
	conn = http.client.HTTPSConnection(api_url)
	conn.request("GET", "/stock/v2/get-summary?region=US&symbol=" + company.api_key, headers=headers)
	res = conn.getresponse()
	data = res.read()
	summary = json.loads(data.decode("utf-8"))
	return JsonResponse(summary)


