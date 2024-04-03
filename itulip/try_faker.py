from django.db import models
from .models import Sorts
from faker import Faker
import os

fake = Faker()


def generate_sorts(num_sorts):
    sorts = []
    for _ in range(num_sorts):
        title = fake.word()  # Генерация случайного названия сорта тюльпанов
        shade = fake.color_name()  # Генерация случайного оттенка цвета
        image_filename = fake.file_name(category='image',
                                        extension='jpg')  # Генерация случайного имени файла изображения
        planted = fake.random_int(min=0, max=1000)  # Генерация случайного числа для поля "Посажено"
        collected = fake.random_int(min=0, max=planted)  # Генерация случайного числа для поля "Собрано"
        died = fake.random_int(min=0, max=planted - collected)  # Генерация случайного числа для поля "Погибло"
        sold = fake.random_int(min=0,
                               max=collected) if collected is not None else 0  # Генерация случайного числа для поля "Продано"

        sort = Sorts(
            title=title,
            shade=shade,
            image=os.path.join('photos', shade, image_filename),
            planted=planted,
            collected=collected,
            died=died,
            sold=sold
        )
        sorts.append(sort)
    return sorts


sorts = generate_sorts(10)

for sort in sorts:
    sort.save()