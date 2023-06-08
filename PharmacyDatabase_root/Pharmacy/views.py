from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


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
