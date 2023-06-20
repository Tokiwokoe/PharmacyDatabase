from django import forms
import pharmacy_admin.models


class PharmacyForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.Pharmacy
        fields = ['number', 'property_type', 'district', 'phone']
