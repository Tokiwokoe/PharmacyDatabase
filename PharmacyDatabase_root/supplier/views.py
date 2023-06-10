from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import Pharmacy.models
from .forms import PharmacyForm
from django.db.models import Max



@login_required
def supplier_index(request):
    if request.user.groups.filter(name='administrator').exists():
        # Редирект для администратора
        return render(request, 'pharmacy/index.html', {'title': 'Режим запросов'})  # Замените 'admin_dashboard' на имя URL-шаблона для административной панели
    elif request.user.groups.filter(name='supplier').exists():
        # Редирект для поставщика
        return render(request, 'supplier/index.html')  # Замените 'supplier_dashboard' на имя URL-шаблона для панели поставщика
    else:
        # Редирект для остальных пользователей
        return render(request, 'user/index.html')  # Замените 'user_dashboard' на имя URL-шаблона для панели обычного пользователя


def supplier_dosage_form(request):
    dosage_form = Pharmacy.models.DosageForm.objects.all()
    return render(request, 'supplier/lookup.html', {'name': 'dosage_form', 'lookup': dosage_form, 'title': 'Формы выпуска'})


def supplier_property_type(request):
    property_type = Pharmacy.models.PropertyType.objects.all()
    return render(request, 'supplier/lookup.html', {'name': 'property_type', 'lookup': property_type, 'title': 'Типы собственности'})


def supplier_district(request):
    district = Pharmacy.models.District.objects.all()
    return render(request, 'supplier/lookup.html', {'name': 'district', 'lookup': district, 'title': 'Районы'})


def supplier_country(request):
    country = Pharmacy.models.Country.objects.all()
    return render(request, 'supplier/lookup.html', {'name': 'country', 'lookup': country, 'title': 'Страны'})


def supplier_pharmacological_group(request):
    pharmacological_group = Pharmacy.models.PharmacologicalGroup.objects.all()
    return render(request, 'supplier/lookup.html', {'name': 'pharmacological_group', 'lookup': pharmacological_group, 'title': 'Фармакологические группы'})


def supplier_pharmacy(request):
    pharmacy = Pharmacy.models.Pharmacy.objects.all()
    return render(request, 'supplier/pharmacy.html', {'name': 'pharmacy', 'table': pharmacy, 'title': 'Аптеки'})


def supplier_drug(request):
    drug = Pharmacy.models.Drug.objects.all()
    return render(request, 'supplier/drug.html', {'name': 'drug', 'table': drug, 'title': 'Препараты'})


def supplier_company(request):
    company = Pharmacy.models.Company.objects.all()
    return render(request, 'supplier/company.html', {'name': 'company', 'table': company, 'title': 'Компании-производители'})


@login_required
def supplier_pharmacy_update(request, pharmacy_id):
    pharmacy = get_object_or_404(Pharmacy.models.Pharmacy, id=pharmacy_id)

    if request.method == 'POST':
        # Получить данные из POST-запроса
        number = request.POST.get('number')
        property_type_id = request.POST.get('property_type')
        district_id = request.POST.get('district')
        phone = request.POST.get('phone')

        # Обновить поля объекта аптеки
        pharmacy.number = number
        pharmacy.property_type_id = property_type_id
        pharmacy.district_id = district_id
        pharmacy.phone = phone

        # Сохранить изменения
        pharmacy.save()

        # Редирект на страницу с деталями аптеки или другую нужную страницу
        return redirect('supplier_pharmacy')

    # Если метод запроса не POST, отобразить форму для редактирования аптеки
    property_types = Pharmacy.models.PropertyType.objects.all()
    districts = Pharmacy.models.District.objects.all()

    return render(request, 'supplier/pharmacy_update.html', {'pharmacy': pharmacy, 'property_types': property_types, 'districts': districts})


def supplier_pharmacy_create(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            pharmacy = form.save(commit=False)
            pharmacy.created_by = request.user
            max_id = Pharmacy.models.Pharmacy.objects.aggregate(Max('id'))['id__max']
            next_id = max_id + 1 if max_id else 1
            form.instance.id = next_id
            form.save()
            return redirect('supplier_pharmacy')
    else:
        max_id = Pharmacy.models.Pharmacy.objects.aggregate(Max('id'))['id__max']
        initial_id = max_id + 1 if max_id else 1
        form = PharmacyForm(initial={'id': initial_id})

    property_types = Pharmacy.models.PropertyType.objects.all()
    districts = Pharmacy.models.District.objects.all()

    context = {
        'form': form,
        'property_types': property_types,
        'districts': districts,
    }

    return render(request, 'supplier/pharmacy_create.html', context)


@login_required
def supplier_pharmacy_delete(request, pharmacy_id):
    pharmacy = get_object_or_404(Pharmacy.models.Pharmacy, id=pharmacy_id)

    if request.method == 'POST':
        pharmacy.delete()
        return redirect('supplier_pharmacy')  # Редирект на другую страницу после удаления

    return render(request, 'supplier/pharmacy_delete.html', {'pharmacy': pharmacy})
