from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime,date
from django.utils import timezone
from django.utils.html import format_html
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.forms import ValidationError
from django.db.models.signals import post_save
from notifications.signals import notify
from notifications.models import Notification



class User(AbstractUser):

    phone       = models.CharField(max_length=50,blank=True,)
    main_image  = models.ImageField(blank = True,null=True, default='default.jpg')
    no_plan     = 'Not subscribed'
    basic       = 'basic'
    standard    = 'standard'
    gold        = 'gold'
    diamond     = 'diamond'
    plans       = [
        (no_plan, 'Not subscribed'),
        (basic, 'basic'),
        (standard, 'standard'),
        (gold, 'gold'),
        (diamond, 'diamond'),
    ]

    plan       = models.CharField(
        max_length=20,
        choices=plans,
        default=no_plan,
    )
    amount          = models.DecimalField(blank=True,null=True,default=0,verbose_name='Balance',max_digits=99999999,decimal_places=2)
    # date_joined   = models.DateField(default = timezone.now, blank = True)
    date_joind      = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    schedul_pay      = models.DateTimeField(verbose_name='Scheduled payment',auto_now_add=True, null=True)
    trans =models.URLField(verbose_name='Transactions',max_length=250)
    subscribed = models.BooleanField(verbose_name='Subscribed',default=False)
    def transaction_url(self):
        return format_html(
            '<a href="{}">Transactions</a>',
            self.trans,)
    # is_trader = models.BooleanField(default=False, verbose_name='Trader')
    is_invester = models.BooleanField(default=False, verbose_name='Invester')
    # api_key = models.CharField(max_length=255,blank=True)
    # api_secret = models.CharField(max_length=255,blank=True)
    # trans_url.allow_tags = True

    def save(self, *args, **kwargs):
        if(self.amount > 0):
            self.subscribed = True
            if(self.amount>=5000 and self.amount <10000):
                self.plan = "basic"
            elif(self.amount>=10000 and self.amount <20000):
                self.plan = "standard"
            elif(self.amount>=20000 and self.amount <50000):
                self.plan = "gold"
            elif(self.amount>=50000):
                self.plan = "diamond"
        super(User, self).save(*args, **kwargs)

        

class Transactions(models.Model):
    class Meta:
        verbose_name = ("Transaction")
        verbose_name_plural = ("Transactions")

    user                = models.ForeignKey(User,on_delete=models.CASCADE)
    # phone = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    withdrawll          = 'withdrawll'
    deposit             = 'deposit'
    transaction_type_choices = [
        (withdrawll,'withdrawll'),
        (deposit,'deposit'),
    ]

    transaction_type    = models.CharField(
        max_length=20, 
        choices=transaction_type_choices)

    transaction_amount  = models.DecimalField(blank = True,decimal_places=2,max_digits=9999999)
    transaction_date    = models.DateTimeField(verbose_name='Transaction Date',auto_now_add=True)
    transaction_complete = models.BooleanField(default=False)
    acc_balance         = models.DecimalField(verbose_name='Account balance after that transaction',blank=True,null=True,decimal_places = 2,max_digits=99999999)
    def username(self):
        c_user = User.objects.get(username=self.user)
        if not self.transaction_complete:
            c_user.amount = c_user.amount+ self.transaction_amount
            c_user.save()
            self.transaction_complete = True
            self.acc_balance = c_user.amount
            self.save()
        
        return c_user
    def balance(self):
        return self.user.amount        
        
    def clean(self):
        if self.transaction_amount > self.user.amount and self.transaction_type == 'withdrawll' :
            raise ValidationError("Can't withdrawll more than the account balance : {} ".format(self.user.amount))
        else:
            if self.transaction_amount > 1 and self.transaction_type == 'withdrawll' :
                raise ValidationError("withdrawll can't be positive value")
            if self.transaction_amount <= 0 and self.transaction_type == 'deposit':
                raise ValidationError("Deposit can't be Zero or negative value")
    def __str__(self):
        return str(self.user) +" "+ self.transaction_type

# class Trades(models.Model):
#     user            = models.ForeignKey(User,on_delete = models.CASCADE)
#     buy             = 'Long'
#     sell            = 'Short'
#     postion_types   = [
#         (buy,'Long'),
#         (sell,'Short')
#     ]
#     running         = 'Running'
#     closed         = 'Closed'
#     trade_statuss = [
#         (running, 'Running'),
#         (closed, 'Closed')
#         ]
#     postion         = models.CharField(max_length = 50,choices = postion_types,blank=True, null=True)
#     lot_size        = models.DecimalField(blank=True, null=True, verbose_name = 'Lot size',decimal_places=15,max_digits=100)
#     trade_price     = models.DecimalField(blank=True, null=True, verbose_name = "Trade Price",decimal_places=15,max_digits=100)
#     symbol          = models.CharField(max_length = 22)
#     trade_date      = models.DateTimeField(verbose_name = 'Date',auto_now_add = True)
#     trade_status    = models.CharField(max_length = 25,choices = trade_statuss,blank=True, null=True)
#     profit          = models.DecimalField(blank=True, null=True, verbose_name="Profit",decimal_places=2,max_digits=1000000)


class Requsest(models.Model):
    
    verbose_name = ("Reqasdasuest")
    verbose_name_plural = 'Requestsghgf'

    user            = models.ForeignKey(User,on_delete = models.CASCADE)
    trans_type      = models.CharField( verbose_name='Type' ,max_length=50,default = 'withdrawl')
    requested_amount= models.DecimalField(blank = True,decimal_places=2,max_digits=9999999)
    date            = models.DateTimeField(verbose_name='Request Date',auto_now_add=True)
    phone           = models.CharField(max_length=50,blank=True )
    read            = models.BooleanField(default = False)

    def account_balance(self):
        return self.user.amount
    def save(self, *args, **kwargs):
        if self.read == False:
            notify.send(self.user, recipient=User.objects.filter(is_superuser =True), verb='you reached level 10')
        if self.read == True:
            n = Notification.objects.filter(actor_object_id=self.user.id )
            n[0].delete()
        super(Requsest, self).save(*args, **kwargs)
    
