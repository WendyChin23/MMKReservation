from django.urls import path
from . import views

app_name = 'mmkreservation'

urlpatterns= [
	
	path('Home', views.Home.as_view(), name="Home_view"),
	path('portfolio', views.Portfolio.as_view(), name="portfolio_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('login', views.Login.as_view(), name="login_view"),
	path('adminpage', views.AdminPage.as_view(), name="admin_view"),
	path('adminrooms', views.AdminRooms.as_view(), name="adminroom_view"),
	path('rooms', views.Rooms.as_view(), name="rooms_view"),

	path('adminaccounts', views.AdminAccountsDashboard.as_view(), name="adminaccounts_view"),

	
]