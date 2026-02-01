from src.products import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products: list):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in self.__products)

    def __str__(self):
        """Стандартное строковое представление категории"""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех товаров категории"""
        return "\n".join(str(product) for product in self.__products) + (
            "\n" if self.__products else ""
        )

    def add_product(self, product: Product):
        """Добавляет товар в список товаров."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")

        for item in self.__products:
            if item.name.lower() == product.name.lower():
                item.quantity += product.quantity
                item.price = max(item.price, product.price)
                Category.product_count += product.quantity
                return
        self.__products.append(product)
        Category.product_count += product.quantity
