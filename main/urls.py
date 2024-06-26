from django.urls import path
from .views import custom_action_view, CheckPage, contract_pdf_view, contract_check

urlpatterns = [
    path('main/custom_action/<int:customer_id>/', custom_action_view, name='admin_custom_action'),
    path('chek/users/', CheckPage, name='chek'),
#     path('admin/contract/<int:contract_id>/pdf/', contract_pdf_view, name='admin_contract_pdf'),
    path('main/contract/check/', contract_check, name='admin_contract_check'),
    path('main/contract/<int:contract_id>/pdf/', contract_pdf_view, name='admin_contract_pdf'),

]