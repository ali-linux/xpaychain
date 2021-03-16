from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages,auth
from .models import User,Transactions,Requsest
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.contrib.sites.shortcuts import get_current_site
# from .models import password_reset
import secrets
from datetime import datetime,date
from django.utils import timezone
# from . import config_api
# from binance.client import Client
# from binance.enums import *

kurdDash = '/accounts/ku/dashboard'
arabDash = '/accounts/ar/dashboard'
kuLogin = '/accounts/ku/login'
arLogin = '/accounts/ar/login'
kuRegister = '/accounts/ku/register'
arRegister = '/accounts/ar/register'

def login(request):
    #CHECK IF THE SUBIMTED FORM IS A POST REQUEST NOT A GET REQUEST
    if request.user.is_authenticated:
        if('/ku' in request.path):
            return redirect('/ku')
        if('/ar' in request.path):
            return redirect('/ar')
        return redirect('index',)
    if request.method == 'POST':
        #STORE SUBMITED DATA INTO VARIBELS
        # username = request.POST['username-email']
        email = request.POST['email'].lower()
        password = request.POST['password']
        #CHECK IF USER CREDENTIALS VALID
        # user_name = auth.authenticate(request, username=username, password=password)
        user_email_check = User.objects.filter(email=email).exists()
        if user_email_check:
            user_valid = User.objects.get(email=email)
            user_1 = auth.authenticate(request, username = user_valid.username, password = password)
            if user_1 is not None:
                auth.login(request,user_1)
                messages.success(request,'logged in successfully')
                if('/ku' in request.path):
                    return redirect(kurdDash)
                elif('/ar' in request.path):
                    return redirect(arabDash)
                else:
                    return redirect('dashboard')
            else:
                if('/ku' in request.path):
                    messages.error(request,'‌‌هەلەیە ٧ برا')
                    return redirect(kuLogin)
                elif('/ar' in request.path):
                    return redirect(arLogin)
                else:
                    messages.error(request,'inavlid credentials')
                    return redirect('login')
        # if user_name  is not None :
        #     auth.login(request,user_name)
        #     messages.success(request,'logged in successfully')
        #     return redirect('dashboard')
        else:
            if('/ku' in request.path):
                messages.error(request,'‌‌هەلەیە ٧ برا')
                return redirect(kuLogin)
            elif('/ar' in request.path):
                return redirect(arLogin)
            else:
                messages.error(request,'inavlid credentials')
                return redirect('login')
    if('/ku' in request.path):
        return render(request, 'accounts/login_ku.html')
    elif('/ar' in request.path):
        return render(request, 'accounts/login_ar.html')
    return render(request,'accounts/login.html')


def register(request):
    #CHECK IF THE SUBIMTED FORM IS A POST REQUEST NOT A GET REQUEST
    if request.user.is_authenticated:
        if('/ku' in request.path):
            return redirect(kurdDash)
        elif('/ar' in request.path):
            return redirect(arabDash)
        else:
            return redirect('dashboard')
    if request.method == 'POST':
        #STORE SUBMITED DATA INTO VARIBELS
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tel = request.POST['tel']
        username = (first_name+tel).lower()
        email = request.POST['email'].lower()
        password = request.POST['password']
        password2 = request.POST['password2']
        pic_bool = False
        try:
            pic = request.FILES['picture']
            fs = FileSystemStorage()
            pic_file = fs.save(pic.name,pic)
            upload_file = fs.url(pic_file)
            pic_bool = True
        except :
            pass
        if password != password2:
            messages.error(request,'passwords dont match')
            if('/ku' in request.path):
                return redirect(kuRegister)

            if('/ar' in request.path):
                return redirect(arRegister)


            return redirect('register')
        else:
            if len(password2)  < 8:
                messages.error(request,'password must be minimum 8 characters')
                if('/ku' in request.path):
                    return redirect(kuRegister)

                elif('/ar' in request.path):
                    return redirect(arRegister)
                else:
                    return redirect('register')
            else:
                #check for duplicate emails
                user_email = User.objects.filter(email=email).exists()
                user_phone = User.objects.filter(phone = tel).exists()
                if user_email or user_phone:
                    messages.error(request,'user already exists with the email or phone number')
                    if('/ku' in request.path):
                        return redirect(kuRegister)

                    elif('/ar' in request.path):
                        return redirect(arRegister)
                    else:
                        return redirect('register')
                else:
                    #EVERYTHING IS VALID
                    trans = 'http://{0}/Transaction/{1}'.format(get_current_site(request),tel)
                    if pic_bool:
                        user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name, last_name=last_name,phone=tel,main_image=pic_file,trans = trans)
                        user.save()
                    else:
                        user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name, last_name=last_name,phone=tel,trans = trans)
                        user.save()
                    messages.success(request,'your account has been created successfuly, you can now login')
                    if('/ku' in request.path):
                        return redirect(kuLogin)

                    elif('/ar' in request.path):
                        return redirect(arLogin)
                    else:
                        return redirect('login')

    else:
        if('/ku' in request.path):
            return render(request, 'accounts/sign_up_ku.html')

        elif('/ar' in request.path):
            return render(request, 'accounts/sign_up_ar.html')
        else:
            return render(request,'accounts/sign_up.html')




