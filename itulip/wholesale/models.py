from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Клиенты
class Client(models.Model):
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    middle_name = models.CharField(max_length=255, verbose_name="Отчество")
    phone_number = models.CharField(max_length=255, verbose_name="Номер телефона")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

# Заказы
class Order(models.Model):
    full_price = models.CharField(max_length=255, verbose_name="Итоговая стоимость")
    prepayment = models.CharField(max_length=255, verbose_name="Предоплата")
    date = models.DateTimeField(verbose_name="Дата и Время")
    client = models.ForeignKey(Client, models.CASCADE)


# Сорта
class Sort(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    shade = models.CharField(max_length=255, verbose_name="Оттенок")
    image = models.ImageField(upload_to=f'photos/{shade}/')
    planted = models.IntegerField(verbose_name="Посажено")
    collected = models.IntegerField(verbose_name="Собрано")
    died = models.IntegerField(verbose_name="Погибло")
    sold = models.IntegerField(verbose_name="Продано")


# Детали заказа
class OrderDetail(models.Model):
    quantity = models.IntegerField(verbose_name="Количество")
    order = models.ForeignKey(Order, models.CASCADE)
    sort = models.ForeignKey(Sort, models.CASCADE)

