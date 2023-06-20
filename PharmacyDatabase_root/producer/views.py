from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import pharmacy_admin.models
from .forms import CompanyForm, DrugForm
from django.db.models import Max


@login_required
def producer_index(request):
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


def producer_dosage_form(request):
    dosage_form = pharmacy_admin.models.DosageForm.objects.all()
    return render(request, 'producer/lookup.html', {'name': 'dosage_form', 'lookup': dosage_form, 'title': 'Формы выпуска'})


def producer_property_type(request):
    property_type = pharmacy_admin.models.PropertyType.objects.all()
    return render(request, 'producer/lookup.html', {'name': 'property_type', 'lookup': property_type, 'title': 'Типы собственности'})


def producer_district(request):
    district = pharmacy_admin.models.District.objects.all()
    return render(request, 'producer/lookup.html', {'name': 'district', 'lookup': district, 'title': 'Районы'})


def producer_country(request):
    country = pharmacy_admin.models.Country.objects.all()
    return render(request, 'producer/lookup.html', {'name': 'country', 'lookup': country, 'title': 'Страны'})


def producer_pharmacological_group(request):
    pharmacological_group = pharmacy_admin.models.PharmacologicalGroup.objects.all()
    return render(request, 'producer/lookup.html', {'name': 'pharmacological_group', 'lookup': pharmacological_group, 'title': 'Фармакологические группы'})


def producer_pharmacy(request):
    pharmacy = pharmacy_admin.models.Pharmacy.objects.all()
    return render(request, 'producer/pharmacy.html', {'name': 'pharmacy', 'table': pharmacy, 'title': 'Аптеки'})


def producer_drug(request):
    drug = pharmacy_admin.models.Drug.objects.all()
    return render(request, 'producer/drug.html', {'name': 'drug', 'table': drug, 'title': 'Препараты'})


def producer_company(request):
    company = pharmacy_admin.models.Company.objects.all()
    return render(request, 'producer/company.html', {'name': 'company', 'table': company, 'title': 'Компании-производители'})


@login_required
def producer_company_update(request, company_id):
    company = get_object_or_404(pharmacy_admin.models.Company, id=company_id)

    if request.method == 'POST':
        # Получить данные из POST-запроса
        name = request.POST.get('name')
        year = request.POST.get('year')
        address = request.POST.get('address')


        # Обновить поля объекта компании
        company.name = name
        company.year = year
        company.address = address

        # Сохранить изменения
        company.save()

        # Редирект на страницу с деталями аптеки или другую нужную страницу
        return redirect('producer_company')

    # Если метод запроса не POST, отобразить форму для редактирования аптеки
    country = pharmacy_admin.models.Country.objects.all()
    property_types = pharmacy_admin.models.PropertyType.objects.all()

    return render(request, 'producer/company_update.html', {'company': company, 'countries': country, 'property_types': property_types})


def producer_company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            max_id = pharmacy_admin.models.Company.objects.aggregate(Max('id'))['id__max']
            next_id = max_id + 1 if max_id else 1
            form.instance.id = next_id
            form.save()
            return redirect('producer_company')
    else:
        max_id = pharmacy_admin.models.Company.objects.aggregate(Max('id'))['id__max']
        initial_id = max_id + 1 if max_id else 1
        form = CompanyForm(initial={'id': initial_id})

    country = pharmacy_admin.models.Country.objects.all()
    property_types = pharmacy_admin.models.PropertyType.objects.all()

    context = {
        'form': form,
        'property_types': property_types,
        'countries': country,
    }

    return render(request, 'producer/company_create.html', context)


@login_required
def producer_company_delete(request, company_id):
    company = get_object_or_404(pharmacy_admin.models.Company, id=company_id)

    if request.method == 'POST':
        company.delete()
        return redirect('producer_company')  # Редирект на другую страницу после удаления

    return render(request, 'producer/company_delete.html', {'company': company})


@login_required
def producer_drug_update(request, drug_id):
    drug = get_object_or_404(pharmacy_admin.models.Drug, id=drug_id)

    if request.method == 'POST':
        # Получить данные из POST-запроса
        name = request.POST.get('name')


        # Обновить поля объекта аптеки
        drug.name = name

        # Сохранить изменения
        drug.save()

        # Редирект на страницу с деталями аптеки или другую нужную страницу
        return redirect('producer_drug')

    # Если метод запроса не POST, отобразить форму для редактирования аптеки
    company = pharmacy_admin.models.Company.objects.all()
    dosage_form = pharmacy_admin.models.DosageForm.objects.all()
    pharmacological_group = pharmacy_admin.models.PharmacologicalGroup.objects.all()

    context = {
        'drug': drug,
        'companies': company,
        'dosage_forms': dosage_form,
        'pharmacological_groups': pharmacological_group,
    }

    return render(request, 'producer/drug_update.html', context)


def producer_drug_create(request):
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            drug = form.save(commit=False)
            drug.created_by = request.user
            max_id = pharmacy_admin.models.Drug.objects.aggregate(Max('id'))['id__max']
            next_id = max_id + 1 if max_id else 1
            form.instance.id = next_id
            form.save()
            return redirect('producer_drug')
    else:
        max_id = pharmacy_admin.models.Drug.objects.aggregate(Max('id'))['id__max']
        initial_id = max_id + 1 if max_id else 1
        form = DrugForm(initial={'id': initial_id})

    company = pharmacy_admin.models.Company.objects.all()
    dosage_form = pharmacy_admin.models.DosageForm.objects.all()
    pharmacological_group = pharmacy_admin.models.PharmacologicalGroup.objects.all()

    context = {
        'form': form,
        'companies': company,
        'dosage_forms': dosage_form,
        'pharmacological_groups': pharmacological_group,
    }

    return render(request, 'producer/drug_create.html', context)


@login_required
def producer_drug_delete(request, drug_id):
    drug = get_object_or_404(pharmacy_admin.models.Drug, id=drug_id)

    if request.method == 'POST':
        drug.delete()
        return redirect('producer_drug')  # Редирект на другую страницу после удаления

    return render(request, 'producer/drug_delete.html', {'drug': drug})