# def password_reset_func(request):
#     if request.method == 'POST':
#         user_email = request.POST['email']
#         user_email_exst = User.objects.filter(email=user_email).exists()
#         if user_email_exst:
#             user_token = secrets.token_urlsafe(16)
#             send_mail('Password Reset','https://nwsinga.herokuapp.com/accounts/password/reset/done/{}'.format(user_token),
#             'ali.srwsht.ali@gmail.com',[user_email],fail_silently=False)
#             messages.success(request,'shortly you will recive an email with instructions to reset your password do not share that link with any one')
#             reset = password_reset(user_email=user_email,user_token=user_token)
#             reset.save()
#         else:
#             messages.error(request,"there is no user with that email")
#             return redirect('password_reset')
#     return render(request,'accounts/reset_password.html')

def time_t (obejt_str):
    date_ = obejt_str.split('-',2)
    #date_[0] == year, date_[1] == month
    date_day = date_[2].split() #date_day[0] == the day
    time_ = obejt_str.split(':')
    time_hour = time_[0].split()
    day = int(date_day[0])
    month = int(date_[1])
    year = int( date_[0])
    hour = int(time_hour[1])
    minute = int(time_[1])
    context = {'date':obejt_str,
                'day':day,'month':month,'year':year,
                'hour':hour, 'minute':minute, 'date':obejt_str
                }
    return context

# def password_reset_done(request,token):
#     user_token_rest = password_reset.objects.filter(user_token=token).exists()
#     if user_token_rest:
#         request_date = password_reset.objects.get(user_token=token)
#         time_request = time_t(str(request_date.date_request))
#         time_now = time_t(str(timezone.now()))
#         #datetime_object = datetime.strptime(request_date.date_request, "%d-%b-%Y  %H:%M:%S.%f")
#         if time_request['day'] == time_now['day'] and time_request['month'] == time_now['month'] and time_request['year'] == time_now['year']:
#             if time_request['hour'] == time_now['hour']:
#                 x = time_now['minute']-time_request['minute']
#                 if x < 5:
#                     if request.method == 'POST':
#                             password = request.POST['password1']
#                             password2 = request.POST['password2']
#                             if password != password2:
#                                 messages.error(request,'passwords dont match')
#                                 return redirect('password_reset_done',token)
#                             else:
#                                 user_info = password_reset.objects.get(user_token=token)
#                                 user_reset = User.objects.get(email=user_info.user_email)
#                                 user_reset.set_password(password)
#                                 user_reset.save()
#                                 messages.success(request,'password successfuly updated')
#                                 password_reset.objects.filter(user_token=token).delete()
#                                 return redirect('login')
#                 else:
#                     password_reset.objects.filter(user_token=token).delete()
#                     messages.error(request,'time expierd make a new request')
#                     return redirect('password_reset')
#     else:
#         messages.error(request,'invalid Token')
#         return redirect('index')
#     context = {'token':token}
#     return render(request,'accounts/password_reset_done.html', context)
    # token = str(tokenn)
    # print(token)
    # print(user_token_rest)
    # if request.method == 'POST':
    #     if user_token_rest:
    #         return redirect('about')
    #     if user_token_rest:
    #         print('heloooooooooooooooooooooooooooo')
# @login_required
def dashboard(request):
    if not request.user.is_authenticated:
        if('/ku' in request.path):
            return redirect('/ku')
        elif('/ar' in request.path):
            return redirect('/ar')
        else:
            return redirect('index')
    else:
        print(request.build_absolute_uri)
        basic = 0.07
        standard = 0.08
        others = 0.09
        plan= request.user.plan
        balance = request.user.amount
        year = request.user.schedul_pay.year
        month = request.user.schedul_pay.month
        year_now = date.today().year
        month_now = date.today().month
        if(year == year_now and balance > 0):
            if(month_now > month):
                if(plan == "basic"):
                    balance ="{:.2f}".format( balance + "{:.2f}".format(balance*basic) )
                    request.user.schedul_pay = datetime.now()
                elif(plan == "standard"):
                    balance ="{:.2f}".format( balance + "{:.2f}".format(balance*standard) )
                    request.user.schedul_pay = datetime.now()
                elif(plan == "gold" or plan == "diamond"):
                    request.user.amount =float( "{:.2f}".format( float(balance) + float("{:.2f}".format(float(balance)*others) )))
                    request.user.schedul_pay = datetime.now()
                    request.user.save()
        elif(year < year_now):
            if(plan == "basic"):
                balance ="{:.2f}".format( balance + "{:.2f}".format(balance*basic) )
                request.user.schedul_pay = datetime.now()
                request.user.amount = float(balance) 
            elif(plan == "standard"):
                balance ="{:.2f}".format( balance + "{:.2f}".format(balance*standard) )
                request.user.schedul_pay = datetime.now()
                request.user.amount = float(balance) 

            elif(plan == "gold" or plan == "diamond"):
                balance = "{:.2f}".format( float(balance) + float("{:.2f}".format(float(balance)*others) ))
                request.user.schedul_pay = datetime.now()
                request.user.amount = float(balance) 
        trans_query = Transactions.objects.filter(user=request.user)
        context = {"trans_query":trans_query,}
        if('/ku' in request.path):
            return render(request, 'accounts/user_dashboard_ku.html',context)
        elif('/ar' in request.path):
            return render(request, 'accounts/user_dashboard_ar.html',context)
        else:
            return render(request, 'accounts/user_dashboard.html',context)

