from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация объекта Product"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity is None:
            quantity = 0
        if quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """Стандартное строковое представление объекта Product"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение двух объектов Product, с учетом типа объектов"""
        if type(self) is type(other):
            if isinstance(other, Product):
                total_quantity = (self.quantity * self.__price) + (
                    other.quantity * other.__price
                )
                return (
                    "Сумма с учетом количества товаров на складе: "
                    f"{float(total_quantity)} руб."
                )
        raise TypeError("Ошибка: невозможно сложить два объекта разных типов")

    @classmethod
    def new_product(cls, product_data: dict):
        """Создание нового объекта Product из словаря"""
        quantity = product_data.get("quantity")
        if quantity is None:
            quantity = 0
        return cls(
            product_data.get("name"),
            product_data.get("description"),
            product_data.get("price"),
            quantity,
        )

    @property
    def price(self):
        """Получение цены товара"""
        return self.__price

    @price.setter
    def price(self, value):
        """Понижение цены товара"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            user_input = (
                input("Вы действительно хотите понизить цену? (y/n): ").strip().lower()
            )
            if user_input != "y":
                print("Изменение цены отменено")
                return
        self.__price = value
