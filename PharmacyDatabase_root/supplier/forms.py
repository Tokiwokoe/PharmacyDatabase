from django import forms
import Pharmacy.models


class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.Pharmacy
        fields = ['number', 'property_type', 'district', 'phone']
