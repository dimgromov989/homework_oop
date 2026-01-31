from src.products import Product


class Category:
    name: str
    description: str
    quantity_categories = 0
    quantity_products = 0

    def __init__(self, name, description, list_products: list):
        self.name = name
        self.description = description
        self.__list_products = list_products if list_products else []
        Category.quantity_categories += 1
        Category.quantity_products += sum(
            product.quantity for product in self.__list_products
        )

    def __str__(self):
        """Стандартное строковое представление категории"""
        total_quantity = sum(p.quantity for p in self.__list_products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def list_products(self) -> str:
        """Возвращает строковое представление всех товаров категории"""
        return "\n".join(str(product) for product in self.__list_products) + (
            "\n" if self.__list_products else ""
        )

    def add_product(self, product: Product):
        """Добавляет товар в список товаров."""
        if isinstance(product, Product):
            for item in self.__list_products:
                if item.name.lower() == product.name.lower():
                    item.quantity += product.quantity
                    item.price = max(item.price, product.price)
                    return
            self.__list_products.append(product)
            Category.quantity_products += product.quantity
