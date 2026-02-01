import json
from pathlib import Path

from src.category import Category
from src.products import Product


def read_json(path: str):
    """Читает json файл и возвращает данные в виде словаря."""
    file_path = Path(path)
    with open(file_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def create_obj_from_json(data):
    """Создает объекты из данных в json файле."""
    categories = []
    for category in data:
        products_data = category.get("products") or []
        products = [Product.new_product(p) for p in products_data]
        cat_obj = Category(
            name=category["name"],
            description=category["description"],
            list_products=products,
        )
        categories.append(cat_obj)
    return categories
