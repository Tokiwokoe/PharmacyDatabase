from django.urls import path
from Pharmacy.views import *

urlpatterns = [
    path('', index, name='pharmacy_index'),

    path('property_type/', property_type, name='property_type'),
    path('dosage_form/', dosage_form, name='dosage_form'),
    path('district/', district, name='district'),
    path('country/', country, name='country'),
    path('pharmacological_group/', pharmacological_group, name='pharmacological_group'),
    path('pharmacy/', pharmacy, name='pharmacy'),
    path('drug/', drug, name='drug'),
    path('company/', company, name='company'),

    path('property_type/<int:id>/', property_type_change, name='property_type_change'),
    path('dosage_form/<int:id>/', dosage_form_change, name='dosage_form_change'),
    path('district/<int:id>/', district_change, name='district_change'),
    path('country/<int:id>/', country_change, name='country_change'),
    path('pharmacological_group/<int:id>/', pharmacological_group_change, name='pharmacological_group_change'),
    path('pharmacy/<int:id>/', pharmacy_change, name='pharmacy_change'),
    path('drug/<int:id>/', drug_change, name='drug_change'),
    path('company/<int:id>/', company_change, name='company_change'),
]
