from django.urls import path
from .views import custom_action_view, CheckPage, ContractPage

urlpatterns = [
        path('admin/custom_action/<int:customer_id>/', custom_action_view, name='custom_action'),
        path('chek/users/', CheckPage, name='chek'),
        path('contract_check/', ContractPage, name='contract_check'),

]