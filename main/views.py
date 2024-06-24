from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Costumer, Contract
from django.db.models import Count,Sum
from django.http import HttpResponse
from datetime import datetime



def CheckPage(request):
    return HttpResponse("This is the check page")

def ContractPage(request):
    now = datetime.now()
    date = now.date()
    contract = Contract.objects.filter(id=2)
    return render(request, 'check_one.html', {'posts': contract, 'data': date})




def custom_action_view(request, customer_id):
    customer = get_object_or_404(Costumer, pk=customer_id)
    # Bu yerda kerakli amalni bajaring
    messages.success(request, 'Maxsus harakat muvaffaqiyatli amalga oshirildi!')
    return redirect('/admin/main/customer/')




def CheckPage(request):
    contracts = Contract.objects.values('city__name', 'room').annotate(
        room_count=Count('room'),
        total_money=Sum('money'),
        total_advance_payment=Sum('advance_payment')
    ).order_by('city__name', 'room')

    context = {
        'contracts': contracts,
    }
    return render(request, 'admin_chek.html', context)