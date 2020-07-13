from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('nav1', views.nav1, name='nav1'),
    path('nav2', views.nav2, name='nav1'),
    #path('company/<int:company_id>/', views.company),
    #path('company/<int:company_id>/<int:fr_id>/', views.financial_report),
]
