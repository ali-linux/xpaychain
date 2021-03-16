from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Transactions,Requsest
from django import forms
from django.forms import ValidationError

UserAdmin.list_display = ('id','username','first_name','last_name','amount','phone','email','main_image','subscribed','plan','transaction_url','schedul_pay')
# UserAdmin.fields = ('username','first_name','last_name','phone','email')
# UserAdmin.list_display_links = ('trans',)

UserAdmin.list_filter            += ('subscribed',)
# when you add new user 
UserAdmin.add_fieldsets +=((None,{'fields':('email','phone','first_name','last_name')}),)

# when you want to edit user fields
UserAdmin.fieldsets +=((None,{'fields':('phone','main_image','plan','amount','is_invester','trans'
)}),)



# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transactions
#         fields = ('transaction_amount',)

#     def clean(self):
#         ts_amount = self.cleaned_data.get('transaction_amount')
#         if ts_amount > 0:
#             raise forms.ValidationError("big dick boyyy")
#         return self.cleaned_data

class TransactionsAdmin(admin.ModelAdmin):
    # form = TransactionForm
    list_display = ['username','transaction_type','transaction_amount','transaction_date','acc_balance','transaction_complete','user','balance']

    fieldsets = ((None,{'fields':('user','transaction_type','transaction_amount')}),)

    
# class TradesAdmin(admin.ModelAdmin):
#     list_display = ['user','symbol','lot_size']
#     fieldsets = ((None,{'fields':('user','symbol','lot_size','trade_price')}),)


class RequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'trans_type','requested_amount','account_balance','phone','read','date']
    list_editable = ('read',)

admin.site.register(Transactions,TransactionsAdmin)
admin.site.register(User, UserAdmin)
# admin.site.register(Trades,TradesAdmin)
admin.site.register(Requsest,RequestAdmin)
