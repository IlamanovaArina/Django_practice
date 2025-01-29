from django.db import models


class BlogEntry(models.Model):
    header = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', null=True, blank=True)
    preview = models.ImageField(verbose_name='Превью', null=True, blank=True)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    publication_attribute = models.BooleanField(verbose_name='Признак публикации')
    quantity_views = models.IntegerField(verbose_name='Количество просмотров', null=True, blank=True)

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'

    def str(self):
        return f'{self.header}'