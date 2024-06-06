from django.contrib import admin
from .models import *
from .forms import ContractForm


admin.site.register(City)
admin.site.register(Costumer)


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