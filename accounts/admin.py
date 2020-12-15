from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Transactions
from django import forms
from django.forms import ValidationError

UserAdmin.list_display = ('username','first_name','last_name','phone','email','main_image','subscribed','plan','transaction_url','amount')
# UserAdmin.fields = ('username','first_name','last_name','phone','email')
# UserAdmin.list_display_links = ('trans',)

UserAdmin.list_filter            += ('subscribed',)
# when you add new user 
UserAdmin.add_fieldsets +=((None,{'fields':('email','phone','first_name','last_name')}),)

# when you want to edit user fields
UserAdmin.fieldsets +=((None,{'fields':('phone','main_image','plan','amount'
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
    list_display = ['username','transaction_type','transaction_amount','transaction_date','acc_balance','transaction_complete','user']

    fieldsets = ((None,{'fields':('user','transaction_type','transaction_amount')}),)

    




admin.site.register(Transactions,TransactionsAdmin)
admin.site.register(User, UserAdmin)