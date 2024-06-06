from django.contrib import admin
from .models import *

admin.site.register(City)
admin.site.register(Costumer)



@admin.register(Contract)
class PostAdmin(admin.ModelAdmin):
    list_display = ['city']
    # prepopulated_fields = {'monthTomoney': (f"{Contract.get_money}",)}


