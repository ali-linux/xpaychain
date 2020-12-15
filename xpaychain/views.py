from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User,Transactions

def user_transactions(request,tel):
    trans = Transactions.objects.all()
    u_phone = User.objects.get(phone=tel)
    trans_query = trans.filter(user=u_phone)
    context = {"trans_query":trans_query}
    return render(request,'custom.html',context)