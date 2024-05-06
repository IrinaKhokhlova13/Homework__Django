from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("fixtures\catalog_data.json", encoding="utf-16") as file:
            data = json.load(file)
            data = data[0:3]
        return data

    # Здесь мы получаем данные из фикстур с категориями

    @staticmethod
    def json_read_products():
        with open("fixtures\catalog_data.json", encoding="utf-16") as file:
            data = json.load(file)
            data = data[4:]
        return data

    # Здесь мы получаем данные из фикстур с продуктами

    def handle(self, *args, **options):
        # print(self.json_read_categories())
        # print(self.json_read_products())
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category["pk"],
                         name_category=category["fields"]["name_category"],
                         description=category["fields"]["description"])
            )


        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product["pk"],
                         name_product=product["fields"]["name_product"],
                         description=product["fields"]["description"],
                         category=Category.objects.get(
                                pk=product["fields"]["category"]),
                         price=product["fields"]["price"],
                         create_at=product["fields"]["create_at"],
                         update_at=product["fields"]["update_at"],
                         )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
