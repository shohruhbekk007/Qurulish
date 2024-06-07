from django.contrib import admin
from .models import *
from .forms import ContractForm


admin.site.register(City)


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'phone_number', 'mavzu')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context)
        if hasattr(response, 'context_data'):
            cl = response.context_data['cl']
            queryset = cl.result_list
            for item in queryset:
                item.row_class = 'colorize-row' if item.mavzu != 'sotib olmoqchi' else ''
        return response

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    form = ContractForm
    list_display = ['city', 'full_name', 'room', 'monthTomoney']
    class Media:
        js = ('js/calculate.js',)
    def save_model(self, request, obj, form, change):
        if obj.month > 0:
            obj.monthTomoney = str(obj.money / obj.month)
        else:
            obj.monthTomoney = "Invalid input"
        super().save_model(request, obj, form, change)