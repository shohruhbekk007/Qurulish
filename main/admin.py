from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
from .forms import ContractForm
from unfold.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("username", "is_active", "is_staff")
    fields = ["username", "first_name", "last_name", "is_staff", "is_active", "email"]


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ("name",)
    fields = list_display


@admin.register(Costumer)
class CustomerAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'phone_number', 'mavzu')
    # list_filter = ("mavzu", )
    # search_fields = ('last_name',)

    def get_row_color(self, obj):
        return 'colorize-row' if obj.mavzu != 'sotib olmoqchi' else ''

    get_row_color.short_description = 'Color'
    get_row_color.admin_order_field = 'mavzu'

    def changelist_view(self, request, extra_context = None):
        custom_context = {"sms_yuborish_button": "<button href=\"#\" class=\"custom-button\" onclick='customAction()'>Sms yuborish</button>"}
        extra_context = extra_context or {}
        extra_context.update(custom_context)
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(Contract)
class ContractAdmin(ModelAdmin):
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

@admin.register(SmsMessage)
class SmsAdmin(ModelAdmin):
    list_display = ['name']