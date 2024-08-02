from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Costumer, Contract
from django.db.models import Count,Sum
from django.http import HttpResponse
from datetime import datetime
import weasyprint
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit






def contract_pdf_view(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    context = {
        'contract': contract,
    }
    html = render_to_string('chek_mijozlar.html', context)
    
    pdf = weasyprint.HTML(string=html).write_pdf()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="contract_{}.pdf"'.format(contract_id)
    return response

def contract_check(request):
    return HttpResponse("This is the contract check view.")


def CheckPage(request):
    return HttpResponse("This is the check page")




def custom_action_view(request, customer_id):
    customer = get_object_or_404(Costumer, pk=customer_id)
    # Bu yerda kerakli amalni bajaring
    messages.success(request, 'Maxsus harakat muvaffaqiyatli amalga oshirildi!')
    return redirect('/admin/main/customer/')




# def CheckPage(request):
#     contracts = Contract.objects.values('city__name', 'room').annotate(
#         room_count=Count('room'),
#         total_money=Sum('money'),
#         total_advance_payment=Sum('advance_payment')
#     ).order_by('city__name', 'room')

#     context = {
#         'contracts': contracts,
#     }
#     return render(request, 'admin_chek.html', context)

def CheckPage(request):
    contracts = Contract.objects.values('city__name', 'room').annotate(
        room_count=Count('room'),
        total_money=Sum('money'),
        total_advance_payment=Sum('advance_payment')
    ).order_by('city__name', 'room')

    context = {
        'contracts': contracts,
    }
    html = render_to_string('admin_chek.html', context)
    
    pdf = weasyprint.HTML(string=html).write_pdf()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="contract_check.pdf"'
    return response