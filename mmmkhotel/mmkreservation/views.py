from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import(get_object_or_404,render,HttpResponseRedirect)
from django.core.mail import send_mail, BadHeaderError
from mmkreservation.forms import AccountForm, RoomForm

from mmkreservation.models import Account, Admin, Rooms


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request,'success.html')

class Success(View):
    def get(self, request):
        return render(request,'index.html')



class Portfolio(View):
    def get(self, request):
        return render(request,'portfolio-details.html')        

class Signup(View):
    def get(self, request):
        return render(request,'signup.html')

class Roomss(View):
    def get(self, request):
        return render(request,'rooms.html')




class AdminPage(View):
    def get(self, request):
        return render(request,'adminpage.html')     

class AdminRooms(View):
    def get(self, request):
        return render(request,'adminrooms.html')    

class Login(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            check_user = Account.objects.filter(username=username, password=password)
            check_admin = Admin.objects.filter(username='admin', password='admin')

            if check_user:
                request.session['usern'] = username
                if Account.objects.filter(username=username).count()>0: 
                        return redirect('mmkreservation:adminaccounts_view')

            if check_admin:
                request.session['admin'] = username
                if Admin.objects.filter(username=username).count()>0:    
                    return redirect('mmkreservation:adminaccounts_view')
            
            else:   
                return HttpResponse('not valid')
        else:   

            return render(request,"signup.html")  



class AdminAccountsDashboard(View):
    def get(self, request):
        if 'admin' in request.session:
            current_admin = request.session['admin']
            accountadmin = Admin.objects.filter(username=current_admin) 
            user = Account.objects.all()
       
        context = {

            'user' : user,
            'accountadmin':accountadmin, #name that we want to use
            
        }
        return render(request,'adminaccounts.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'BtnUpdate' in request.POST:
                print('update button clicked')
                Idn = request.POST.get("uid-uid")                                                                                                                                                                                                                                                                                                                                            
                firstname = request.POST.get("first-name")
                lastname = request.POST.get("last-name")
                Email = request.POST.get("email-email")             
                Address = request.POST.get("address-address")
                Age = request.POST.get("age-age")
                Username = request.POST.get("user-name")
                Password = request.POST.get("pass-word")
                
                update_user = Account.objects.filter(uid=Idn).update(first_name = firstname, last_name = lastname, address = Address,
                email = Email, age = Age, username = Username, password = Password )
                print(update_user)
                print('user updated')

            elif 'BtnDelete' in request.POST:
                print('delete button clicked')
                Idn = request.POST.get("iidn-idn")
                accounts = Account.objects.filter(uid=Idn).delete()


        return redirect('mmkreservation:adminaccounts_view')


class AccountView(View):
    def get(self, request):
        return render(request, 'adminaccounts.html')                      
    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            fname = request.POST.get("first_name")
            Uid = request.POST.get("uid")            
            lname = request.POST.get("last_name")
            Email = request.POST.get("email")
            Address = request.POST.get("address")
            Age = request.POST.get("age")
            Username = request.POST.get("username")
            Password = request.POST.get("password")
            form = Account(uid = Uid, first_name = fname, last_name = lname, email = Email, address = Address, age = Age,
             username = Username, password=Password)
            print('clicked')
            form.save() 

            return redirect('mmkreservation:adminaccounts_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')








class Signup(View):
  

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):        
        form = AccountForm(request.POST)        
        # fname = request.POST.get("firstname")
        # print(fname)
        # lname = request.POST.get("lastname")
        # print(lname)
        if form.is_valid():
            # try:
            fname = request.POST.get("first_name")
            Uid = request.POST.get("uid")            
            lname = request.POST.get("last_name")
            Email = request.POST.get("email")
            Address = request.POST.get("address")
            Age = request.POST.get("age")

            Username = request.POST.get("username")
            Password = request.POST.get("password")
            form = Account(uid = Uid, first_name = fname, last_name = lname, email = Email, address = Address, age = Age,
             username = Username, password=Password)
            print('clicked')
            form.save() 

            #return HttpResponse('Student record saved!')           
            return redirect('mmkreservation:login_view')
            # except:
            #   raise Http404
        else:
            print(form.errors)
            return HttpResponse('not valid')  





class Roomss(View):
  

    def get(self, request):
        return render(request, 'rooms.html')

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            Rid = request.POST.get("rid")
            Roomtype = request.POST.get("roomtype")            
            Date = request.POST.get("date")
            Email = request.POST.get("email")
            Day = request.POST.get("day")
            form = Rooms(rid = Rid, roomtype = Roomtype, date = Date, email = Email, day = Day,)
            print('clicked')
            form.save() 


            return redirect('mmkreservation:adminroom_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')






class AdminRoomsDashboard(View):
    def get(self, request):
        if 'admin' in request.session:
            current_admin = request.session['admin']
            accountadmin = Admin.objects.filter(username=current_admin) 
            roomsss = Rooms.objects.all()
       
        context = {
            'roomsss' : roomsss,
            'accountadmin':accountadmin, #name that we want to use
            
        }
        return render(request,'adminaccounts.html', context)

    def post(self, request):
        if request.method == 'POST':
            if 'BtnUpdate' in request.POST:
                print('update button clicked')
                Idn = request.POST.get("rid-rid")                                                                                                                                                                                                                                                                                                                                            
                Roomtype = request.POST.get("roomtype")
                Date = request.POST.get("date-date")
                Email = request.POST.get("email-email")             
                Day = request.POST.get("day-day")
             
                update_rooms = Rooms.objects.filter(rid=Idn).update(roomtype = Roomtype, date = Date, day = Day,
                email = Email)
                print(update_rooms)
                print('user updated')

            elif 'BtnDelete' in request.POST:
                print('delete button clicked')
                Idn = request.POST.get("iidn-idn")
                room = Rooms.objects.filter(rid=Idn).delete()


        return redirect('mmkreservation:adminroom_view')
