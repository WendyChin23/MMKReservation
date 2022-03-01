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

class Portfolio(View):
    def get(self, request):
        return render(request,'portfolio-details.html')        

class Signup(View):
    def get(self, request):
        return render(request,'signup.html')

class Login(View):
    def get(self, request):
        return render(request,'members.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            check_user = Account.objects.filter(username=username, password=password)
            check_admin = Admin.objects.filter(username='admin', password='admin')

            if check_user:
                request.session['usern'] = username
                if Account.objects.filter(username=username).count()>0: 
                        return redirect('mmkreservation:clientdashboard_view')

            if check_admin:
                request.session['admin'] = username
                if Admin.objects.filter(username=username).count()>0:    
                    return redirect('mmkreservation:accountdashboard_view')
            
            else:   
                return HttpResponse('not valid')
        else:   
            return render(request,"signup.html")