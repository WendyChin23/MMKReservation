from django import forms
#from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User
from django import forms
#from django.db.models import fields
from .models import *
from django.core.exceptions import ValidationError

# class ContactForm(forms.ModelForm):
# 	class Meta:
# 		model = ContactMessage
# 		fields= '__all__'

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields= ['email' , 'username']
		#fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2', 'address', 'age', 'birthdate')

class RoomForm(forms.ModelForm):
	class Meta:
		model = Rooms
		fields= '__all__'
		exclude = ('roomtype',)      

class PaymentForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields = '__all__'	

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = '__all__'
