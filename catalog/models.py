from django.db import models

from config import settings


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    imagery = models.ImageField(upload_to='catalog/', verbose_name='Изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publication_attribute = models.BooleanField(null=True, blank=True, default=False, verbose_name="Признак публикации")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Владелец')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category']
        permissions = [
            ('can_unpublish_product', 'can unpublish product',),
            ('can_delete_product', 'can delete product')
        ]

    def save(self, *args, **kwargs):
        """ Если объект еще не сохранен (т.е. new объект), устанавливаем owner """
        if self.pk is None and 'request' in kwargs:
            self.owner = kwargs.pop('request').user
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}  from the category: {self.category}.'