from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from django.utils.html import format_html
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.forms import ValidationError


class User(AbstractUser):
    phone       = models.CharField(max_length=50,blank=True,)
    main_image  = models.ImageField(blank = True,null=True, default='default.jpg')
    no_plan     = 'Not subscribed'
    basic       = 'Basic'
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
    amount          = models.IntegerField(blank=True,null=True,default=0)
    # date_joined   = models.DateField(default = timezone.now, blank = True)
    date_joind      = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    trans =models.URLField(verbose_name='Transactions',max_length=250)
    subscribed = models.BooleanField(verbose_name='Subscribed',default=False)
    def transaction_url(self):
        return format_html(
            '<a href="{}">Transactions</a>',
            self.trans,)
    # trans_url.allow_tags = True

class Transactions(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    # phone = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    withdrawll  = 'withdrawll'
    deposit  = 'deposit'
    transaction_type_choices = [
        (withdrawll,'withdrawll'),
        (deposit,'deposit'),
    ]

    transaction_type = models.CharField(
        max_length=20, 
        choices=transaction_type_choices)

    transaction_amount = models.IntegerField(blank=True)
    transaction_date      = models.DateTimeField(verbose_name='Transaction Date',auto_now_add=True)
    # transaction_date = models.DateField(default=timezone.now,blank=True)
    transaction_complete = models.BooleanField(default=False)
    acc_balance = models.IntegerField(verbose_name='Account balance after that transaction',blank=True,null=True)
    def username(self):
        c_user = User.objects.get(username=self.user)
        if not self.transaction_complete:
            c_user.amount = c_user.amount+ self.transaction_amount
            c_user.save()
            self.transaction_complete = True
            self.acc_balance = c_user.amount
            self.save()
        
        return c_user
    def clean(self):
        if self.transaction_amount > 1 and self.transaction_type == 'withdrawll':
            raise ValidationError("withdrawll cant be positive value")
        if self.transaction_amount <= 0 and self.transaction_type == 'deposit':
            raise ValidationError("Deposit cant be Zero or negative value")
    
    


