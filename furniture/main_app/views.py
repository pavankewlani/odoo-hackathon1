from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from main_app.forms import LoginForm, Usersignupform, usercart_table
from django.contrib import messages
from datetime import datetime

from main_app.models import cart_table
# Create your views here.


def home_page(request):
    return render(request,'index.html')

def login_page(request):
    context={}
    form=LoginForm

    #if request.user.is_authenticated:
    #    return redirect("login_page")
    

    if(request.method=="POST"):

        data=request.POST
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        print(user)
        print("username",username,"password",password)
        if user:
            login(request,user)
            return redirect("home_page")
        
        else:
            print("error")

    context["form"]=form
    return render(request,'login.html',context)

def signup_page(request):

    context={}
    form = Usersignupform()

    if (request.method == 'POST'):  

        form=Usersignupform(request.POST)
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Account created successfully')  

            return redirect("login_page")
        else:  
            print("error")

    context["form"]=form

    return render(request,'signup.html',context)


def bedroom_page(request):
    return render(request,"bedroom.html")

def dining_page(request):

    return render(request,'diningtable.html')

def sofa_page(request):

    return render(request,'sofa.html')


def cart_page(request):


    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost

    from_date = "2023-07-1"
    end_date = "2023-07-15"
    daily_rate = 500

    days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
    print(f"Number of days: {days}")
    print(f"Total cost: ₹{cost}")

    context={}
    print(context)
    form=cart_table(id=2,user="admin",starting_date=from_date,ending_date=end_date,name="xyz",rate=daily_rate,Total_price=cost)

    print(form)
    form.save()
    print("done")

    return render(request,'cart.html')


def bed1_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'bed1.html')



def dine1_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'din1.html')

def dine2_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'dine2.html')


def dine3_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'dine3.html')



def dine4_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'dine4.html')


def dine5_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'dine5.html')


def dine6_page(request):
    def calculate_rental_cost(from_date_str, end_date_str, daily_rate):
    
        from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        
        
        delta = end_date - from_date
        number_of_days = (delta.days)+1
        
        total_cost = (number_of_days) * daily_rate
        
        return number_of_days, total_cost
    
    if(request.method=="POST"):

        data=request.POST
        #itemname = request.POST['name']
        from_date = request.POST['from']
        end_date = request.POST['until']
        daily_rate = 500
        days, cost = calculate_rental_cost(from_date, end_date, daily_rate)
        print(f"Number of days: {days}")
        print(f"Total cost: ₹{cost}")

        #form=cart_table(id=1,user="admin",starting_date=from_date,ending_date=end_date,name=itemname,rate=daily_rate,Total_price=cost)
        #print(form)
        #form.save()
        print("done")
    return render(request,'dine6.html')
