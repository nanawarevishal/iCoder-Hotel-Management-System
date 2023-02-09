
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Myfood,BookTable,Profile,contact,Order
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
import uuid
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def index(request):

    if Myfood.objects.filter(food_type__icontains='Starter'):
        
        allfood = Myfood.objects.filter(food_type__icontains='Starter')
        # print(allfood)
        
    if Myfood.objects.filter(food_type__icontains='Breakfast'):
       
        bffood = Myfood.objects.filter(food_type__icontains='Breakfast')
        # print(bffood)

    context = {'allfood':allfood}      
    return render(request,'index.html',context)

def booktable(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        no_of_people = request.POST['people']
        msg = request.POST['message']

        # checking if same days having same entries at same time

        if BookTable.objects.filter(date__icontains=date) and BookTable.objects.filter(time__icontains=time):
            messages.error(request,"Sorry...! It is booked by someone earlier try another...!")
            return render(request,'index.html') 

        else:

            myTable = BookTable(name =name,email=email,phone = phone,date =date,time=time,no_of_people=no_of_people,msg=msg)
            myTable.save()
            messages.success(request,"Congratulation your table has been booked successfully")
            return render(request,'index.html') 

    else:
        print('get')
        return HttpResponse('not found')


def food(request):
   
    return render(request,'index.html')


def contactus(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']

        mycontact = contact(name =name,email = email,subject=subject,msg = msg)
        mycontact.save()
        messages.success(request,"Your feedback has been sent successfully...!")
        return render(request,'index.html') 
        

def onlinefood(request):

    if Myfood.objects.filter(food_type__icontains='Starter'):
        
        allfood = Myfood.objects.filter(food_type__icontains='Starter')
        # print(allfood)
        
    if Myfood.objects.filter(food_type__icontains='Breakfast'):
       
        bffood = Myfood.objects.filter(food_type__icontains='Breakfast')
        # print(bffood)

    context = {'allfood':allfood}      
    return render(request,'onlinefood.html',context)

def handlesignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input

        try:

            if User.objects.filter(username = username).first():
                messages.warning(request,"Username is already taken......!")
                return redirect('onlinefood')
            
            if User.objects.filter(email = email).first():
                messages.warning(request,"Email is already taken......!")
                return redirect('onlinefood')

            if  not username.isalnum():
                messages.warning(request, " Username must be characters and numbers only")
                return redirect('onlinefood')

            if len(username) > 10 :
                messages.warning(request, " Username should must be 10 characters only")
                return redirect('onlinefood')

            if pass1 != pass2:
                messages.warning(request, " password didn't match")
                return redirect('onlinefood')
        
            # Create the user
            user_obj = User.objects.create(username=username, email=email)
            user_obj.first_name= fname
            user_obj.last_name= lname
            user_obj.set_password(pass1)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            print(auth_token)

            profile_obj = Profile.objects.create(user = user_obj,auth_token=auth_token)
            profile_obj.save()

            print(profile_obj)

            sendEmail(email,auth_token)
            messages.success(request, "Please check user email for verification....!")

            
            return redirect('onlinefood')

        except Exception as e:
            print(e)
            return redirect('onlinefood')

def loginuser(request):

    if request.method =="POST":
        username = request.POST['username']
        userpass = request.POST['pass']

        user_obj = User.objects.filter(username = username).first()

        if user_obj is None:
            messages.warning(request,"Sorry ...! User not found...!")
            return redirect('onlinefood')

        profile_obj = Profile.objects.filter(user = user_obj).first()

        if  not profile_obj.is_verified:
            messages.warning(request,"Please check your email and Verify your profile......!")
            return redirect('onlinefood')

        myuser = authenticate(username=username,password=userpass)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"You are successfully login...!")
            return redirect('onlinefood')

        else:
             messages.warning(request,"invalid credential ...! Enter correct credentials..!")
             return redirect('onlinefood')

    else:
        return render(request,'onlinefood.html')


def logoutuser(request):
    logout(request)
    messages.success(request,"You are successfully logout...!")
    return redirect('onlinefood')

def orderfood(request,order_id):
    if order_id:
        order = Myfood.objects.get(food_id= order_id)
        # print(order)
        orderdetails = Myfood.objects.filter(food_type = order)
        # print(orderdetails)

        for i in orderdetails:
            food_type=i.food_type
            food_title=i.food_title
            food_price=i.food_price
            food_desc=i.food_desc
            
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        no_ofDish = request.POST['no_ofDish']
        msg = request.POST['message']

        
        myorder = Order(name = name,email=email,phone=phone,address=address,food_type=food_type,food_title=food_title,food_price=food_price,food_desc=food_desc, no_ofDish=no_ofDish,msg =msg)
        myorder.save()
        messages.success(request,"Your Order placed successfully...!")
        return redirect('onlinefood')
            
    
    if Myfood.objects.filter(food_type__icontains='Starter'):
        
        allfood = Myfood.objects.filter(food_type__icontains='Starter')
        # print(allfood)

    context = {'allfood':allfood,'orderdetails':orderdetails}      
    return render(request,'orderfood.html',context)

def order(request):
     if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        no_ofDish = request.POST['no_ofDish']
        msg = request.POST['message']

        
        myorder = Order(name = name,email=email,phone=phone,address=address,no_ofDish=no_ofDish,msg =msg)
        myorder.save()
        messages.success(request,"Your Order placed successfully...!")
        return redirect('onlinefood')
        
def sendEmail(email, token):
    subject = "Your account need to be verified"
    msg = f"Click here http://127.0.0.1:8000/verify/{token}"

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,msg,email_from,recipient_list)


def verify(request,auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj.is_verified:
            messages.success(request,"Your profile is already verified....!")
            return redirect('onlinefood')

        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request,"Congratulations Your iCoder-food account has been verified....!")
        return redirect('onlinefood')

    except Exception as e:
        print(e)
        return redirect('onlinefood')