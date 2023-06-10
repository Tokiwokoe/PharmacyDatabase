from django.urls import path
from Pharmacy.views import *

urlpatterns = [
    path('', execute_query, name='execute_query'),
    path('generate-chart/', generate_chart, name='generate_chart'),
    path('export-to-excel/', export_to_excel, name='export_to_excel'),
    path('query/<int:value>/', queries, name='queries'),

    path('property_type/', property_type, name='property_type'),
    path('dosage_form/', dosage_form, name='dosage_form'),
    path('district/', district, name='district'),
    path('country/', country, name='country'),
    path('pharmacological_group/', pharmacological_group, name='pharmacological_group'),
    path('pharmacy/', pharmacy, name='pharmacy'),
    path('drug/', drug, name='drug'),
    path('company/', company, name='company'),

    path('property_type/<int:id>/', property_type_update, name='property_type_change'),
    path('dosage_form/<int:id>/', dosage_form_update, name='dosage_form_change'),
    path('district/<int:id>/', district_update, name='district_change'),
    path('country/<int:id>/', country_update, name='country_change'),
    path('pharmacological_group/<int:id>/', pharmacological_group_update, name='pharmacological_group_change'),
]
