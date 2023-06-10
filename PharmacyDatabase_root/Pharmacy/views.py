from django.db import connection
from django.shortcuts import render, redirect
import supplier
from .models import *
import json
from openpyxl import Workbook
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from supplier.views import supplier_index
from producer.views import producer_index


@login_required  # Декоратор, требующий аутентификации пользователя
def index(request):
    if request.user.groups.filter(name='administrator').exists():
        # Редирект для администратора
        return render(request, 'pharmacy/index.html', {'title': 'Режим запросов'})
    elif request.user.groups.filter(name='supplier').exists():
        # Редирект для поставщика
        return render(request, 'supplier/index.html')
    elif request.user.groups.filter(name='producer').exists():
        return render(request, 'producer/index.html')
    else:
        # Редирект для остальных пользователей
        return render(request, 'user/index.html')

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


def property_type_update(request, id):
    lookup = PropertyType.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('property_type')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'property_type'})


def dosage_form_update(request, id):
    lookup = DosageForm.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('dosage_form')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'dosage_form'})


def district_update(request, id):
    lookup = District.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('district')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'district'})


def country_update(request, id):
    lookup = Country.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('country')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'country'})


def pharmacological_group_update(request, id):
    lookup = PharmacologicalGroup.objects.get(id=id)
    if request.method == 'POST':
        lookup.name = request.POST.get('name')
        lookup.save()
        return redirect('pharmacological_group')  # Перенаправление на страницу со списком районов
    return render(request, 'pharmacy/lookup_change.html', {'lookup': lookup, 'name': 'pharmacological_group'})


def execute_query(request):
    districts = District.objects.all()
    for district in districts:
        print(district.name)
    return render(request, 'pharmacy/index.html', {'districts': districts})


def queries(request, value, data):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM query{value}({data});")
        results = cursor.fetchall()
        title = ['Симметричное внутреннее соединение с условием отбора по внешнему ключу (часть 1)', 'Симметричное внутреннее соединение с условием отбора по внешнему ключу (часть 2)', 'Симметричное внутреннее соединение с условием отбора по датам (часть 1)', 'Симметричное внутреннее соединение с условием отбора по датам (часть 2)', 'Симметричное внутреннее соединение без условия (часть 1)', 'Симметричное внутреннее соединение без условия (часть 2)', 'Симметричное внутреннее соединение без условия (часть 3)', 'Левое внешнее соединение', 'Правое внешнее соединение', 'Запрос на запросе по принципу левого соединения', 'Итоговый запрос без условия', 'Итоговый запрос с условием на группы', 'Итоговый запрос с условием на данные', 'Итоговый запрос с условием на данные и на группы', 'Итоговый запрос с условием на данные и на группы', 'Запрос с подзапросом']
    return render(request, 'pharmacy/result.html', {'results': results, 'number': value, 'title': title[value-1]})


def generate_chart(request, value):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM query{value}(4);")
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


def export_to_excel(request, value):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM query{value}(4);")
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
