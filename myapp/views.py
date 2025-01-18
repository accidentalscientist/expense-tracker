from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from . models import Expense

# Create your views here.
def index(request):
    if request.method == 'POST':
        date_added = request.POST.get ('date_added')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        category = request.POST.get ('category')

        if not date_added or not description or not amount or not category:
            messages.error(request, 'All fields must be filled')
            print('Field missing')
        # if amount < 0 or amount ==0:
            # messages.error (request, 'Amount cannot be lesser or equal to zero') 
        try:
            Expense.objects.create (
                date_added = date_added,
                description = description,
                amount = amount,
                category = category,
            )
            print('Expense added successfully')
            messages.success(request, 'Expense added successfully')
            return redirect('index')
        except Exception as e:
            messages.error(request, 'Not addded')
            print(f'Expense not added str{e}')
            
    return render(request,'myapp/index.html')