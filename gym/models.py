from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Suplement(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    content = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спортивное питание'
        verbose_name_plural = 'Спортивное питание'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
