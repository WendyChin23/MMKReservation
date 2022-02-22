from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import(get_object_or_404,render,HttpResponseRedirect)
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request,'index.html')