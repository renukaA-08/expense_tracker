from django.shortcuts import render,redirect
from django.http import HttpResponse
from tracker.models import CurrentBalance , TrackingHistory
# Create your views here.

def index(request):
    if request.method == "POST" :
        description = request.POST.get("description")
        amount = request.POST.get("amt")
        currentbal , _ = CurrentBalance.objects.get_or_create(id = 1)
        expense_type = "Credit" if float(amount) > 0 else "Debit"
        trackhistory = TrackingHistory.objects.create(
            description = description ,
            amount= amount ,
            current_balance = currentbal ,
            expense_type = expense_type
        )
        currentbal.current_balance += float(amount)
        currentbal.save()
        print(description , amount ,currentbal.current_balance )
        return redirect('/')
    income = 0
    expense = 0
    for expenses in TrackingHistory.objects.all():
        if expenses.expense_type == "Credit":
            income += expenses.amount 
        if expenses.expense_type == "Debit":
            expense += -expenses.amount
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    context = {'income':income , 'expenses' : expense , 'current_balance' :current_balance , 'history':TrackingHistory.objects.all()}
    return render(request , 'index.html',context )
def delete(request , id):
    transaction = TrackingHistory.objects.filter(id=id)
    print(transaction)
    if transaction.exists():
        transaction = TrackingHistory.objects.get(id = id)
        currentBal,_ = CurrentBalance.objects.get_or_create(id = 1)
        currentBal.current_balance = currentBal.current_balance - transaction.amount
        currentBal.save()
    transaction.delete()
    return redirect('/')

