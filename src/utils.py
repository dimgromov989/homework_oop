import json
from pathlib import Path

from src.category import Category
from src.products import Product


def read_json(path: str):
    file_path = Path(path)
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def create_obj_from_json(data):
    categories = []
    for category in data:
        products = [Product(**p) for p in category.get("products")]
        cat_obj = Category(
            name=category["name"],
            description=category["description"],
            list_products=products
        )
        categories.append(cat_obj)
    return categories




if __name__ == '__main__':
    result = read_json("../data/products.json")
    obj_result = create_obj_from_json(result)

    print(obj_result)


