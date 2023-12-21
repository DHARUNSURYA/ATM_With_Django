from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Account
from .form import DepositForm, WithdrawForm, CheckBalanceForm, PinForm

def home(request):
    return render(request, 'index.html')

def check_pin(request):
    if request.method == 'POST':
        pin_form = PinForm(request.POST)
        if pin_form.is_valid():
            entered_pin = pin_form.cleaned_data['pin']
            account = Account.objects.first()  
            if account and entered_pin == account.pin:
                return redirect('home')
            else:
                messages.error(request, 'Invalid PIN. Please try again.')
    else:
        pin_form = PinForm()
    return render(request, 'pin.html', {'pin_form': pin_form})

def deposit(request):
    account = Account.objects.first()  
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            account.balance += amount
            account.save()
            return redirect('check_balance')
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form})

def withdraw(request):
    account = Account.objects.first()  
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                return redirect('check_balance')
            else:
                messages.error(request, 'Insufficient funds')
    else:
        form = WithdrawForm()
    return render(request, 'width.html', {'form': form})

def check_balance(request):
    account = Account.objects.first()  
    balance = account.balance
    return render(request, 'check.html', {'balance': balance})
