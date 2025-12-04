from src.products import Product


class Category:
    name: str
    description: str
    list_products: list
    quantity_categories = 0
    quantity_products = 0
    def __init__(self, name, description, list_products):
        self.name = name
        self.description = description
        self.list_products = list_products if list_products else []
        Category.quantity_categories += 1
        Category.quantity_products += len(list_products) if list_products else 0


if __name__ == '__main__':
    product_banana = Product(name="Банан", description="жёлтый", price=15.0, quantity=3)
    product_pomidor = Product(name="Помидор", description="азербайджанский", price=3.0, quantity=10)
    category_food = Category(name="Еда", description="Продукты питания", list_products=[product_banana, product_pomidor])

    print(category_food.name)
    print(category_food.list_products[0].name)
    print(category_food.quantity_products)
    print(category_food.quantity_categories)







