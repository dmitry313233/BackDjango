from django.db import models
from django.db.models import ForeignKey

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название продукта')
    start_data = models.DateTimeField(verbose_name='Время и дата старта')
    cost = models.IntegerField(verbose_name='Стоимость')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='Преподаватель')

    def __str__(self):
        return f'{self.name} {self.start_data} {self.owner}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название урока')
    video_url = models.URLField(unique=True, verbose_name='Ссылка на видео')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons', verbose_name='Продукт')

    def __str__(self):
        return f'{self.name}, {self.video_url}, {self.product}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Group(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название группы')
    students = models.ManyToManyField(User, related_name='groups_in', verbose_name='Ученики')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups', verbose_name='Продукт')

    def __str__(self):
        return f'{self.name}, {self.product}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
