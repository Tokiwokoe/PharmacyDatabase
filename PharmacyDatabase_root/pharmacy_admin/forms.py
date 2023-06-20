from django import forms
import pharmacy_admin.models


class DistrictForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.District
        fields = ['name']


class CountryForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.Country
        fields = ['name']


class DosageFormForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.DosageForm
        fields = ['name']


class PharmacologicalGroupForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.PharmacologicalGroup
        fields = ['name']


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = pharmacy_admin.models.PropertyType
        fields = ['name']