@login_required
def logout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            auth.logout(request)
            if('/ku' in request.path):
                return redirect('/ku')
            elif('/ar' in request.path):
                return redirect('/ar')
            else:
                return redirect('index')
        else:
            if('/ku' in request.path):
                return redirect(kurdDash)
            elif('/ar' in request.path):
                return redirect(arabDash)
            else:
                return redirect('dashboard')
    else:
        if('/ku' in request.path):
            return redirect('/ku')
        elif('/ar' in request.path):
            return redirect('/ar')
        else:
            return redirect('index')

# @login_required
# def trading(request):
#     if request.user.is_authenticated:
#         if request.user.is_trader:
#             user_api__secret_key = request.user.api_secret
#             user_api_key =request.user.api_key
#             client = Client(user_api_key,user_api__secret_key)
#             info = client.get_account()
#             exchange_info = client.get_exchange_info()
#             symbols = exchange_info['symbols']        
#             balance = info['balances']
#             all_symbols = []
#             for symbol in symbols:
#                 all_symbols.append(symbol['symbol']) 
#             context = {'balance':balance, 'symbols':all_symbols, 'info':exchange_info}
#             return render(request,'accounts/trading.html',context)
#         else:
#             return redirect('dashboard')
#     else:
#         return redirect('login')

# @login_required
# def buy(request):
#         if request.user.is_authenticated:
#             if request.method == 'POST':
#                 client = Client(config_api.API_KEY,config_api.API_SECRET)
#                 symbol = request.POST['symbol']
#                 amount = request.POST['amount']
#                 order = client.create_test_order(
#                     symbol=symbol,
#                     side=SIDE_BUY,
#                     type=ORDER_TYPE_MARKET,
#                     quantity=amount)
#                 context = {'amount':amount, 'symbol':symbol, 'order':order}
#                 messages.success(request,'your order has been placed')
#                 amount = float(amount)
#                 trade = Trades(user=request.user,symbol=symbol,lot_size=amount)
#                 trade.save()
#                 return redirect('trading')
#             else:
#                 messages.error(request,'fuckkkkkk')
#                 return redirect('trading')
#         else:
#             messages.error(request,'trade was not succesful')
#             return redirect('login')

# @login_required
# def sell(request):
#         if request.user.is_authenticated:
#             pass
#         else:
#             return redirect('login')

@login_required
def withdrawl(request):
    u = request.user
    print( u.amount <= 0)
    if u.amount <= 0:
        messages.warning(request,"You are not subscribed you can't withdrawl")
        if('/ku' in request.path):
            return redirect(kurdDash)
        elif('/ar' in request.path):
            return redirect(arabDash)
        else:
            return redirect('dashboard')
    else:
        if request.method == 'POST' and request.user.is_authenticated:
            req_amount = float(request.POST['req']) 
            if req_amount > u.amount:
                messages.warning(request,"You can't withdrawl more than what you have")
                if('/ku' in request.path):
                    return redirect('/accounts/ku/withdrawl')
                elif('/ar' in request.path):
                    return redirect('/accounts/ar/withdrawl')
                else:
                    return redirect('withdrawl')
            else:
                r = Requsest(user = u, requested_amount = req_amount, phone = u.phone)
                r.save()
                messages.success(request,'Request has been sent successfully')
                if('/ku' in request.path):
                    return redirect(kurdDash)
                elif('/ar' in request.path):
                    return redirect(arabDash)
                else:
                    return redirect('dashboard')

        if('/ku' in request.path):
            return render(request, 'accounts/withdrawl_ku.html')
        elif('/ar' in request.path):
            return render(request, 'accounts/withdrawl_ar.html')
        else:
            return render(request,'accounts/withdrawl.html')
