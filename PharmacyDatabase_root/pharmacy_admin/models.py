from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from psqlextra.indexes import UniqueIndex
from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel


class PropertyType(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class DosageForm(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PharmacologicalGroup(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=32)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MaxValueValidator(datetime.date.today().year), MinValueValidator(1890)])
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Drug(models.Model):
    name = models.CharField(max_length=32)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    dosage_form = models.ForeignKey(DosageForm, on_delete=models.CASCADE)
    pharmacological_group = models.ForeignKey(PharmacologicalGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    number = models.IntegerField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    phone = models.CharField(max_length=19)
    drugs = models.ManyToManyField(Drug, through="DrugInPharmacy")

    def __str__(self):
        return str(self.number)


class DrugInPharmacy(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["delivery_date"]

    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'Препарат: {self.drug.name}, аптека: {str(self.pharmacy.number)}'
