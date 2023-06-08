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
]
