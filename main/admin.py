from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
from .forms import ContractForm
from unfold.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect

admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.register(HouseMod)

# @admin.register(User)
# class UserAdmin(ModelAdmin):
#     list_display = ("username", "is_active", "is_staff")
#     fields = ["username", "first_name", "last_name", "is_staff", "is_active", "email"]


@admin.register(City)
class CityAdmin(ModelAdmin):
    list_display = ("name",)
    fields = list_display

@admin.register(Room)
class RoomCity(ModelAdmin):
    list_display = ('city', 'number')

@admin.register(Costumer)
class CustomerAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'phone_number', 'mavzu')
    list_filter = ('mavzu',) 
    
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
    list_display = ['city', 'full_name', 'room', 'monthTomoney']
    change_form_template = "admin/change_form.html"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['contract_check_button'] = format_html(
            '<a href="{}" class="custom-button" target="_blank">Check Contract</a>',
            reverse('admin_contract_check')
        )
        extra_context['pdf_button'] = format_html(
            '<a href="{}" class="custom-button" target="_blank">View PDF</a>',
            reverse('admin_contract_pdf', args=[object_id])
        )
        return super().change_view(request, object_id, form_url, extra_context=extra_context)



# @admin.register(SmsMessage)
# class SmsAdmin(ModelAdmin):
#     list_display = ['name']

#     def changelist_view(self, request, extra_context=None):
#         custom_context = {
#             "sms_yuborish_button": format_html(
#                 '<a href="{}" class="custom-button">Hisobot</a>',
#                 reverse('chek')
#             )
#         }
#         extra_context = extra_context or {}
#         extra_context.update(custom_context)
#         return super().changelist_view(request, extra_context=extra_context)

#     class Media:
#         css = {
#             'all': ('admin/css/custom_admin.css',)
#         }
@admin.register(SmsMessage)
class SmsAdmin(ModelAdmin):
    list_display = ['name']

    def changelist_view(self, request, extra_context=None):
        custom_context = {
            "sms_yuborish_button": format_html(
                '<a href="{}" class="custom-button" target="_blank">Hisobot</a>',
                reverse('chek')
            )
        }
        extra_context = extra_context or {}
        extra_context.update(custom_context)
        return super().changelist_view(request, extra_context=extra_context)

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
