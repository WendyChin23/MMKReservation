from django.urls import path
from . import views

app_name = 'mmkreservation'

urlpatterns= [
	
	path('Home', views.Home.as_view(), name="Home_view"),

	
]