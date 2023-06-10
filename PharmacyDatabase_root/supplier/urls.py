from django.urls import path
from supplier.views import (
    supplier_index,
    supplier_dosage_form,
    supplier_company,
    supplier_country,
    supplier_district,
    supplier_drug,
    supplier_pharmacy,
    supplier_property_type,
    supplier_pharmacological_group,
    supplier_pharmacy_update,
    supplier_pharmacy_create,
    supplier_pharmacy_delete,
)

urlpatterns = [
    path('', supplier_index, name='supplier_index'),
    path('dosage_form', supplier_dosage_form, name='supplier_dosage_form'),
    path('company', supplier_company, name='supplier_company'),
    path('country', supplier_country, name='supplier_country'),
    path('district', supplier_district, name='supplier_district'),
    path('drug', supplier_drug, name='supplier_drug'),
    path('pharmacy', supplier_pharmacy, name='supplier_pharmacy'),
    path('property_type', supplier_property_type, name='supplier_property_type'),
    path('pharmacological_group', supplier_pharmacological_group, name='supplier_pharmacological_group'),
    path('pharmacy_update/<int:pharmacy_id>/', supplier_pharmacy_update, name='supplier_pharmacy_update'),
    path('pharmacy_create', supplier_pharmacy_create, name='supplier_pharmacy_create'),
    path('pharmacy_delete/<int:pharmacy_id>/', supplier_pharmacy_delete, name='supplier_pharmacy_delete')
]
