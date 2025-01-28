from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from . models import Expense
from datetime import datetime
from dateutil.parser import parse
# from django.utils.dateparse import parse_date
from decimal import Decimal
from django.utils import timezone

# Create your views here.
def index(request):
    context = {
        'date_added': '',
        'name': '',
        'description': '',
        'amount': '',
        'category': '',
    }
    if request.method == 'POST':
        context['date_added'] = request.POST.get ('date_added')
        context['name'] = request.POST.get('name')
        context['description'] = request.POST.get('description')
        context['amount'] = request.POST.get('amount')
        context['category'] = request.POST.get ('category')

        if not context['date_added'] or not context['name'] or not context['description'] or not context['amount'] or not context['category']:
            messages.error(request, 'All fields must be filled')
            return render (request, 'myapp/index.html', context)
        try:
            # Validate and process amount
            amount_obj = abs(Decimal(str(context['amount'])))

            # Vaidate date format
            parsed_date = parse(context['date_added']).date()
            # date_obj = parsed_date.strftime('%Y-%m-%d')

            # this part should make sure that future dates cannot be handed in.
            now = timezone.now().date()
            if parsed_date > now:
                messages.error(request, f'The date cannot be in the future.')
                return render (request, 'myapp/index.html', context)
            
            date_fiff = now - parsed_date
            if date_fiff.days > 20:
                messages.error(request, f'The date is too far behind')
                return render (request, 'myapp/index.html', context)
            
            Expense.objects.create (
                date_added = parsed_date,
                name = context['name'],
                description = context['description'],
                amount = amount_obj,
                category = context['category'],
            )
            messages.success(request, f'Expense {context['name']} added successfully')
            return redirect('index')

        except ValueError as e:
            messages.error(request,f'Invalid date format: {e}')
            return render (request, 'myapp/index.html', context)
        except Exception as e:
            messages.error(request, f'{context['name']} expense not added: {e}')
            return render (request, 'myapp/index.html', context)
            
    return render(request,'myapp/index.html', context)