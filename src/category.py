from src.exceptions import MyValueError
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
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты Product")
            if product.quantity <= 0:
                raise MyValueError()
            found = False
            for item in self.__products:
                if item.name.lower() == product.name.lower():
                    item.quantity += product.quantity
                    item.price = max(item.price, product.price)
                    Category.product_count += product.quantity
                    found = True
                    break
            if not found:
                self.__products.append(product)
                Category.product_count += product.quantity
        except MyValueError as e:
            print(e)
        else:
            print("Товар успешно добавлен")
        finally:
            print("Операция завершена")

    def middle_price(self):
        """Возвращает средний ценник товаров в категории"""
        try:
            total_price = sum(product.price for product in self.__products)
            average = total_price / len(self.__products)
            return average
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
