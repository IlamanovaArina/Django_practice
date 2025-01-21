from django.db import models


class Category(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name_product']


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')
    imagery = models.ImageField(upload_to='photos/', verbose_name='Изображение', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    purchase_price = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_product}  from the category: {self.category}.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name_product']


