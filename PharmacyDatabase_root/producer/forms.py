from django import forms
import pharmacy_admin.models


class CompanyForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.Company
        fields = ['name', 'year', 'address', 'country', 'property_type']


class DrugForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.Drug
        fields = ['name', 'company', 'dosage_form', 'pharmacological_group']
