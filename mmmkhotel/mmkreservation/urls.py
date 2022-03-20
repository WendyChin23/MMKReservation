from django.urls import path
from . import views

app_name = 'mmkreservation'

urlpatterns= [
	
	path('Home', views.Home.as_view(), name="Home_view"),
	path('rates', views.Rates.as_view(), name="rates_view"),
	path('portfolio', views.Portfolio.as_view(), name="portfolio_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('login', views.Login.as_view(), name="login_view"),
	path('adminpage', views.AdminPage.as_view(), name="admin_view"),
	path('adminrooms', views.AdminRoomsDashboard.as_view(), name="adminroom_view"),
	path('adminpayment', views.AdminPaymentDashboard.as_view(), name="adminpayment_view"),

	path('rooms', views.RoomAdd.as_view(), name="rooms_view"),
	path('rooms/<conferenceId>/', views.RoomAdd.as_view(), name="rooms_view"),
	path('payment', views.PaymentPage.as_view(), name="payment_view"),

##Rooms add from user to admin
	path('adminaccounts', views.AdminAccountsDashboard.as_view(), name="adminaccounts_view"),
	path('success', views.Success.as_view(), name="success_view"),
	
	##Rooms add from admin to user
	path('adminviewroom', views.AdminViewRoom.as_view(), name="adminviewroom_view"),
	##Dashboard
	path('userviewroom', views.UserViewRoom.as_view(), name="userviewroom_view"),

]
