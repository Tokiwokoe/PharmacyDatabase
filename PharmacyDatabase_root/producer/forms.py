from django import forms
import Pharmacy.models


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.Company
        fields = ['name', 'year', 'address', 'country', 'property_type']


class DrugForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.Drug
        fields = ['name', 'company', 'dosage_form', 'pharmacological_group']
