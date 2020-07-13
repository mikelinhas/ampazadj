from django.urls import path

from . import ajax

urlpatterns = [
    path('getallcompanies', ajax.getallcompanies, name='getallcompanies'),
    path('getcompanyinfo', ajax.getcompanyinfo, name='getcompanyinfo'),
    path('getcompanyfinancial/<int:company_id>', ajax.getcompanyfinancial, name='getcompanyfinancial'),
    path('getcompanysummary/<int:company_id>', ajax.getcompanysummary, name='getcompanysummary'),
]
