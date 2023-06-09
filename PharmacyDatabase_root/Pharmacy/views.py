from django.db import connection
from django.shortcuts import render, redirect
from .models import *
import json
from openpyxl import Workbook
from django.http import HttpResponse


def index(request):
    return render(request, 'pharmacy/index.html', {'title': 'Главная страница'})


def property_type(request):
    property_type = PropertyType.objects.all()
    return render(request, 'pharmacy/lookup.html', {'name': 'property_type', 'lookup': property_type, 'title': 'Типы собственности'})


def dosage_form(request):
    dosage_form = DosageForm.objects.all()
    return render(request, 'pharmacy/lookup.html', {'name': 'dosage_form', 'lookup': dosage_form, 'title': 'Формы выпуска'})


def district(request):
    district = District.objects.all()
    return render(request, 'pharmacy/lookup.html', {'name': 'district', 'lookup': district, 'title': 'Районы'})


def country(request):
    country = Country.objects.all()
    return render(request, 'pharmacy/lookup.html', {'name': 'country', 'lookup': country, 'title': 'Страны'})


def pharmacological_group(request):
    pharmacological_group = PharmacologicalGroup.objects.all()
    return render(request, 'pharmacy/lookup.html', {'name': 'pharmacological_group', 'lookup': pharmacological_group, 'title': 'Фармакологические группы'})


def pharmacy(request):
    pharmacy = Pharmacy.objects.all()
    return render(request, 'pharmacy/pharmacy.html', {'name': 'pharmacy', 'table': pharmacy, 'title': 'Аптеки'})


def drug(request):
    drug = Drug.objects.all()
    return render(request, 'pharmacy/drug.html', {'name': 'drug', 'table': drug, 'title': 'Препараты'})


def company(request):
    company = Company.objects.all()
    return render(request, 'pharmacy/company.html', {'name': 'company', 'table': company, 'title': 'Компании-производители'})


def property_type_change(request, id):
    lookup = PropertyType.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('property_type')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'property_type'})


def dosage_form_change(request, id):
    lookup = DosageForm.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('dosage_form')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'dosage_form'})


def district_change(request, id):
    lookup = District.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('district')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'district'})


def country_change(request, id):
    lookup = Country.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('country')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'country'})


def pharmacological_group_change(request, id):
    lookup = PharmacologicalGroup.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('pharmacological_group')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'pharmacological_group'})


def pharmacy_change(request, id):
    table = Pharmacy.objects.get(id=id)
    return render(request, 'pharmacy/pharmacy_change.html', {'table': table})


def drug_change(request, id):
    table = Drug.objects.get(id=id)
    return render(request, 'pharmacy/drug_change.html', {'table': table})


def company_change(request, id):
    table = Company.objects.get(id=id)
    return render(request, 'pharmacy/company_change.html', {'table': table})


def execute_query(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM query15(4);")
            results = cursor.fetchall()

        return render(request, 'pharmacy/result.html', {'results': results})

    return render(request, 'index.html')


def generate_chart(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM query15(4);")
        results = cursor.fetchall()

    # Process the results and prepare data for the chart
    labels = [result[0] for result in results]
    data = [result[1] for result in results]

    # Pass the data to the template
    chart_data = {
        'labels': labels,
        'data': data,
    }

    return render(request, 'pharmacy/chart.html', {'chart_data': json.dumps(chart_data)})


def export_to_excel(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM query15(4);")
        results = cursor.fetchall()

    # Create a new workbook and get the active sheet
    wb = Workbook()
    sheet = wb.active

    # Write the column headers
    sheet['A1'] = 'Компания-производитель'
    sheet['B1'] = 'Всего препаратов'

    # Write the result rows
    for row_num, result in enumerate(results, start=2):
        sheet[f'A{row_num}'] = result[0]
        sheet[f'B{row_num}'] = result[1]

    # Set the response content type
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Set the file name
    response['Content-Disposition'] = 'attachment; filename=query15.xlsx'

    # Save the workbook to the response
    wb.save(response)

    return response
