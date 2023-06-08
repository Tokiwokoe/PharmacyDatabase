from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, 'pharmacy/index.html', {'title': 'Главная страница'})


def property_type(request):
    property_type = PropertyType.objects.all()
    return render(request, 'pharmacy/lookup.html', {'lookup': property_type, 'title': 'Типы собственности'})


def dosage_form(request):
    dosage_form = DosageForm.objects.all()
    return render(request, 'pharmacy/lookup.html', {'lookup': dosage_form, 'title': 'Формы выпуска'})


def district(request):
    district = District.objects.all()
    return render(request, 'pharmacy/lookup.html', {'lookup': district, 'title': 'Районы'})


def country(request):
    country = Country.objects.all()
    return render(request, 'pharmacy/lookup.html', {'lookup': country, 'title': 'Страны'})


def pharmacological_group(request):
    pharmacological_group = PharmacologicalGroup.objects.all()
    return render(request, 'pharmacy/lookup.html', {'lookup': pharmacological_group, 'title': 'Фармакологические группы'})


def pharmacy(request):
    pharmacy = Pharmacy.objects.all()
    return render(request, 'pharmacy/pharmacy.html', {'table': pharmacy, 'title': 'Аптеки'})


def drug(request):
    drug = Drug.objects.all()
    return render(request, 'pharmacy/drug.html', {'table': drug, 'title': 'Препараты'})


def company(request):
    company = Company.objects.all()
    return render(request, 'pharmacy/company.html', {'table': company, 'title': 'Компании-производители'})
