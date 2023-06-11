from django import forms
import Pharmacy.models


class DistrictForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.District
        fields = ['name']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.Country
        fields = ['name']


class DosageFormForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.DosageForm
        fields = ['name']


class PharmacologicalGroupForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.PharmacologicalGroup
        fields = ['name']


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = Pharmacy.models.PropertyType
        fields = ['name']
