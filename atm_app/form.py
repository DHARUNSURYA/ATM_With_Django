from django import forms

class DepositForm(forms.Form):
    amount = forms.DecimalField()

class WithdrawForm(forms.Form):
    amount = forms.DecimalField()

class CheckBalanceForm(forms.Form):
    pass

class PinForm(forms.Form):
    pin = forms.CharField(max_length=4, widget=forms.PasswordInput())
