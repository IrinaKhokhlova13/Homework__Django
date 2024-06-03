from django.db import models

from users.models import User

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
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)


    def __str__(self):
        return f'{self.name_product} {self.description} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ('cancellation_of_publication', 'Canceling the publication of the product'),
            ('changes_the_description', 'Changes the description of any product'),
            ('changes_the_category', 'Changes the category of any product'),

        ]


class Contacts(models.Model):
    city = models.CharField(max_length=50, verbose_name="Страна")
    identity_nalog_number = models.IntegerField(verbose_name="ИНН")
    address = models.TextField(verbose_name="Адрес")
    slug = models.CharField(max_length=255, verbose_name="URL", **NULLABLE)

    def __str__(self):
        return f"{self.city} {self.identity_nalog_number} {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"




class Version(models.Model):

    """Модель версия продукта"""
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='versions', **NULLABLE)
    number_v = models.PositiveIntegerField(verbose_name='номер версии')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    current_version = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name_version} - {self.number_v}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'