from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.name_category} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'



class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание продукта')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    create_at = models.DateField(verbose_name='дата создания')
    update_at = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name_product} {self.description} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
