from django.db import models
from datetime import date

from django.template import engines
# Create your models here.


class Category(models.Model):
    name = models.CharField("Имя категории", max_length=150)
    url = models.SlugField("Ссылка на категорию", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField("Имя", max_length=150)
    logo = models.ImageField("Логотип", upload_to="brand_logos/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class CarModel(models.Model):
    name = models.CharField(max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class DriveUnit(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Привод"
        verbose_name_plural = "Привод"


class FuelType(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип топлива"
        verbose_name_plural = "Типы топлива"


class BodyType(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузова"


class EngineCapacity(models.Model):
    capacity = models.FloatField()

    class Meta:
        verbose_name = "Объем"
        verbose_name_plural = "Объем"


class SteeringWheel(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Руль"
        verbose_name_plural = "Руль"


class Transmission(models.Model):
    name = models.CharField(max_length=130)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробка передач"


class Car(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    carModel = models.ForeignKey(
        CarModel, on_delete=models.SET_NULL, null=True)
    driveUnit = models.ForeignKey(
        DriveUnit, on_delete=models.SET_NULL, null=True)
    fuelType = models.ForeignKey(
        FuelType, on_delete=models.SET_NULL, null=True)
    bodyType = models.ForeignKey(
        BodyType, on_delete=models.SET_NULL, null=True)
    engineCapacity = models.ForeignKey(
        EngineCapacity, on_delete=models.SET_NULL, null=True)
    steeringWheel = models.ForeignKey(
        SteeringWheel, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(
        Transmission, on_delete=models.SET_NULL, null=True)
    sold = models.BooleanField(default=False)
    description = models.TextField()
    mileage = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    year_of_issue = models.DateField(default=date.today)
    url = models.SlugField()
    created_at = models.DateTimeField(auto_now=True)



class Images(models.Model):
    image = models.ImageField(upload_to="cars/")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url
