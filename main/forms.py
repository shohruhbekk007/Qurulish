from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        money = cleaned_data.get("money")
        month = cleaned_data.get("month")

        if money is not None and month is not None and month > 0:
            cleaned_data['monthTomoney'] = str(money / month)
        else:
            cleaned_data['monthTomoney'] = "Invalid input"
        
        return cleaned_data
