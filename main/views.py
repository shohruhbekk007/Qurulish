from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Costumer

def custom_action_view(request, customer_id):
    customer = get_object_or_404(Costumer, pk=customer_id)
    # Bu yerda kerakli amalni bajaring
    messages.success(request, 'Maxsus harakat muvaffaqiyatli amalga oshirildi!')
    return redirect('/admin/main/customer/')
